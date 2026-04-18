# Infraestructura del curso

Esta carpeta se reserva para repositorios de IaC o material de infraestructura asociado al curso.

## Sugerencia inicial

- terraform-py271: recursos para GCP, Artifact Registry, Google Cloud Functions, Compute Engine y componentes base del despliegue.

## Ejemplo de alta de submodulo

```bash
git submodule add https://github.com/TU_ORG/terraform-py271.git infra/terraform-py271
git submodule update --init --recursive
```