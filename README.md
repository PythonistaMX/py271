# CI/CD Seguro con GitHub Actions, GCP, Linux e IaC (Py271)

> Estado: En preparación | Serie: py2xx | Nivel: Intermedio-Avanzado

## Nota sobre nivel

Este curso se considera principalmente de nivel intermedio, con algunos tramos intermedio-avanzados.

- Recomendado para perfiles con experiencia previa en desarrollo (especialmente backend) y uso habitual de Git.
- No está orientado a iniciar desde cero en programación o en flujo de trabajo técnico.
- Para perfiles senior, funciona como consolidación práctica de CI/CD seguro y operación DevSecOps.

Este repositorio contiene el material del curso orientado a integración y entrega continua segura con GitHub Actions, Google Cloud Platform, Linux e infraestructura como código.

La estructura sigue el patrón operativo usado en cursos basados en notebooks: el recorrido principal vive en notebooks numeradas en la raíz, mientras que las aplicaciones e infraestructura auxiliar pueden integrarse como submódulos Git separados.

## Objetivo del curso

Construir un pipeline funcional de CI/CD que cubra:

- calidad y pruebas automatizadas;
- construcción de contenedores;
- seguridad de cadena de suministro;
- aprovisionamiento con Terraform;
- despliegue seguro en GCP y Linux.

## Perfil del alumno

Programador (principalmente Python, pero no exclusivamente) con experiencia en desarrollo back-end o full-stack.

Se asume:
- fluidez con Python;
- uso cotidiano de git: commits, branches, merges y pull requests.

No se asume conocimiento previo de DevSecOps, CI/CD, IaC ni pipelines de entrega.

## Modalidad sugerida

El curso está empaquetado como taller de 16 horas en 8 sesiones de 2 horas. La distribución recomendada es:

- Sesión 1: CI/CD y riesgos actuales, flujos de trabajo y plataforma GitHub.
- Sesión 2: Marco DevSecOps, introducción a GitHub Actions y sintaxis YAML.
- Sesión 3: Matriz de versiones y entornos; linters, tipado y pruebas automatizadas.
- Sesión 4: SBOM, provenance, seguridad de dependencias e IAM/OIDC.
- Sesión 5: Build de contenedores y runners endurecidos; Terraform: fundamentos y estado remoto.
- Sesión 6: Terraform para Artifact Registry, Cloud Functions y Compute Engine.
- Sesión 7: Pipelines de infraestructura y despliegue seguro en Linux.
- Sesión 8: Observabilidad, rollback y proyecto final end to end.

## Bloque temático central

El tramo central del curso integra, de forma progresiva, estos conceptos:

- marco operativo de *DevSecOps* y entornos;
- diseño de *workflows* en *GitHub Actions*;
- ejecución con matriz de versiones y promoción por entornos;
- *quality gates* con linters, tipado y pruebas automatizadas;
- seguridad de cadena de suministro: *SBOM*, *provenance*, *attestations* y escaneo;
- identidad federada con *OIDC* para evitar llaves estáticas;
- *build* de contenedores con criterio de *runners hosted* y *self-hosted* endurecidos.

## Modelo de entornos del curso

El curso trabaja con tres entornos operativos bien diferenciados:

- *dev*: máquina del desarrollador con SQLite para iteración rápida local.
- *test*: servidor Linux hosteado con PostgreSQL para validar despliegue remoto y operación realista.
- *prod*: GCP con Cloud SQL para PostgreSQL y publicación en Cloud Functions (2nd gen, sobre Cloud Run).

La promoción mantiene el mismo artefacto entre entornos para conservar trazabilidad y evitar reconstrucciones por ambiente.

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

## Submódulos sugeridos

- `apps/api-github-actions-demo`: aplicación base del curso.
- `infra/terraform-py271`: infraestructura del curso con Terraform.

La plantilla deja estos componentes documentados, pero no registra submódulos reales todavía.

## Tabla de contenidos

- 01 - Introducción a CI/CD y riesgos actuales
- 02 - Flujos de trabajo con Git
- 03 - GitHub: plataforma y funcionalidades de seguridad
- 04 - DevSecOps, workflows de repositorio y entornos
- 05 - Introducción a CI/CD y GitHub Actions
- 06 - YAML y sintaxis de workflows
- 07 - Matriz de versiones y entornos
- 08 - Linters y tipado en pipeline
- 09 - Pruebas automatizadas con pytest
- 10 - SBOM, provenance y attestations
- 11 - Seguridad de dependencias e imágenes
- 12 - IAM, OIDC y autenticación sin llaves
- 13 - Build de contenedores y runners endurecidos en Actions
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

Si después agregas submódulos:

```bash
git submodule update --init --recursive
```

## Notas de operación

- Las notebooks de la raíz son el material troncal del curso.
- `04_devsecops_workflows_de_repos_y_entornos.ipynb` fija el lenguaje y los criterios operativos del curso.
- GitHub Actions opera como plano de control principal del pipeline.
- El uso de self-hosted runners se reserva para necesidades técnicas justificadas (red privada, segmentación o cumplimiento).
- Google Cloud Build se presenta como alternativa avanzada, no como ruta principal.
- Google Artifact Registry funciona como registro principal de artefactos e imágenes en GCP.
- La ruta serverless del curso se enfoca en Google Cloud Functions para cargas ligeras y orientadas a eventos.
- Aunque Kubernetes tambien ejecuta cargas contenerizadas, en este curso no se adopta como ruta base porque el caso de estudio no responde a una arquitectura de microservicios que justifique su complejidad operativa.
- El modelo de entornos oficial es: *dev* en local con SQLite, *test* en Linux con PostgreSQL y *prod* en GCP con Cloud SQL PostgreSQL.
- El despliegue en Linux contempla una ruta explícita de despliegue remoto por SSH hacia servidores endurecidos.
- La observabilidad se trata como parte del pipeline de entrega: logs, métricas, alertas, smoke tests y rollback.
- `apps/` contiene aplicaciones auxiliares como submódulos Git.
- `infra/` contiene repositorios de IaC como submódulos Git o material de apoyo.
- `ejercicios_resueltos/` sirve para práctica posterior a clase.
