# CI/CD Seguro con GitHub Actions, GCP, Linux e IaC (Py271)

> Estado: En preparacion | Serie: py2xx | Nivel: Intermedio-Avanzado

Este repositorio contiene la base del curso Py271, orientado a integracion y entrega continua segura con GitHub Actions, Google Cloud Platform, Linux e infraestructura como codigo.

La estructura sigue el patron operativo usado en cursos basados en notebooks: el recorrido principal vive en notebooks numeradas en la raiz, mientras que las aplicaciones e infraestructura auxiliar pueden integrarse como submodulos Git separados.

El contenido base de GitHub Actions esta integrado directamente al enfoque editorial de Pythonista y extendido para cubrir seguridad de cadena de suministro, GCP, Linux e IaC dentro de la serie py2xx.

## Objetivo del curso

Construir un pipeline funcional de CI/CD que cubra:

- calidad y pruebas automatizadas;
- construccion de contenedores;
- seguridad de cadena de suministro;
- aprovisionamiento con Terraform;
- despliegue seguro en GCP y Linux.

## Modalidad sugerida

Py271 esta empaquetado como taller de 16 horas en 8 sesiones de 2 horas. La distribucion recomendada es:

- Sesion 1: marco DevSecOps, workflows de repositorio y fundamentos de GitHub Actions.
- Sesion 2: YAML, sintaxis de workflows, linters y tipado.
- Sesion 3: pruebas automatizadas, matrices y estrategia por entornos.
- Sesion 4: build de contenedores, Artifact Registry, escaneo y trazabilidad.
- Sesion 5: OIDC, Terraform base y despliegue hacia Google Cloud Functions.
- Sesion 6: Compute Engine, red y pipelines de infraestructura.
- Sesion 7: despliegue Linux por SSH, observabilidad y rollback.
- Sesion 8: proyecto final end to end.

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
├── 01_*.ipynb ... 17_*.ipynb
├── INSTRUCTOR_GUIDE.md
├── README.md
└── requirements.txt
```

## Submodulos sugeridos

- apps/api-github-actions-demo: aplicacion base del curso.
- infra/terraform-py271: infraestructura del curso con Terraform.

La plantilla deja estos componentes documentados, pero no agrega submodulos reales todavia.

## Tabla de contenidos

- 01 - DevSecOps, workflows de repositorio y entornos
- 02 - Introduccion a CI/CD y GitHub Actions
- 03 - YAML y sintaxis de workflows
- 04 - Linters y tipado en pipeline
- 05 - Pruebas automatizadas con pytest
- 06 - Matriz de versiones y entornos
- 07 - Build de contenedores en Actions
- 08 - Seguridad de dependencias e imagenes
- 09 - SBOM, provenance y attestations
- 10 - IAM, OIDC y autenticacion sin llaves
- 11 - Terraform: fundamentos y estado remoto
- 12 - Terraform para Artifact Registry y Google Cloud Functions
- 13 - Terraform para Compute Engine y red
- 14 - Pipelines de infraestructura: plan y apply
- 15 - Despliegue seguro en Linux
- 16 - Observabilidad, smoke tests y rollback
- 17 - Proyecto final end to end

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
- 01_devsecops_workflows_de_repos_y_entornos.ipynb funciona como capitulo marco para alinear lenguaje y criterios operativos.
- El recorrido tecnico contempla tanto builds con GitHub Actions como la opcion de construir en GCP con Google Cloud Build.
- Google Artifact Registry funciona como registro principal de artefactos e imagenes en GCP.
- La ruta serverless del curso se enfoca en Google Cloud Functions para cargas ligeras y orientadas a eventos.
- El despliegue en Linux contempla una ruta explicita de despliegue remoto por SSH hacia servidores endurecidos.
- La observabilidad se trata como parte del pipeline de entrega: logs, metricas, alertas, smoke tests y rollback.
- apps/ contiene aplicaciones auxiliares como submodulos Git.
- infra/ contiene repositorios de IaC como submodulos Git o material de apoyo.
- ejercicios_resueltos/ sirve para practica posterior a clase.