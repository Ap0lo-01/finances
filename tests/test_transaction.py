import pytest
from datetime import datetime
from modulo_finances.transaction import Transaction

def test_transaction_initialization():
    """
    Testa a inicialização de um objeto Transaction.
    
    Verifica se os atributos são corretamente atribuídos
    e se a data da transação é do tipo datetime.
    """
    transaction = Transaction(100.0, "Food", "Grocery shopping")
    assert transaction.amount == 100.0
    assert transaction.category == "Food"
    assert transaction.description == "Grocery shopping"
    assert isinstance(transaction.date, datetime)

def test_transaction_str():
    """
    Testa a representação em string de um objeto Transaction.
    
    Verifica se a string retornada está no formato correto.
    """
    transaction = Transaction(100.0, "Food", "Grocery shopping")
    assert str(transaction) == "Transação: Grocery shopping R$ 100.00 (Food)"

def test_transaction_update():
    """
    Testa a atualização de atributos de um objeto Transaction.
    
    Verifica se os atributos são atualizados corretamente.
    """
    transaction = Transaction(100.0, "Food", "Grocery shopping")
    transaction.update(amount=150.0, category="Dining")
    assert transaction.amount == 150.0
    assert transaction.category == "Dining"
