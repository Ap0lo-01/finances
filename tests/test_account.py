import pytest
from modulo_finances.account import Account

def test_account_initialization():
    """
    Testa a inicialização de um objeto Account.
    
    Verifica se o nome da conta é atribuído corretamente,
    o saldo inicial é zero e a lista de transações é criada.
    """
    account = Account("Main Account")
    assert account.name == "Main Account"
    assert account.balance == 0.0
    assert isinstance(account.transactions, list)

def test_add_transaction():
    """
    Testa a adição de uma transação a uma conta.
    
    Verifica se a transação é criada corretamente e
    se o saldo da conta é atualizado.
    """
    account = Account("Main Account")
    transaction = account.add_transaction(100.0, "Food", "Grocery shopping")
    assert transaction.amount == 100.0
    assert transaction.category == "Food"
    assert transaction.description == "Grocery shopping"
    assert account.balance == 100.0

def test_get_transactions():
    """
    Testa a obtenção de transações filtradas por categoria.
    
    Verifica se a função retorna as transações da categoria correta.
    """
    account = Account("Main Account")
    transaction1 = account.add_transaction(100.0, "Food", "Grocery shopping")
    transaction2 = account.add_transaction(50.0, "Transport", "Bus fare")
    transactions = account.get_transactions(category="Food")
    assert len(transactions) == 1
    assert transactions[0].category == "Food"
