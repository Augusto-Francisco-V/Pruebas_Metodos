import pytest
from main import validar_longitud

def test_Primera_Desicion():
    print("Desicion 1")
    assert validar_longitud("Python") == True

def test_Segunda_Desicion():
    print("Desicion 2")
    assert validar_longitud("ABCDEFGHI") == True

def test_Tercera_Desicion():
    print("Desicion 3")
    assert validar_longitud("") == True