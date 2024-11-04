from stellar_sdk.transaction_envelope import TransactionEnvelope
from stellar_sdk import Keypair, Network, Server, ManageData
from stellar_sdk.exceptions import BadSignatureError, NotFoundError
import base64
import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Configurações de chaves
public_key = os.getenv("PUBLIC_KEY_1")  # Chave pública da Testnet no arquivo .env
secret_key = os.getenv("SECRET_KEY_1")  # Chave privada da Testnet no arquivo .env

def read():
    # Configuração do servidor para Testnet
    server = Server("https://horizon-testnet.stellar.org")

    # Ler o hash da transação do arquivo
    try:
        with open("tx_hash.txt", "r") as f:
            lines = f.readlines()
            tx_hashes_and_public_keys = [line.strip().split() for line in lines]
    except FileNotFoundError as err:
        new_msg = "🚨 Arquivo 'tx_hash.txt' não encontrado. Execute o Script 1 primeiro."
        print(new_msg)
        raise FileNotFoundError(new_msg) from err

    # Processar cada transação do arquivo
    for tx_hash, public_key in tx_hashes_and_public_keys:
        print(f"\n🔐 Conta da Transação: {public_key}")
        print(f"🔗 Hash da Transação:  {tx_hash}")

        # Recuperar a transação pelo hash
        try:
            tx = server.transactions().transaction(tx_hash).call()
            print("✅ Transação encontrada.")
        except NotFoundError:
            print("🚫 Transação não encontrada na rede.")
            continue
        except Exception as e:
            print(f"🚨 Erro ao recuperar a transação: {e}")
            continue

        # Recuperar o envelope XDR da transação
        try:
            envelope_xdr = tx["envelope_xdr"]
            tx_envelope = TransactionEnvelope.from_xdr(
                envelope_xdr, Network.TESTNET_NETWORK_PASSPHRASE
            )
            print("✅ Envelope XDR decodificado com sucesso.")
        except Exception as e:
            print("🚨 Erro ao decodificar o envelope XDR:", e)
            continue

        # Extrair a operação Manage Data com a chave "desafio"
        manage_data_op = None
        for op in tx_envelope.transaction.operations:
            if isinstance(op, ManageData) and op.data_name == "desafio":
                manage_data_op = op
                break

        if not manage_data_op:
            print("🚫 Operação 'manage_data' com a chave 'desafio' não encontrada na transação.")
            continue
        else:
            print("✅ Operação 'manage_data' encontrada.")

        # Mensagem original
        mensagem = "DEV30K".encode()
        mensagem_b64 = base64.b64encode(mensagem)
        print(f"📧 Mensagem em base64: {mensagem_b64.decode()}")

        # Obter a assinatura (bytes)
        assinatura_bytes = manage_data_op.data_value
        print(f"📝 Assinatura (hex): {assinatura_bytes.hex()}")

        # Criar um objeto Keypair a partir da chave pública
        try:
            keypair = Keypair.from_public_key(public_key)
            print("✅ Keypair criado com sucesso.")
        except Exception as e:
            print("🚨 Erro ao criar Keypair a partir da chave pública:", e)
            continue

        # Verificar a assinatura
        try:
            keypair.verify(mensagem_b64, assinatura_bytes)
            print("✅ A assinatura é válida. A mensagem foi assinada pela chave pública fornecida.")
        except BadSignatureError:
            print("❌ A assinatura é inválida. A mensagem não foi assinada pela chave pública fornecida.")
        except Exception as e:
            print("🚨 Erro ao verificar a assinatura:", e)

# Executar a função
read()
