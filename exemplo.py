from modulo_finances.client import Client
from datetime import datetime

# Cria um cliente
cliente = Client("João Silva")

# Adiciona uma conta ao cliente
conta = cliente.add_account("Conta Principal")

# Adiciona transações à conta
transacao1 = conta.add_transaction(1000.0, "Renda", "Salário")
transacao2 = conta.add_transaction(-200.0, "Alimentação", "Jantar no restaurante")
transacao3 = conta.add_transaction(-150.0, "Transporte", "Manutenção do carro")

# Exibe as transações
print(transacao1)
print(transacao2)
print(transacao3)

# Adiciona um investimento ao cliente
data_compra = datetime(2023, 12, 8)  # Data fictícia de compra
investimento = Investment("Ações", 5000.0, 0.05, data_compra)
cliente.add_investment(investimento)

# Gera e exibe um relatório financeiro do cliente
relatorio = cliente.generate_report()
print(relatorio)

# Gera e exibe um relatório de projeção de rendimentos futuros do cliente
data_futura = datetime(2025, 12, 31)
relatorio_futuro = cliente.future_value_report(data_futura)
print(relatorio_futuro)
