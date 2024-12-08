from datetime import datetime

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
