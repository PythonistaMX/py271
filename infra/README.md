# Infraestructura del curso

Esta carpeta contiene el material de infraestructura como código (IaC) del curso.

## Contenido

- **`terraform-py271/`** — Stack GCP para la aplicación `api-github-actions-demo`:
  Artifact Registry, Cloud SQL PostgreSQL, Cloud Run y configuración de
  Workload Identity Federation para autenticación OIDC desde GitHub Actions.

## Arquitectura de prod

```
GitHub Actions
    │  OIDC (sin llaves estáticas)
    ▼
cicd-deployer SA
    │  roles/run.admin + roles/artifactregistry.writer
    ▼
Cloud Run ──────────────── Cloud SQL (PostgreSQL 15)
(apiflask-demo-runtime SA)     (socket Unix via Auth Proxy)
    │
    │  roles/secretmanager.secretAccessor (solo DATABASE_URL)
    ▼
Secret Manager
(DATABASE_URL — valor poblado manualmente tras terraform apply)
```

## Flujo recomendado: Terraform + OIDC

1. `plan` y `apply` desde GitHub Actions con entornos protegidos (`test`, `prod`).
2. Autenticación a GCP mediante OIDC + Workload Identity Federation — sin llaves JSON.
3. Promotion de imagen inmutable desde GHCR a Cloud Run entre `test` y `prod`.

## Variables de GitHub Actions requeridas por los workflows de despliegue

Configura estas variables en `Settings → Environments → prod → Variables`.
Los valores se obtienen de los outputs de Terraform tras `terraform apply`.

| Variable | Fuente |
|---|---|
| `GCP_PROJECT_ID` | `terraform.tfvars` |
| `GCP_REGION` | `terraform.tfvars` |
| `GCP_WORKLOAD_IDENTITY_PROVIDER` | `terraform output workload_identity_provider` |
| `GCP_SERVICE_ACCOUNT` | `terraform output cicd_service_account_email` |
| `GCP_CLOUD_SQL_CONNECTION_NAME` | `terraform output cloud_sql_instance_connection_name` |
| `GCP_CLOUD_RUN_SERVICE` | `terraform output cloud_run_service_name` |
| `TF_STATE_BUCKET` | Nombre del bucket GCS para el estado remoto de Terraform |

## Buenas prácticas aplicadas

- No usar llaves estáticas de GCP (`*.json`) en GitHub Secrets.
- Separar SA de CI/CD (`cicd-deployer`) del SA de runtime de Cloud Run.
- `DATABASE_URL` en Secret Manager (no como variable de entorno plana); el runtime SA tiene acceso solo a ese secreto.
- `lifecycle.ignore_changes` en Cloud Run para que Terraform no revierta imágenes.
- `deletion_protection = true` en Cloud SQL para entornos productivos.
- Separar jobs de `plan` y `apply`, con aprobación manual en `prod`.

## Alta como submódulo

```bash
git submodule add https://github.com/PythonistaMX/terraform-py271.git infra/terraform-py271
git submodule update --init --recursive
```
