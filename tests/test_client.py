import pytest
from modulo_finances.client import Client
from modulo_finances.account import Account
from modulo_finances.investment import Investment
from datetime import datetime, timedelta

def test_client_initialization():
    """
    Testa a inicialização de um objeto Client.
    """
    cliente = Client("João Silva")
    assert cliente.name == "João Silva"
    assert isinstance(cliente.accounts, list)
    assert isinstance(cliente.investments, list)

def test_add_account():
    """
    Testa a adição de uma conta a um cliente.
    """
    cliente = Client("João Silva")
    conta = cliente.add_account("Conta Principal")
    assert conta.name == "Conta Principal"
    assert conta in cliente.accounts

def test_add_investment():
    """
    Testa a adição de um investimento a um cliente.
    """
    cliente = Client("João Silva")
    investimento = Investment("Ações", 1000.0, 0.05, datetime.now())
    cliente.add_investment(investimento)
    assert investimento in cliente.investments

def test_get_net_worth():
    """
    Testa o cálculo do patrimônio líquido de um cliente.
    """
    cliente = Client("João Silva")
    conta = cliente.add_account("Conta Principal")
    conta.add_transaction(1000.0, "Renda", "Salário")
    data_compra = datetime.now() - timedelta(days=365)
    investimento = Investment("Ações", 1000.0, 0.05, data_compra)
    cliente.add_investment(investimento)
    patrimonio_liquido = cliente.get_net_worth()
    valor_esperado = 1000.0 + 1000.0 * ((1 + 0.05) ** 12)  # Saldo + 12 meses de crescimento do investimento
    assert patrimonio_liquido == pytest.approx(valor_esperado, 0.01)

def test_generate_report():
    """
    Testa a geração de um relatório financeiro para um cliente.
    """
    cliente = Client("João Silva")
    conta = cliente.add_account("Conta Principal")
    conta.add_transaction(1000.0, "Renda", "Salário")
    data_compra = datetime.now() - timedelta(days=365)
    investimento = Investment("Ações", 1000.0, 0.05, data_compra)
    cliente.add_investment(investimento)
    relatorio = cliente.generate_report()
    assert "Relatório Financeiro para João Silva" in relatorio
    assert "Conta Principal: R$ 1000.00" in relatorio
    assert "Ações: R$" in relatorio

def test_future_value_report():
    """
    Testa a geração de um relatório de projeção de rendimentos futuros para um cliente.
    """
    cliente = Client("João Silva")
    conta = cliente.add_account("Conta Principal")
    conta.add_transaction(1000.0, "Renda", "Salário")
    data_compra = datetime.now() - timedelta(days=365)
    investimento = Investment("Ações", 1000.0, 0.05, data_compra)
    cliente.add_investment(investimento)
    data_futura = datetime.now() + timedelta(days=365)
    relatorio = cliente.future_value_report(data_futura)
    assert "Projeção de Rendimentos Futuros para João Silva até" in relatorio
    assert "Conta Principal: R$ 1000.00" in relatorio
    assert "Ações: R$" in relatorio
