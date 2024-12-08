from datetime import datetime
from typing import List, Optional

class Transaction:
    """
    Classe para representar transações financeiras.
    
    Atributos:
        amount (float): Valor da transação;
        date (datetime): Data da transação;
        category (str): Identificador de uma categoria;
        description (str): Descrição da transação.
    """

    def __init__(self, amount: float, category: str, description: str = ""):
        """
        Inicializa um objeto Transaction.
        
        Args:
            amount (float): Valor da transação;
            category (str): Identificador de uma categoria;
            description (str): Descrição da transação.
        """
        self.amount = amount
        self.date = datetime.now()
        self.category = category
        self.description = description
    
    def __str__(self):
        """
        Retorna uma descrição da transação.
        
        Returns:
            str: Descrição da transação.
        """
        return f"Transação: {self.description} R$ {self.amount:0.2f} ({self.category})"
    
    def update(self, **attributes):
        """
        Atualiza um ou mais atributos da transação.
        
        Args:
            **attributes: Atributos a serem atualizados.
        """
        for key, value in attributes.items():
            if hasattr(self, key):
                setattr(self, key, value)

class Account:
    """
    Classe para representar contas e armazenar transações.
    
    Atributos:
        name (str): Nome da conta;
        balance (float): Saldo da conta;
        transactions (List[Transaction]): Lista de transações na conta.
    """

    def __init__(self, name: str):
        """
        Inicializa um objeto Account.
        
        Args:
            name (str): Nome da conta.
        """
        self.name = name
        self.balance = 0.0
        self.transactions = []

    def add_transaction(self, amount: float, category: str, description: str = "") -> Transaction:
        """
        Cria uma transação na conta e atualiza o saldo da conta.
        
        Args:
            amount (float): Valor da transação;
            category (str): Identificador de uma categoria;
            description (str): Descrição da transação.
        
        Returns:
            Transaction: A transação criada.
        """
        transaction = Transaction(amount, category, description)
        self.transactions.append(transaction)
        self.balance += amount
        return transaction

    def get_transactions(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, category: Optional[str] = None) -> List[Transaction]:
        """
        Gera uma lista de transações.
        
        Args:
            start_date (Optional[datetime]): Data inicial para filtrar transações;
            end_date (Optional[datetime]): Data final para filtrar transações;
            category (Optional[str]): Categoria para filtrar transações.
        
        Returns:
            List[Transaction]: Lista de transações filtradas.
        """
        filtered_transactions = [t for t in self.transactions if (start_date is None or t.date >= start_date) and (end_date is None or t.date <= end_date) and (category is None or t.category == category)]
        return filtered_transactions

class Investment:
    """
    Classe para representar investimentos.
    
    Atributos:
        type (str): Identificador de um tipo de investimento;
        initial_amount (float): Valor inicial do investimento;
        date_purchased (datetime): Data da compra do investimento;
        rate_of_return (float): Taxa mensal de retorno.
    """

    def __init__(self, type: str, initial_amount: float, rate_of_return: float, date_purchased: datetime):
        """
        Inicializa um objeto Investment.
        
        Args:
            type (str): Identificador de um tipo de investimento;
            initial_amount (float): Valor inicial do investimento;
            rate_of_return (float): Taxa mensal de retorno;
            date_purchased (datetime): Data da compra do investimento.
        """
        self.type = type
        self.initial_amount = initial_amount
        self.rate_of_return = rate_of_return
        self.date_purchased = date_purchased

    def calculate_value(self, current_date: datetime) -> float:
        """
        Calcula o valor atual do investimento.
        
        Args:
            current_date (datetime): Data atual para cálculo do valor.
        
        Returns:
            float: Valor atual do investimento.
        """
        months_passed = (current_date.year - self.date_purchased.year) * 12 + current_date.month - self.date_purchased.month
        return self.initial_amount * ((1 + self.rate_of_return) ** months_passed)

    def sell(self, account: Account):
        """
        Vende o investimento e deposita o valor em uma conta.
        
        Args:
            account (Account): Conta para depositar o valor.
        
        Returns:
            float: Valor atual do investimento vendido.
        """
        current_value = self.calculate_value(datetime.now())
        account.add_transaction(current_value, "Venda de Investimento", f"Vendeu investimento {self.type}")
        return current_value

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
