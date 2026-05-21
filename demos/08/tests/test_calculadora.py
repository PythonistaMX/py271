import pytest

from calculadora import dividir
from calculadora import multiplicar
from calculadora import restar
from calculadora import sumar


@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0.5, 0.5, 1.0),
    ],
)
def test_sumar(a, b, esperado):
    assert sumar(a, b) == esperado


def test_restar():
    assert restar(10, 4) == 6


def test_multiplicar():
    assert multiplicar(6, 7) == 42


def test_dividir():
    assert dividir(9, 3) == 3


def test_dividir_entre_cero_lanza_error():
    with pytest.raises(ValueError, match="cero"):
        dividir(1, 0)
