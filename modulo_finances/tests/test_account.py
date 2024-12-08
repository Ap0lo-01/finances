import pytest
from finances import Account

def test_account_initialization():
    """
    Testa a inicialização de um objeto Account.
    """
    conta = Account("Conta Principal")
    assert conta.name == "Conta Principal"
    assert conta.balance == 0.0
    assert isinstance(conta.transactions, list)

def test_add_transaction():
    """
    Testa a adição de uma transação em uma conta.
    """
    conta = Account("Conta Principal")
    transacao = conta.add_transaction(100.0, "Alimentação", "Compras no supermercado")
    assert transacao.amount == 100.0
    assert transacao.category == "Alimentação"
    assert transacao.description == "Compras no supermercado"
    assert conta.balance == 100.0

def test_get_transactions():
    """
    Testa a filtragem de transações por categoria.
    """
    conta = Account("Conta Principal")
    transacao1 = conta.add_transaction(100.0, "Alimentação", "Compras no supermercado")
    transacao2 = conta.add_transaction(50.0, "Transporte", "Tarifa de ônibus")
    transacoes = conta.get_transactions(category="Alimentação")
    assert len(transacoes) == 1
    assert transacoes[0].category == "Alimentação"
