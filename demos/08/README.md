# Demo 08: Linters, tipado y pytest desde CLI

Este ejercicio cubre los tres quality gates que corren en el pipeline antes de llegar a producción: análisis estático con `ruff`, verificación de tipos con `mypy` y pruebas unitarias con `pytest`.

## Estructura

- `calculadora.py`: funciones con anotaciones de tipo.
- `tests/conftest.py`: configuración de ruta para que pytest resuelva importaciones.
- `tests/test_calculadora.py`: pruebas unitarias con `parametrize` y manejo de excepciones.

## Ejecutar desde CLI

Instala las herramientas si no las tienes:

```bash
pip install ruff mypy pytest
```

Corre cada gate por separado desde `demos/08`:

```bash
# Linter
ruff check .

# Tipado estático
mypy calculadora.py

# Pruebas
python -m pytest -q
```

Los tres comandos deben terminar sin errores antes de considerar el código listo para el pipeline.

## Reto

1. Agrega una función `potencia(a, b: int) -> float` en `calculadora.py`.
2. Escribe pruebas para exponentes positivos, cero y negativos.
3. Introduce intencionalmente un error de tipo (por ejemplo, `return str(resultado)`) y observa qué reporta `mypy`.
4. Vuelve a pasar los tres gates hasta que todos estén en verde.
