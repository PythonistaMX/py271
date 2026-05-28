# Guía operativa de GCP y entornos

Instrucciones paso a paso para habilitar los tres entornos del curso.
Este archivo no se versiona — contiene referencias a valores sensibles específicos de la instalación.

---

## Entornos del curso

| Entorno | Infraestructura | Base de datos | Gestionado con |
|---|---|---|---|
| `dev` | Máquina del desarrollador | SQLite | — |
| `test` | Servidor Linux con Docker y PostgreSQL | PostgreSQL | Manual / Ansible |
| `prod` | GCP — Cloud Run v2 + Cloud SQL | Cloud SQL PostgreSQL | Terraform |

---

## Entorno `dev` — Máquina del desarrollador

No requiere configuración de infraestructura. Basta con instalar dependencias y correr las pruebas localmente:

```bash
cd apps/api-github-actions-demo
uv sync --frozen --extra dev
uv run pytest --cov=apiflaskdemo --cov-fail-under=80
```

No requiere entorno en GitHub Actions: ningún workflow referencia el entorno `dev`.

---

## Entorno `test` — Servidor Linux

### En el servidor

```bash
# Instalar PostgreSQL
sudo apt-get update && sudo apt-get install -y postgresql postgresql-contrib

# Crear usuario y base de datos
sudo -u postgres psql <<'SQL'
CREATE USER app_user WITH PASSWORD '<contraseña>';
CREATE DATABASE apiflask OWNER app_user;
SQL

# Permitir conexiones remotas si el runner de GitHub Actions no es local
# 1. Editar /etc/postgresql/*/main/postgresql.conf
#      listen_addresses = '*'
# 2. Editar /etc/postgresql/*/main/pg_hba.conf
#      host  apiflask  app_user  <IP-del-runner>/32  scram-sha-256
sudo systemctl restart postgresql
```

### GitHub Actions — entorno `test`

`Settings → Environments → test`

| Tipo | Nombre | Valor |
|---|---|---|
| Variable | `DATABASE_URL` | `postgresql://app_user:<pass>@<host>:5432/apiflask` |
| Secreto | `APP_SECRET_KEY` | string aleatorio ≥ 32 chars |
| Secreto | `APP_SECURITY_PASSWORD_SALT` | string aleatorio ≥ 32 chars |

No requiere gcloud, Terraform ni ningún recurso de GCP.

---

## Entorno `prod` — GCP

### Paso 0 — Requisitos previos

