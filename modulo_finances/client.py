from typing import List
from .account import Account
from .investment import Investment
from datetime import datetime

class Client:
    """
    Classe para representar clientes.
    
    Atributos:
        name (str): Nome do cliente;
        accounts (List[Account]): Contas do cliente;
        investments (List[Investment]): Investimentos do cliente.
    """

    def __init__(self, name: str):
        """
        Inicializa um objeto Client.
        
        Args:
            name (str): Nome do cliente.
        """
        self.name = name
        self.accounts = []
        self.investments = []

    def add_account(self, account_name: str) -> Account:
        """
        Cria uma conta para o cliente.
        
        Args:
            account_name (str): Nome da conta.
        
        Returns:
            Account: A conta criada.
        """
        account = Account(account_name)
        self.accounts.append(account)
        return account

    def add_investment(self, investment: Investment):
        """
        Adiciona um investimento para o cliente.
        
        Args:
            investment (Investment): Investimento a ser adicionado.
        """
        self.investments.append(investment)

    def get_net_worth(self) -> float:
        """
        Calcula a soma do valor atual de todas as contas e investimentos do cliente.
        
        Returns:
            float: Patrimônio líquido do cliente.
        """
        total_balance = sum(account.balance for account in self.accounts)
        total_investments = sum(investment.calculate_value(datetime.now()) for investment in self.investments)
        return total_balance + total_investments

    def generate_report(self) -> str:
        """
        Gera um relatório financeiro para o cliente.
        
        Returns:
            str: Relatório financeiro do cliente.
        """
        report = f"Relatório Financeiro para {self.name}\n"
        report += "Contas:\n"
        for account in self.accounts:
            report += f"  - {account.name}: R$ {account.balance:0.2f}\n"
        report += "Investimentos:\n"
        for investment in self.investments:
            current_value = investment.calculate_value(datetime.now())
            report += f"  - {investment.type}: R$ {current_value:0.2f}\n"
        return report

    def future_value_report(self, date: datetime) -> str:
        """
        Gera um relatório de projeção de rendimentos futuros para o cliente.
        
        Args:
            date (datetime): Data futura para a projeção.
        
        Returns:
            str: Relatório de projeção de rendimentos futuros.
        """
        report = f"Projeção de Rendimentos Futuros para {self.name} até {date}\n"
        report += "Contas:\n"
        for account in self.accounts:
            report += f"  - {account.name}: R$ {account.balance:0.2f}\n"
        report += "Investimentos:\n"
        for investment in self.investments:
            future_value = investment.calculate_value(date)
            report += f"  - {investment.type}: R$ {future_value:0.2f}\n"
        return report
