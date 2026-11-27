# Instructor Guide - Py271

Guia operativa para impartir Py271 con consistencia tecnica y pedagogica.

## Ubicacion curricular

Py271 pertenece a la serie py2xx, enfocada en backend, pruebas, despliegue, CI/CD y operacion de software.

En este curso, IaC es parte central del flujo de entrega y no un complemento opcional.

La base tematica de GitHub Actions esta reorganizada con la estructura editorial de Pythonista y ampliada para aterrizarla a un curso de CI/CD seguro dentro de py2xx.

## Estructura sugerida

1. Marco conceptual: DevSecOps, workflows de repositorio y entornos.
2. Fundamentos de GitHub Actions y workflows.
3. Matriz, calidad tecnica y pruebas en pipeline.
4. Seguridad de cadena de suministro y contenedores.
5. Provision con Terraform en GCP e identidad federada con OIDC.
6. Despliegue en Linux y operacion segura.
7. Proyecto final integrador.

## Bloque tematico central

El tramo central del curso avanza por estos conceptos:

- marco operativo de DevSecOps y entornos;
- diseno y sintaxis de workflows en GitHub Actions;
- matriz de versiones y promocion por entornos;
- quality gates con linters, tipado y pruebas automatizadas;
- seguridad de cadena de suministro: SBOM, provenance, attestations y escaneo;
- build de contenedores con criterio de runners hosted y self-hosted endurecidos;
- provision de infraestructura con Terraform en GCP;
- identidad federada con OIDC y Workload Identity Federation (requiere Terraform).

## Criterio operativo de plataforma

- GitHub Actions se mantiene como plano de control principal del pipeline.
- Los hosted runners son la opcion por defecto.
- Los self-hosted runners se usan solo cuando hay necesidad tecnica justificada (red privada, segmentacion o cumplimiento).
- Cloud Build se presenta como alternativa avanzada, no como ruta principal.

## Modelo de entornos del curso

Para imparticion y practicas, el curso usa este modelo:

- dev: maquina del desarrollador con SQLite para iteracion local.
- test: servidor Linux hosteado con PostgreSQL para despliegue remoto y validacion operativa.
- prod: GCP con Cloud SQL para PostgreSQL y despliegue en Cloud Run v2.

La recomendacion didactica es promover el mismo artefacto entre entornos y variar solo configuracion, identidad y controles de aprobacion.

## Empaque recomendado

- Modalidad: taller de 16 horas.
- Cadencia recomendada: 8 sesiones de 2 horas.
- Distribucion sugerida: 30 a 40 minutos de marco conceptual, 35 a 45 minutos de demo guiada y 35 a 45 minutos de practica por sesion.
- Sesion de mayor carga tecnica: 5, 6 y 7; conviene llegar con repositorios y credenciales preparados.

## Resultados de aprendizaje

- Disenar workflows mantenibles en GitHub Actions.
- Aplicar quality gates con herramientas de lint, tipado y pruebas.
- Construir y validar imagenes de contenedor en CI.
- Aplicar criterio tecnico para decidir entre runners hosted y self-hosted.
- Integrar controles de seguridad en la cadena de suministro.
- Provisionar infraestructura con Terraform para despliegue continuo en Google Cloud Run v2 y Linux.
- Ejecutar despliegues con criterios de seguridad, observabilidad y rollback.

## Repositorios auxiliares sugeridos

- apps/api-github-actions-demo
- infra/terraform-py271

## Checklist previa a clase

- Verificar que la notebook de la sesion abre y ejecuta celdas clave.
- Confirmar acceso a kernel de Python y Jupyter.
- Validar que las demos o submodulos requeridos estan disponibles.
- Revisar credenciales, entornos o variables ficticias usadas en ejemplos.

## Checklist de cierre de bloque

- Confirmar cobertura de objetivos del bloque.
- Registrar fallas frecuentes en pipelines o despliegues.
- Actualizar material de refuerzo y ejercicios resueltos.
- Verificar si hay cambios necesarios en submodulos de app o infraestructura.

## Recomendaciones didacticas

- Separar claramente conceptos de CI, CD, seguridad e IaC.
- Evitar acoplar demasiado pronto ejemplos a una sola plataforma concreta.
- Explicar que Kubernetes no es la ruta base del curso: aunque usa contenedores, su valor principal aparece en arquitecturas de microservicios y el caso de estudio actual no requiere ese nivel de orquestacion.
- Mostrar fallas reales de pipeline, no solo ejecuciones exitosas.
- Tratar IaC como parte del sistema de entrega, no como apendice teorico.