import pytest
from datetime import datetime
from finances import Transaction

def test_transaction_initialization():
    """
    Testa a inicialização de um objeto Transaction.
    """
    transacao = Transaction(100.0, "Alimentação", "Compras no supermercado")
    assert transacao.amount == 100.0
    assert transacao.category == "Alimentação"
    assert transacao.description == "Compras no supermercado"
    assert isinstance(transacao.date, datetime)

def test_transaction_str():
    """
    Testa a representação em string de um objeto Transaction.
    """
    transacao = Transaction(100.0, "Alimentação", "Compras no supermercado")
    assert str(transacao) == "Transação: Compras no supermercado R$ 100.00 (Alimentação)"

def test_transaction_update():
    """
    Testa a atualização dos atributos de um objeto Transaction.
    """
    transacao = Transaction(100.0, "Alimentação", "Compras no supermercado")
    transacao.update(amount=150.0, category="Restaurante")
    assert transacao.amount == 150.0
    assert transacao.category == "Restaurante"