- Proyecto GCP con facturación habilitada.
- [`gcloud` CLI](https://cloud.google.com/sdk/docs/install) instalado y actualizado.
- [Terraform](https://developer.hashicorp.com/terraform/install) >= 1.6.0.
- Permisos de Owner o Editor en el proyecto GCP.

```bash
gcloud auth login
gcloud auth application-default login
gcloud config set project <PROJECT_ID>
```

### Paso 1 — Habilitar APIs

```bash
gcloud services enable \
  run.googleapis.com \
  sqladmin.googleapis.com \
  secretmanager.googleapis.com \
  iam.googleapis.com \
  iamcredentials.googleapis.com \
  cloudresourcemanager.googleapis.com \
  --project=<PROJECT_ID>
```

### Paso 2 — Bucket GCS para estado remoto de Terraform

```bash
gcloud storage buckets create gs://<TF_STATE_BUCKET> \
  --project=<PROJECT_ID> \
  --location=<REGION> \
  --uniform-bucket-level-access

gcloud storage buckets update gs://<TF_STATE_BUCKET> --versioning
```

> Elige un nombre único globalmente, por ejemplo `tf-state-<PROJECT_ID>`.

### Paso 3 — Preparar `terraform.tfvars`

```bash
cd infra/terraform-py271
cp terraform.tfvars.example terraform.tfvars
```

Editar `terraform.tfvars`:

```hcl
project_id                 = "<PROJECT_ID>"
region                     = "<REGION>"          # ej. us-central1
environment                = "prod"
app_name                   = "apiflask-demo"
cloud_sql_instance_name    = "apiflask-prod-sql"
cloud_sql_database_name    = "apiflask"
cloud_sql_tier             = "db-f1-micro"
db_username                = "app_user"
enable_deletion_protection = true
github_repository          = "org/api-github-actions-demo"
cloud_run_service_name     = "apiflask-demo"
```

La contraseña de base de datos **nunca** va en el archivo:

```bash
export TF_VAR_db_password="$(python3 -c 'import secrets; print(secrets.token_hex(24))')"
```

### Paso 4 — Primer `terraform apply`

```bash
terraform init \
  -backend-config="bucket=<TF_STATE_BUCKET>" \
  -backend-config="prefix=prod/terraform"

terraform fmt -check -recursive
terraform validate
terraform plan
terraform apply
```

Al terminar, capturar los outputs:

```bash
terraform output
```

| Output de Terraform | Uso |
|---|---|
| `workload_identity_provider` | → `GCP_WORKLOAD_IDENTITY_PROVIDER` en GitHub |
| `cicd_service_account_email` | → `GCP_SERVICE_ACCOUNT` en GitHub |
| `cloud_sql_instance_connection_name` | → `GCP_CLOUD_SQL_CONNECTION_NAME` en GitHub y paso 5 |
| `cloud_sql_database_name` | → variable `DB_NAME` en paso 5 |
| `cloud_run_service_name` | → `GCP_CLOUD_RUN_SERVICE` en GitHub |
| `cloud_run_service_url` | → URL para verificación final |
| `database_url_secret_name` | → verificación del secreto creado en Secret Manager |

### Paso 5 — Poblar secretos en Secret Manager

#### `DATABASE_URL` (contenedor creado por Terraform, valor manual)

```bash
CONN=$(terraform output -raw cloud_sql_instance_connection_name)
DB_NAME=$(terraform output -raw cloud_sql_database_name)

gcloud secrets versions add DATABASE_URL \
  --data-file=<(echo -n "postgresql://app_user:${TF_VAR_db_password}@/${DB_NAME}?host=/cloudsql/${CONN}")
```

#### `APP_SECRET_KEY` y `APP_SECURITY_PASSWORD_SALT`

Genera los valores primero y guárdalos: los necesitarás en el paso 7 como secretos de GitHub Actions.

```bash
APP_SECRET_KEY_VAL=$(python3 -c 'import secrets; print(secrets.token_hex(32))')
APP_SALT_VAL=$(python3 -c 'import secrets; print(secrets.token_hex(32))')

echo "APP_SECRET_KEY:             $APP_SECRET_KEY_VAL"
echo "APP_SECURITY_PASSWORD_SALT: $APP_SALT_VAL"
```

Copia esos valores en un gestor de contraseñas. Luego súbelos a Secret Manager:

```bash
gcloud secrets create APP_SECRET_KEY --replication-policy=automatic
echo -n "$APP_SECRET_KEY_VAL" | gcloud secrets versions add APP_SECRET_KEY --data-file=-

gcloud secrets create APP_SECURITY_PASSWORD_SALT --replication-policy=automatic
echo -n "$APP_SALT_VAL" | gcloud secrets versions add APP_SECURITY_PASSWORD_SALT --data-file=-
```

#### Permisos del runtime SA sobre `APP_SECRET_KEY` y `APP_SECURITY_PASSWORD_SALT`

```bash
PROJECT_ID=<PROJECT_ID>
APP_NAME=apiflask-demo
RUNTIME_SA="${APP_NAME}-runtime@${PROJECT_ID}.iam.gserviceaccount.com"

for SECRET in APP_SECRET_KEY APP_SECURITY_PASSWORD_SALT; do
  gcloud secrets add-iam-policy-binding $SECRET \
    --member="serviceAccount:${RUNTIME_SA}" \
    --role="roles/secretmanager.secretAccessor"
done
```

### Paso 6 — Acceso público a Cloud Run (si el servicio es público)

```bash
gcloud run services add-iam-policy-binding apiflask-demo \
  --region=<REGION> \
  --member="allUsers" \
  --role="roles/run.invoker"
```

Si el servicio se mantiene privado, el smoke test del workflow ya usa un identity token.

### Paso 7 — Configurar entornos en GitHub Actions

#### Repo de la app — entorno `test`

`Settings → Environments → test`

Usado por `python-app-test.yml` (PRs y push a `main`) y `envia-a-packages.yml` (tags prerelease).

| Tipo | Nombre | Valor |
|---|---|---|
| Variable | `DATABASE_URL` | `postgresql://app_user:<pass>@/<db>?host=/cloudsql/<connection_name>` |
| Secreto | `APP_SECRET_KEY` | string aleatorio ≥ 32 chars |
| Secreto | `APP_SECURITY_PASSWORD_SALT` | string aleatorio ≥ 32 chars |

#### Repo de la app — entorno `prod`

`Settings → Environments → prod`

Usado por `despliega-cloud-run.yaml` (tags estables `v1.2.3`).

| Tipo | Nombre | Origen |
|---|---|---|
| Variable | `GCP_PROJECT_ID` | `<PROJECT_ID>` |
| Variable | `GCP_REGION` | `<REGION>` |
| Variable | `GCP_WORKLOAD_IDENTITY_PROVIDER` | `terraform output workload_identity_provider` |
| Variable | `GCP_SERVICE_ACCOUNT` | `terraform output cicd_service_account_email` |
| Variable | `GCP_CLOUD_RUN_SERVICE` | `terraform output cloud_run_service_name` |
| Variable | `GCP_CLOUD_SQL_CONNECTION_NAME` | `terraform output cloud_sql_instance_connection_name` |
| Variable | `GCP_ARTIFACT_REGISTRY` | `terraform output artifact_registry_url` |
| Secreto | `APP_SECRET_KEY` | mismo valor que pusiste en Secret Manager |
| Secreto | `APP_SECURITY_PASSWORD_SALT` | mismo valor que pusiste en Secret Manager |

#### Repo de infra — entorno `prod`

`Settings → Environments → prod` (en `infra/terraform-py271`)

| Tipo | Nombre | Valor |
|---|---|---|
| Variable | `GCP_PROJECT_ID` | `<PROJECT_ID>` |
| Variable | `GCP_REGION` | `<REGION>` |
| Variable | `GCP_WORKLOAD_IDENTITY_PROVIDER` | `terraform output workload_identity_provider` |
| Variable | `GCP_SERVICE_ACCOUNT` | `terraform output cicd_service_account_email` |
| Variable | `APP_NAME` | `apiflask-demo` |
| Variable | `CLOUD_SQL_INSTANCE_NAME` | valor de `terraform.tfvars` |
| Variable | `CLOUD_SQL_DATABASE_NAME` | valor de `terraform.tfvars` |
| Variable | `CLOUD_SQL_TIER` | `db-f1-micro` |
| Variable | `DB_USERNAME` | `app_user` |
| Variable | `ENABLE_DELETION_PROTECTION` | `true` |
| Variable | `APP_GITHUB_REPOSITORY` | `PythonistaMX/api-github-actions-demo` |
| Variable | `GCP_CLOUD_RUN_SERVICE` | `terraform output cloud_run_service_name` |
| Variable | `TF_STATE_BUCKET` | nombre del bucket del paso 2 |
| Secreto | `DB_PASSWORD` | valor de `TF_VAR_db_password` |

### Paso 8 — Verificar el pipeline completo

```bash
# Tag prerelease → envia-a-packages.yml → publica imagen en GHCR (test/dev)
git tag v0.1.0-rc.1 && git push --tags

# Tag estable → despliega-cloud-run.yaml → build + AR + deploy prod (blue/green)
git tag v0.1.0 && git push --tags

# Verificar el servicio en vivo
curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
  "$(terraform output -raw cloud_run_service_url)/api/alumnos/"
```

---

## Secretos y variables — resumen completo

### GitHub Actions — secretos de repositorio (repo de la app)

| Secreto | Workflows |
|---|---|
| `DOCKER_USERNAME` | `envia-a-docker.yaml` |
| `DOCKER_PASSWORD` | `envia-a-docker.yaml` |

### GitHub Actions — por entorno

| Tipo | Nombre | `dev` | `test` | `prod` |
|---|---|---|---|---|
| Variable | `DATABASE_URL` | — | `postgresql://...` | — (Secret Manager) |
| Secreto | `APP_SECRET_KEY` | — | ✓ | ✓ |
| Secreto | `APP_SECURITY_PASSWORD_SALT` | — | ✓ | ✓ |
| Variable | `GCP_PROJECT_ID` | — | — | ✓ |
| Variable | `GCP_REGION` | — | — | ✓ |
| Variable | `GCP_WORKLOAD_IDENTITY_PROVIDER` | — | — | ✓ |
| Variable | `GCP_SERVICE_ACCOUNT` | — | — | ✓ |
| Variable | `GCP_CLOUD_RUN_SERVICE` | — | — | ✓ |
| Variable | `GCP_CLOUD_SQL_CONNECTION_NAME` | — | — | ✓ |
| Variable | `GCP_ARTIFACT_REGISTRY` | — | — | ✓ |

### GCP Secret Manager

| Secreto | Crea el contenedor | Puebla el valor | Lo lee |
|---|---|---|---|
| `DATABASE_URL` | Terraform | Operador (paso 5) | Runtime SA vía `value_source.secret_key_ref` |
| `APP_SECRET_KEY` | Operador (paso 5) | Operador (paso 5) | Runtime SA vía `--update-secrets` |
| `APP_SECURITY_PASSWORD_SALT` | Operador (paso 5) | Operador (paso 5) | Runtime SA vía `--update-secrets` |
