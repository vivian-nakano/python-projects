import pytest
from matematica import operacao_soma, operacao_multiplicacao, operacao_divisao, operacao_subtracao

def test_soma():
    assert operacao_soma(2,1) == 3

def test_multiplicacao():
    assert operacao_multiplicacao(4,8) == 32

def test_divisao():
    assert operacao_divisao(8,2) == 4

def test_subtracao():
    assert operacao_subtracao(10,9) == 1

