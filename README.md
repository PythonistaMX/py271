# CI/CD Seguro con GitHub Actions, GCP, Linux e IaC (Py271)

> Estado: En preparacion | Serie: py2xx | Nivel: Intermedio-Avanzado

Este repositorio contiene el material del curso orientado a integracion y entrega continua segura con GitHub Actions, Google Cloud Platform, Linux e infraestructura como codigo.

La estructura sigue el patron operativo usado en cursos basados en notebooks: el recorrido principal vive en notebooks numeradas en la raiz, mientras que las aplicaciones e infraestructura auxiliar pueden integrarse como submodulos Git separados.

## Objetivo del curso

Construir un pipeline funcional de CI/CD que cubra:

- calidad y pruebas automatizadas;
- construccion de contenedores;
- seguridad de cadena de suministro;
- aprovisionamiento con Terraform;
- despliegue seguro en GCP y Linux.

## Perfil del alumno

Programador (principalmente Python, pero no exclusivamente) con experiencia en desarrollo back-end o full-stack. Se asume fluidez con Python y git. No se asume conocimiento previo de DevSecOps, CI/CD, IaC ni pipelines de entrega.

## Modalidad sugerida

El curso esta empaquetado como taller de 16 horas en 8 sesiones de 2 horas. La distribucion recomendada es:

- Sesion 1: CI/CD y riesgos actuales, flujos de trabajo y plataforma GitHub.
- Sesion 2: Marco DevSecOps, introduccion a GitHub Actions y sintaxis YAML.
- Sesion 3: Linters, tipado y pruebas automatizadas; matrices y entornos.
- Sesion 4: Build de contenedores, SBOM, provenance y seguridad de dependencias.
- Sesion 5: IAM, OIDC y Terraform: fundamentos y estado remoto.
- Sesion 6: Terraform para Artifact Registry, Cloud Functions y Compute Engine.
- Sesion 7: Pipelines de infraestructura y despliegue seguro en Linux.
- Sesion 8: Observabilidad, rollback y proyecto final end to end.

## Estructura del repositorio

```text
py271/
├── .devcontainer/
├── apps/
├── data/
├── demos/
├── ejercicios_resueltos/
├── img/
├── infra/
├── 01_*.ipynb ... 20_*.ipynb
├── INSTRUCTOR_GUIDE.md
├── README.md
└── requirements.txt
```

## Submodulos sugeridos

- `apps/api-github-actions-demo`: aplicacion base del curso.
- `infra/terraform-py271`: infraestructura del curso con Terraform.

La plantilla deja estos componentes documentados, pero no registra submodulos reales todavia.

## Tabla de contenidos

- 01 - Introduccion a CI/CD y riesgos actuales
- 02 - Flujos de trabajo con Git
- 03 - GitHub: plataforma y funcionalidades de seguridad
- 04 - DevSecOps, workflows de repositorio y entornos
- 05 - Introduccion a CI/CD y GitHub Actions
- 06 - YAML y sintaxis de workflows
- 07 - Linters y tipado en pipeline
- 08 - Pruebas automatizadas con pytest
- 09 - Matriz de versiones y entornos
- 10 - Build de contenedores en Actions
- 11 - SBOM, provenance y attestations
- 12 - Seguridad de dependencias e imagenes
- 13 - IAM, OIDC y autenticacion sin llaves
- 14 - Terraform: fundamentos y estado remoto
- 15 - Terraform para Artifact Registry y Cloud Functions
- 16 - Terraform para Compute Engine y red
- 17 - Pipelines de infraestructura: plan y apply
- 18 - Despliegue seguro en Linux
- 19 - Observabilidad, smoke tests y rollback
- 20 - Proyecto final end to end

## Uso local

```bash
git clone <repo>
cd py271
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Si despues agregas submodulos:

```bash
git submodule update --init --recursive
```

## Notas de operacion

- Las notebooks de la raiz son el material troncal del curso.
- `04_devsecops_workflows_de_repos_y_entornos.ipynb` fija el lenguaje y los criterios operativos del curso.
- El recorrido tecnico contempla tanto builds con GitHub Actions como la opcion de construir en GCP con Google Cloud Build.
- Google Artifact Registry funciona como registro principal de artefactos e imagenes en GCP.
- La ruta serverless del curso se enfoca en Google Cloud Functions para cargas ligeras y orientadas a eventos.
- El despliegue en Linux contempla una ruta explicita de despliegue remoto por SSH hacia servidores endurecidos.
- La observabilidad se trata como parte del pipeline de entrega: logs, metricas, alertas, smoke tests y rollback.
- `apps/` contiene aplicaciones auxiliares como submodulos Git.
- `infra/` contiene repositorios de IaC como submodulos Git o material de apoyo.
- `ejercicios_resueltos/` sirve para practica posterior a clase.
