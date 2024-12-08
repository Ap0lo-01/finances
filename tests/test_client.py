import pytest
from modulo_finances.client import Client
from modulo_finances.account import Account
from modulo_finances.investment import Investment
from datetime import datetime, timedelta

def test_client_initialization():
    """
    Testa a inicialização de um objeto Client.
    
    Verifica se o nome do cliente é atribuído corretamente e
    se as listas de contas e investimentos são criadas.
    """
    client = Client("John Doe")
    assert client.name == "John Doe"
    assert isinstance(client.accounts, list)
    assert isinstance(client.investments, list)

def test_add_account():
    """
    Testa a adição de uma conta a um cliente.
    
    Verifica se a conta é criada e adicionada à lista de contas do cliente.
    """
    client = Client("John Doe")
    account = client.add_account("Main Account")
    assert account.name == "Main Account"
    assert account in client.accounts

def test_add_investment():
    """
    Testa a adição de um investimento a um cliente.
    
    Verifica se o investimento é adicionado à lista de investimentos do cliente.
    """
    client = Client("John Doe")
    investment = Investment("Stock", 1000.0, 0.05, datetime.now())
    client.add_investment(investment)
    assert investment in client.investments

def test_get_net_worth():
    """
    Testa o cálculo do patrimônio líquido de um cliente.
    
    Verifica se a soma dos saldos das contas e o valor dos investimentos
    resulta no valor correto.
    """
    client = Client("John Doe")
    account = client.add_account("Main Account")
    account.add_transaction(1000.0, "Income", "Salary")
    date_purchased = datetime.now() - timedelta(days=365)
    investment = Investment("Stock", 1000.0, 0.05, date_purchased)
    client.add_investment(investment)
    net_worth = client.get_net_worth()
    expected_value = 1000.0 + 1000.0 * ((1 + 0.05) ** 12)  # Saldo + 12 meses de crescimento do investimento
    assert net_worth == pytest.approx(expected_value, 0.01)
