from stellar_sdk import Keypair, Network, Server, TransactionBuilder
import base64
import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Configurações de chaves
public_key = os.getenv("PUBLIC_KEY_1")  # Chave pública da Testnet no arquivo .env
secret_key = os.getenv("SECRET_KEY_1")  # Chave privada da Testnet no arquivo .env

# Conectar-se ao servidor da Stellar Testnet
server = Server("https://horizon-testnet.stellar.org")

# Configura o servidor da Stellar Mainnet
#server = Server("https://horizon.stellar.org")

# 1. Converter o texto "DEV30K" em bytes e codificar em Base64
mensagem = "DEV30K".encode()                # Texto em bytes
mensagem_b64 = base64.b64encode(mensagem)    # Codificar em Base64
print(f"📧 Mensagem em Base64: {mensagem_b64.decode()}")

# 2. Assinar a mensagem codificada em Base64
chave = Keypair.from_secret(secret_key)
assinatura = chave.sign(mensagem_b64)  # Assinatura da mensagem Base64 em bytes

# Exibir a assinatura para verificação
print(f"📝 Assinatura (hex): {assinatura.hex()}")
print(f"Tamanho da assinatura em bytes: {len(assinatura)} bytes")

# Verifique se a assinatura em bytes cabe dentro do limite de 64 bytes
if len(assinatura) > 64:
    raise ValueError("A assinatura em bytes excede o limite de 64 bytes.")

# 3. Configurar e criar a transação com `manage_data_op` armazenando a assinatura em bytes
try:
    conta = server.load_account(public_key)
    transacao = (
        TransactionBuilder(
            source_account=conta,
            network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
            base_fee=100
        )
        .add_text_memo("DEV30K")
        .append_manage_data_op(
            data_name="desafio",
            data_value=assinatura  # Armazena a assinatura diretamente em bytes
        )
        .build()
    )

    # Assinar e enviar a transação
    transacao.sign(chave)
    response = server.submit_transaction(transacao)

    # 4. Obter o hash da transação para o critério de aceite
    transaction_hash = response["hash"]
    
    # Saída formatada
    print("\n🔐 Conta da Transação:", public_key)
    print(f"🔗 Hash da Transação:  {transaction_hash}")
    print(f"📧 Mensagem em Base64: {mensagem_b64.decode()}")
    print(f"📝 Assinatura (hex): {assinatura.hex()}")
    print("✅ A assinatura é válida. A mensagem foi assinada pela chave pública fornecida.")
    print("🌐 Link da Transação:", response["_links"]["transaction"]["href"])

except Exception as e:
    print("🚨 Erro ao enviar a transação:", e)
