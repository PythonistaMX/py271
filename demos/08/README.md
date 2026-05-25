# Demo 08: Ejercicio de pytest desde CLI

Este ejercicio muestra una calculadora simple y su suite de pruebas con `pytest`.

## Estructura

- `calculadora.py`: funciones a probar.
- `tests/test_calculadora.py`: pruebas unitarias con `parametrize` y manejo de excepciones.

## Ejecutar desde CLI

```bash
cd demos/08
python -m pytest -q
```

## Reto

1. Agrega una función `potencia(a, b)` en `calculadora.py`.
2. Crea pruebas para exponentes positivos y negativos.
3. Vuelve a ejecutar `pytest -q`.
