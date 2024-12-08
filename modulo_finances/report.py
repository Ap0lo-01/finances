from .client import Client
from datetime import datetime

def generate_report(client: Client) -> str:
    """
    Gera um relatório financeiro para um cliente.
    
    Args:
        client (Client): Cliente para o qual o relatório será gerado.
    
    Returns:
        str: Relatório financeiro do cliente.
    """
    report = f"Relatório Financeiro para {client.name}\n"
    report += "Contas:\n"
    for account in client.accounts:
        report += f"  - {account.name}: R$ {account.balance:0.2f}\n"
    report += "Investimentos:\n"
    for investment in client.investments:
        current_value = investment.calculate_value(datetime.now())
        report += f"  - {investment.type}: R$ {current_value:0.2f}\n"
    return report

def future_value_report(client: Client, date: datetime) -> str:
    """
    Gera um relatório de projeção de rendimentos futuros para um cliente.
    
    Args:
        client (Client): Cliente para o qual a projeção será gerada;
        date (datetime): Data futura para a projeção.
    
    Returns:
        str: Relatório de projeção de rendimentos futuros.
    """
    report = f"Projeção de Rendimentos Futuros para {client.name} até {date}\n"
    report += "Contas:\n"
    for account in client.accounts:
        report += f"  - {account.name}: R$ {account.balance:0.2f}\n"
    report += "Investimentos:\n"
    for investment in client.investments:
        future_value = investment.calculate_value(date)
        report += f"  - {investment.type}: R$ {
