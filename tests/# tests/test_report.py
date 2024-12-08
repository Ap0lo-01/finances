import pytest
from datetime import datetime, timedelta
from modulo_finances.client import Client
from modulo_finances.account import Account
from modulo_finances.investment import Investment
from modulo_finances.report import generate_report, future_value_report

def test_generate_report():
    """
    Testa a geração de um relatório financeiro para um cliente.
    
    Verifica se o relatório contém informações das contas e investimentos do cliente.
    """
    client = Client("John Doe")
    account = client.add_account("Main Account")
    account.add_transaction(1000.0, "Income", "Salary")
    date_purchased = datetime.now() - timedelta(days=365)
    investment = Investment("Stock", 1000.0, 0.05, date_purchased)
    client.add_investment(investment)
    report = generate_report(client)
    assert "Relatório Financeiro para John Doe" in report
    assert "Main Account: R$ 1000.00" in report
    assert "Stock: R$" in report

def test_future_value_report():
    """
    Testa a geração de um relatório de projeção de rendimentos futuros para um cliente.
    
    Verifica se o relatório contém projeções das contas e investimentos do cliente para a data futura especificada.
    """
    client = Client("John Doe")
    account = client.add_account("Main Account")
    account.add_transaction(1000.0, "Income", "Salary")
    date_purchased = datetime.now() - timedelta(days=365)
    investment = Investment("Stock", 1000.0, 0.05, date_purchased)
    client.add_investment(investment)
    future_date = datetime.now() + timedelta(days=365)
    report = future_value_report(client, future_date)
    assert "Projeção de Rendimentos Futuros para John
