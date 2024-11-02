from stellar_sdk import Server
import requests
import os
from dotenv import load_dotenv


# Carregar as variáveis do arquivo .env
load_dotenv()

# Obter as chaves do .env
public_key_1 = os.getenv("PUBLIC_KEY_1")
secret_key_1 = os.getenv("SECRET_KEY_1")
public_key_2 = os.getenv("PUBLIC_KEY_2")
secret_key_2 = os.getenv("SECRET_KEY_2")

# Configura o servidor da Stellar Testnet
server = Server("https://horizon-testnet.stellar.org")

# Função para consultar saldo da conta
def consultar_saldo(chave_publica):
    try:
        conta = server.accounts().account_id(chave_publica).call()
        print(f"Saldos para a conta {chave_publica}:")
        for saldo in conta['balances']:
            print(f"Tipo de ativo: {saldo['asset_type']}, Saldo: {saldo['balance']}")
    except Exception as e:
        print(f"Erro ao consultar saldo para a conta {chave_publica}: {e}")

# Função opcional para financiar a conta na Testnet (caso necessário)
def financiar_conta(chave_publica):
    response = requests.get(f"https://friendbot.stellar.org/?addr={chave_publica}")
    if response.status_code == 200:
        print(f"Conta {chave_publica} financiada com sucesso!")
    else:
        print(f"Erro ao financiar a conta {chave_publica}: {response.text}")

# Financiar e consultar saldo de ambas as contas
# Se uma ou ambas as contas estiverem sem saldo, descomente as linhas abaixo para financiar:
# financiar_conta(public_key_1)
# financiar_conta(public_key_2)

# Consultar saldo das duas contas
consultar_saldo(public_key_1)
consultar_saldo(public_key_2)
