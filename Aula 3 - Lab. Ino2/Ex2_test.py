import pytest
from Ex2 import ListaDeCompras

@pytest.fixture
def lista_vazia():
    return ListaDeCompras()

def test_adicionar_item(lista_vazia):
    lista_vazia.adicionar_item('Arroz', 8.50)
    assert 'Arroz' in lista_vazia.itens
    assert lista_vazia.itens['Arroz'] == 8.50

def test_remover_item(lista_vazia):
    lista_vazia.adicionar_item('Feijão', 6.50)
    lista_vazia.remover_item('Feijão')
    assert 'Feijão' not in lista_vazia.itens

def test_mostrar_itens(lista_vazia, capsys):
    lista_vazia.adicionar_item('Macarrão', 3.99)
    lista_vazia.mostrar_itens()
    capturado = capsys.readouterr()
    assert 'Macarrão: R$1.99' in capturado.out

def test_calcular_total(lista_vazia):
    lista_vazia.adicionar_item('Café', 15.00)
    lista_vazia.adicionar_item('Açúcar', 5.00)
    assert lista_vazia.calcular_total() == 20.00
