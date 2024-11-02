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

# Conectar-se ao servidor da Stellar Mainnet
server = Server("https://horizon.stellar.org")

# Função para consultar transações
def consultar_transacoes(chave_publica):
    try:
        transacoes = server.transactions().for_account(chave_publica).call()
        print(f"\nTransações para a conta {chave_publica}:")

        # Verifica se há transações
        if '_embedded' in transacoes and 'records' in transacoes['_embedded']:
            if transacoes['_embedded']['records']:
                for tx in transacoes['_embedded']['records']:
                    print(f"ID da transação: {tx['id']}, Tipo: {tx.get('type', 'Desconhecido')}, Data: {tx['created_at']}")
            else:
                print("Nenhuma transação encontrada para esta conta.")
        else:
            print("Nenhum dado de transação encontrado na resposta.")

    except Exception as e:
        # Imprime uma mensagem de erro detalhada
        print(f"Erro ao consultar transações para a conta {chave_publica}: {e}")

# Consultar transações para ambas as carteiras
consultar_transacoes(public_key_1)
consultar_transacoes(public_key_2)
