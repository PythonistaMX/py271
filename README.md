# CI/CD Seguro con GitHub Actions, GCP, Linux e IaC (Py271)

> Estado: En preparación | Serie: py2xx | Nivel: Avanzado

## Nota sobre nivel

Este es un curso avanzado. El proyecto final construye un pipeline de CI/CD de nivel productivo con seguridad de cadena de suministro, identidad federada y despliegue blue/green en GCP.

- Requiere experiencia previa en desarrollo backend, contenedores y uso fluido de Git.
- Los tramos de Terraform (NB13–17) se cubren desde fundamentos, pero se aplican en configuraciones de producción real.
- Los tramos de IAM y OIDC (NB16, NB19–20) implican conceptos como Workload Identity Federation, auto-impersonación de service accounts e identity tokens efímeros.
- Para perfiles senior con experiencia en GCP, el curso añade profundidad en DevSecOps y seguridad de cadena de suministro.

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

Se asume haber completado cd441 o tener experiencia equivalente en CI/CD con GitHub Actions. No se asume conocimiento previo de DevSecOps, IaC ni seguridad de cadena de suministro, pero sí de pipelines básicos.

## Ruta de aprendizaje previa

Este curso es la continuación natural de la siguiente ruta del catálogo Cloudevel:

| Curso | Contenido | Nivel |
|---|---|---|
| [cd101 — GNU/Linux desde la línea de comandos](https://github.com/Cloudevel/cd101) | Shell, permisos, procesos, systemd, redes, SSH, seguridad básica | Introductorio |
| [cd411 — Introducción a Git](https://github.com/Cloudevel/cd411) | Control de versiones, ramas, resolución de conflictos, integración con GitHub | Introductorio |
| [cd421 — GitHub Avanzado](https://github.com/Cloudevel/cd421) | Administración de repos y organizaciones, GitHub Actions, entornos, secretos, `gh` CLI | Intermedio |
| [cd501 — Gestión de contenedores con Docker](https://github.com/Cloudevel/cd501) | Imágenes, contenedores, redes, volúmenes, registros privados, Docker Compose | Intermedio |
| [gcp101 — Google Cloud Platform](https://github.com/Cloudevel/gcp101) | IAM, Compute Engine, Cloud Run, Cloud SQL, Secret Manager, redes, operaciones | Intermedio |
| [cd441 — CI/CD con GitHub Actions](https://github.com/Cloudevel/cd441) | Pipelines reales, runners, artefactos, despliegue en GCP y Linux | Intermedio |
| **py271 — CI/CD Seguro** | Endurecimiento, DevSecOps, IaC, OIDC, cadena de suministro | **Avanzado** |

El prerrequisito directo es **cd441**. Los cursos cd101, cd501 y gcp101 proveen el contexto operativo que cd441 y este curso asumen conocido.

> **Nota sobre Terraform:** los notebooks 13 al 17 introducen Terraform desde fundamentos. No existe aún un curso dedicado de Terraform en la serie; ese material se cubre aquí por primera vez.

## Modalidad sugerida

El curso está empaquetado como taller de 16 horas en 8 sesiones de 2 horas. La distribución recomendada es:

- Sesión 1: CI/CD y riesgos actuales, flujos de trabajo y plataforma GitHub.
- Sesión 2: Marco DevSecOps, introducción a GitHub Actions y sintaxis YAML.
- Sesión 3: Matriz de versiones y entornos; linters, tipado y pruebas automatizadas.
- Sesión 4: SBOM, provenance y seguridad de dependencias e imágenes.
- Sesión 5: Build de contenedores en Actions; Terraform: fundamentos y estado remoto.
- Sesión 6: Terraform para Artifact Registry, Cloud Run y Compute Engine.
- Sesión 7: IAM, OIDC y autenticación sin llaves; pipelines de infraestructura y despliegue seguro en Linux.
- Sesión 8: Observabilidad, smoke tests, rollback y proyecto final end to end.

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
- *prod*: GCP con Cloud SQL para PostgreSQL y despliegue en Cloud Run v2.

La promoción mantiene el mismo artefacto entre entornos para conservar trazabilidad y evitar reconstrucciones por ambiente.

## Estructura del repositorio

```text
py271/
├── .devcontainer/
├── apps/
├── data/
├── demos/
├── img/
├── infra/
├── 01_*.ipynb ... 20_*.ipynb
├── INSTRUCTOR_GUIDE.md
├── README.md
└── requirements.txt
```

## Submódulos sugeridos

- `apps/api-github-actions-demo`: aplicación base del curso — API Flask con cinco workflows de CI/CD.
- `infra/terraform-py271`: infraestructura del curso con Terraform — Cloud Run, Cloud SQL, Artifact Registry y WIF/OIDC.

## Tabla de contenidos

- 01 - Introducción a CI/CD y riesgos actuales
- 02 - Flujos de trabajo con Git
- 03 - GitHub: plataforma y funcionalidades de seguridad
- 04 - DevSecOps, workflows de repositorio y entornos
- 05 - Introducción a CI/CD y GitHub Actions
- 06 - YAML y sintaxis de workflows
- 07 - Matriz de versiones y entornos
- 08 - Linters, tipado y gestores de paquetes y entornos
- 09 - Pruebas automatizadas con pytest
- 10 - SBOM, provenance y attestations
- 11 - Seguridad de dependencias e imágenes
- 12 - Build de contenedores en Actions
- 13 - Terraform: fundamentos y estado remoto
- 14 - Terraform para Artifact Registry y Cloud Run
- 15 - Terraform para Compute Engine y red
- 16 - IAM, OIDC y autenticación sin llaves
- 17 - Pipelines de infraestructura: plan y apply
- 18 - Despliegue seguro en Linux
- 19 - Observabilidad, smoke tests y rollback
- 20 - Proyecto final end to end
- 21 - Criterios y trade-offs de endurecimiento

## Demos

`demos/` contiene ejercicios ejecutables de apoyo a sesiones específicas:

| Carpeta | Sesión | Contenido |
|---|---|---|
| `demos/06/` | Sesión 2 — YAML y sintaxis de workflows | `blank.yml`: plantilla mínima de workflow para completar en clase |
| `demos/08/` | Sesión 3 — Linters, tipado y pruebas | `calculadora.py` con anotaciones de tipo + quality gates: `ruff`, `mypy` y `pytest` con `parametrize`; incluye reto de extensión |

Cada subcarpeta tiene su propio `README.md` con instrucciones de ejecución y reto.

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

Si el repositorio de infra no está disponible, usa `.gitmodules.example` como plantilla con URLs de marcador de posición:

```bash
cp .gitmodules.example .gitmodules
```

## Notas de operación

- Las notebooks de la raíz son el material troncal del curso.
- `04_devsecops_workflows_de_repos_y_entornos.ipynb` fija el lenguaje y los criterios operativos del curso.
- GitHub Actions opera como plano de control principal del pipeline.
- El uso de self-hosted runners se reserva para necesidades técnicas justificadas (red privada, segmentación o cumplimiento).
- Google Cloud Build se presenta como alternativa avanzada, no como ruta principal.
- GitHub Container Registry (*GHCR*) funciona como registro principal de artefactos e imágenes del curso.
- La ruta serverless del curso se enfoca en Google Cloud Run v2 para cargas contenerizadas orientadas a eventos.
- Aunque Kubernetes tambien ejecuta cargas contenerizadas, en este curso no se adopta como ruta base porque el caso de estudio no responde a una arquitectura de microservicios que justifique su complejidad operativa.
- El modelo de entornos oficial es: *dev* en local con SQLite, *test* en Linux con PostgreSQL y *prod* en GCP con Cloud SQL PostgreSQL.
- El despliegue en Linux contempla una ruta explícita de despliegue remoto por SSH hacia servidores endurecidos.
- La observabilidad se trata como parte del pipeline de entrega: logs, métricas, alertas, smoke tests y rollback.
- `apps/` contiene aplicaciones auxiliares como submódulos Git.
- `infra/` contiene repositorios de IaC como submódulos Git o material de apoyo.
- `ejercicios_resueltos/` sirve para práctica posterior a clase.
