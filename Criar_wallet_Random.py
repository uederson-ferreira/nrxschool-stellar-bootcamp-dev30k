from stellar_sdk import Keypair, Server

# Gerar um novo par de chaves (chave pública e privada)
keypair = Keypair.random()
public_key = keypair.public_key
secret_key = keypair.secret

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
