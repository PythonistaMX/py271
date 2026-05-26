# Demo 06: Completar un workflow de GitHub Actions

Este archivo es la plantilla mínima que genera GitHub al crear un workflow nuevo desde la interfaz web. El ejercicio consiste en transformarla en un workflow funcional para un proyecto Python.

## Estructura

- `blank.yml`: plantilla de workflow con estructura básica y comentarios guía.

## Ejercicio en clase

1. Copia `blank.yml` a `.github/workflows/ci.yml` en tu repositorio de práctica.
2. Cambia el nombre del workflow (`name: CI`) por algo descriptivo.
3. Reemplaza el job `build` con los pasos de un pipeline Python mínimo:

```yaml
jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.13"

      - run: pip install ruff pytest

      - run: ruff check .

      - run: pytest -q
```

4. Haz un push o abre un pull request y observa la ejecución en la pestaña *Actions*.

## Reto

1. Añade un trigger `workflow_dispatch` para poder ejecutar el workflow manualmente.
2. Extrae la versión de Python a un `env` o `matrix` y prueba con dos versiones (3.12 y 3.13).
3. Nombra el job de forma que aparezca como status check requerido en la rama protegida.
