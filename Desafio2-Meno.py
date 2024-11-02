from stellar_sdk import Keypair, Network, Server, TransactionBuilder
import base64
import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Obter as chaves do .env
public_key_1 = os.getenv("PUBLIC_KEY_1")
secret_key_1 = os.getenv("SECRET_KEY_1")
public_key_2 = os.getenv("PUBLIC_KEY_2")
secret_key_2 = os.getenv("SECRET_KEY_2")

# Configurações de chaves
public_key = public_key_1  # Substitua com sua chave pública da Mainnet
secret_key = secret_key_1  # Substitua com sua chave privada da Mainnet

# Conectar-se ao servidor da Stellar Mainnet
server = Server("https://horizon.stellar.org")

# Assinar o texto "DEV30K"
chave = Keypair.from_secret(secret_key)
texto = "DEV30K".encode()
assinatura_binaria = chave.sign(texto)
assinatura_base64 = base64.b64encode(assinatura_binaria).decode()
print("Assinatura Base64 completa:", assinatura_base64)

# Dividir a assinatura Base64 em duas partes
parte1 = assinatura_base64[:32]  # Primeiros 32 caracteres
parte2 = assinatura_base64[32:]   # Restantes

try:
    conta = server.load_account(public_key)
    transacao = (
        TransactionBuilder(
            source_account=conta,
            network_passphrase=Network.PUBLIC_NETWORK_PASSPHRASE,
            base_fee=100
        )
        .add_text_memo("DEV30K")
        .append_manage_data_op(
            data_name="desafio_parte1",
            data_value=parte1  # Primeira metade da assinatura
        )
        .append_manage_data_op(
            data_name="desafio_parte2",
            data_value=parte2  # Segunda metade da assinatura
        )
        .build()
    )

    # Assinar e enviar a transação
    transacao.sign(chave)
    response = server.submit_transaction(transacao)

    # Hash da transação para submissão
    transaction_hash = response["hash"]
    print("Transação enviada com sucesso!")
    print("Hash da Transação:", transaction_hash)
    print("Link da Transação:", response["_links"]["transaction"]["href"])

except Exception as e:
    print("Erro ao enviar a transação:", e)
