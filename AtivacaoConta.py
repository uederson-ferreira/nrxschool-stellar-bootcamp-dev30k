from stellar_sdk import Keypair, Network, Server, TransactionBuilder, Asset
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
source_public_key = public_key_1  # Substitua pela sua chave pública da conta de origem
source_secret_key = secret_key_1  # Substitua pela sua chave privada da conta de origem

# Chave pública da conta de destino (a que receberá 1 XLM)
destination_public_key = public_key_2

# Conectar-se ao servidor da Stellar Mainnet
server = Server("https://horizon.stellar.org")

# Carregar a conta de origem
source_keypair = Keypair.from_secret(source_secret_key)
source_account = server.load_account(source_public_key)

# Criar a transação de pagamento para ativar a conta de destino
transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.PUBLIC_NETWORK_PASSPHRASE,
        base_fee=100
    )
    .append_create_account_op(
        destination=destination_public_key,  # Conta de destino
        starting_balance="1"  # Quantidade de XLM para ativar a conta (mínimo 1 XLM)
    )
    .set_timeout(30)
    .build()
)

# Assinar a transação com a chave privada da conta de origem
transaction.sign(source_keypair)

# Enviar a transação para a rede Stellar Mainnet
try:
    response = server.submit_transaction(transaction)
    print("Transação enviada com sucesso! Conta de destino ativada.")
    print("Hash da Transação:", response["hash"])
    print("Link da Transação:", response["_links"]["transaction"]["href"])
except Exception as e:
    print("Erro ao enviar a transação:", e)
