# Apps del curso

Esta carpeta se reserva para aplicaciones auxiliares versionadas como submódulos Git.

## Sugerencia inicial

- api-github-actions-demo: aplicación base para prácticas de pipeline, contenedores y despliegue.

## Ejemplo de alta de submódulo

```bash
git submodule add https://github.com/PythonistaMX/api-github-actions-demo.git apps/api-github-actions-demo
git submodule update --init --recursive
```