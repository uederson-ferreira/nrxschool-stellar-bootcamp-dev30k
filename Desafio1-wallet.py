from stellar_sdk import Keypair, Server
import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Obter as chaves do .env
public_key_1 = os.getenv("PUBLIC_KEY_1")
secret_key_1 = os.getenv("SECRET_KEY_1")
public_key_2 = os.getenv("PUBLIC_KEY_2")
secret_key_2 = os.getenv("SECRET_KEY_2")

public_key = public_key_1  # Chave pública da segunda carteira
secret_key = secret_key_1  # Chave privada da segunda carteira

print("Chave Pública:", public_key)
print("Chave Privada:", secret_key)

# Conectar ao servidor da Testnet
server = Server("https://horizon-testnet.stellar.org")

# Financiar a conta usando o Friendbot
import requests
response = requests.get(f"https://friendbot.stellar.org/?addr={public_key}")

if response.status_code == 200:
    print("Conta financiada com sucesso na Testnet!")
else:
    print("Erro ao financiar a conta:", response.text)
    
account = server.accounts().account_id(public_key).call()
balances = account['balances']
for balance in balances:
    print(f"Tipo de Ativo: {balance['asset_type']}, Saldo: {balance['balance']}")
