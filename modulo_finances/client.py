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
