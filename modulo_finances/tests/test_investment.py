import pytest
from datetime import datetime, timedelta
from finances import Investment, Account

def test_investment_initialization():
    """
    Testa a inicialização de um objeto Investment.
    """
    investimento = Investment("Ações", 1000.0, 0.05, datetime.now())
    assert investimento.type == "Ações"
    assert investimento.initial_amount == 1000.0
    assert investimento.rate_of_return == 0.05
    assert isinstance(investimento.date_purchased, datetime)

def test_calculate_value():
    """
    Testa o cálculo do valor atual de um investimento.
    """
    data_compra = datetime.now() - timedelta(days=365)
    investimento = Investment("Ações", 1000.0, 0.05, data_compra)
    valor_atual = investimento.calculate_value(datetime.now())
    valor_esperado = 1000.0 * ((1 + 0.05) ** 12)  # 12 meses se passaram
    assert valor_atual == pytest.approx(valor_esperado, 0.01)

def test_sell_investment():
    """
    Testa a venda de um investimento e o depósito do valor em uma conta.
    """
    conta = Account("Conta Principal")
    data_compra = datetime.now() - timedelta(days=365)
    investimento = Investment("Ações", 1000.0, 0.05, data_compra)
    valor_atual = investimento.sell(conta)
    valor_esperado = 1000.0 * ((1 + 0.05) ** 12)  # 12 meses se passaram
    assert valor_atual == pytest.approx(valor_esperado, 0.01)
    assert conta.balance == pytest.approx(valor_esperado, 0.01)
