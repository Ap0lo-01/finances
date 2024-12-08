from datetime import datetime

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

    def sell(self, account):
        """
        Vende o investimento e deposita o valor em uma conta.
        
        Args:
            account (Account): Conta para depositar o valor.
        
        Returns:
            float: Valor atual do investimento vendido.
        """
        current_value = self.calculate_value(datetime.now())
        account.add_transaction(current_value, "Investment Sale", f"Sold {self.type} investment")
        return current_value
