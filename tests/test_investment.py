import pytest
from datetime import datetime, timedelta
from modulo_finances.investment import Investment
from modulo_finances.account import Account

def test_investment_initialization():
    """
    Testa a inicialização de um objeto Investment.
    
    Verifica se os atributos são corretamente atribuídos.
    """
    investment = Investment("Stock", 1000.0, 0.05, datetime.now())
    assert investment.type == "Stock"
    assert investment.initial_amount == 1000.0
    assert investment.rate_of_return == 0.05
    assert isinstance(investment.date_purchased, datetime)

def test_calculate_value():
    """
    Testa o cálculo do valor atual de um investimento.
    
    Verifica se o valor é calculado corretamente com base na taxa de retorno mensal.
    """
    date_purchased = datetime.now() - timedelta(days=365)
    investment = Investment("Stock", 1000.0, 0.05, date_purchased)
    current_value = investment.calculate_value(datetime.now())
    expected_value = 1000.0 * ((1 + 0.05) ** 12)  # 12 meses se passaram
    assert current_value == pytest.approx(expected_value, 0.01)

def test_sell_investment():
    """
    Testa a venda de um investimento e o depósito do valor em uma conta.
    
    Verifica se o valor atual do investimento é adicionado ao saldo da conta.
    """
    account = Account("Main Account")
    date_purchased = datetime.now() - timedelta(days=365)
    investment = Investment("Stock", 1000.0, 0.05, date_purchased)
    current_value = investment.sell(account)
    expected_value = 1000.0 * ((1 + 0.05) ** 12)  # 12 meses se passaram
    assert current_value == pytest.approx(expected_value, 0.01)
    assert account.balance == pytest.approx(expected_value, 0.01)
