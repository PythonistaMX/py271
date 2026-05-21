# Infraestructura del curso

Esta carpeta se reserva para repositorios de IaC o material de infraestructura asociado al curso.

## Sugerencia inicial

- terraform-py271: recursos para GCP, Artifact Registry, Google Cloud Functions, Compute Engine y componentes base del despliegue.

## Flujo recomendado: Terraform + OIDC

Modelo operativo sugerido:

1. `plan` y `apply` de Terraform desde GitHub Actions con entornos protegidos.
2. Autenticación a GCP mediante OIDC + Workload Identity Federation.
3. Promoción de un artefacto inmutable entre `test` y `prod`.

Variables de entorno recomendadas en GitHub (`Environment variables`):

- `GCP_PROJECT_ID`
- `GCP_REGION`
- `GCP_WORKLOAD_IDENTITY_PROVIDER`
- `GCP_SERVICE_ACCOUNT`
- `TF_STATE_BUCKET` (si usas backend remoto en GCS)

Secretos de entorno recomendados (`Environment secrets`):

- `TF_VAR_db_password` (si aplica)
- secretos propios de aplicación (si no están en Secret Manager)

Buenas prácticas del curso:

- No usar llaves estáticas de GCP (`*.json`) en GitHub.
- Usar `permissions: id-token: write` y `contents: read` en workflows.
- Separar jobs de `plan` y `apply`, con aprobación manual en `prod`.
- Mantener módulos y proveedores de Terraform versionados/pineados.

## Ejemplo de alta de submodulo

```bash
git submodule add https://github.com/TU_ORG/terraform-py271.git infra/terraform-py271
git submodule update --init --recursive
```