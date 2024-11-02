
from stellar_sdk import Server
import os
from dotenv import load_dotenv


# Carregar as variáveis do arquivo .env
load_dotenv()

# Obter as chaves do .env
public_key_1 = os.getenv("PUBLIC_KEY_1")
secret_key_1 = os.getenv("SECRET_KEY_1")
public_key_2 = os.getenv("PUBLIC_KEY_2")
secret_key_2 = os.getenv("SECRET_KEY_2")

# Configurar o servidor da Stellar Testnet
server = Server("https://horizon-testnet.stellar.org")

# Função para consultar saldo de uma conta
def consultar_saldo(chave_publica):
    conta = server.accounts().account_id(chave_publica).call()
    print(f"Saldos para a conta {chave_publica}:")
    for saldo in conta['balances']:
        print(f"Tipo de ativo: {saldo['asset_type']}, Saldo: {saldo['balance']}")

# Consultar saldo das duas carteiras
consultar_saldo(public_key_1)
consultar_saldo(public_key_2)
