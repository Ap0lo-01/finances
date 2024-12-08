from typing import List, Optional
from .transaction import Transaction
from datetime import datetime

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
