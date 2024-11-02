# Stellar Mainnet Desafios - Assinatura e Transações com Memo

Este repositório contém os scripts necessários para cumprir dois desafios de transação usando o Stellar SDK em Python, enviando transações com assinaturas específicas na Stellar Mainnet.

## Desafios

### Desafio 1: Criar uma Transação com "DEV30K" Assinado no MEMO

- **Descrição**: Criar uma transação na Stellar Mainnet, incluindo o texto "DEV30K" no campo Memo e uma operação `manage_data_op`.
- **Passo a Passo**:
  - Utilizar a chave privada para assinar o texto `DEV30K`.
  - Converter a assinatura para o formato Base64.
  - Criar uma transação com um `manage_data_op` que tenha:
    - **Chave**: `desafio`
    - **Valor**: Assinatura em Base64 do texto `DEV30K`.
  - Enviar a transação para a Mainnet da Stellar.
- **Critério de Aceite**: Hash da transação gerada.

### Desafio 2: Explicação e Critérios de Aceite

- **Descrição**: Enviar a transação assinada para a Mainnet e fornecer o hash da transação para o formulário de submissão.
- **Critérios de Aceite**:
  - A transação deve incluir o Memo `DEV30K`.
  - O `manage_data_op` deve conter o campo `desafio` com o valor da assinatura em Base64.
  - O **hash da transação** deve ser extraído do servidor `Horizon` após a submissão bem-sucedida e fornecido para verificação.

## Requisitos

- Python 3.6+
- Bibliotecas:
  - [`stellar-sdk`](https://pypi.org/project/stellar-sdk/) - para comunicação com a rede Stellar.
- Stellar Mainnet Keypair:
  - Chaves públicas e privadas reais (chave pública começa com `G` e a privada com `S`).

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
pip install stellar-sdk
```

## Scripts e Uso

### Script para Desafio 1 e 2

O script `desafio_stellar.py` assina o texto `DEV30K`, cria a transação com `manage_data_op`, inclui o Memo, e envia a transação para a Mainnet. No final, o hash da transação é exibido.

```python
from stellar_sdk import Keypair, Network, Server, TransactionBuilder
import base64

# Substitua estas variáveis com suas próprias chaves
public_key = "SUA_CHAVE_PUBLICA"  # Sua chave pública da Mainnet
secret_key = "SUA_CHAVE_PRIVADA"  # Sua chave privada da Mainnet

# Conectar-se ao servidor da Stellar Mainnet
server = Server("https://horizon.stellar.org")

# Assinar o texto "DEV30K"
chave = Keypair.from_secret(secret_key)
texto = "DEV30K".encode()
assinatura_binaria = chave.sign(texto)
assinatura_base64 = base64.b64encode(assinatura_binaria).decode()
print("Assinatura Base64:", assinatura_base64)

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
            data_name="desafio",
            data_value=assinatura_base64
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
```

### Executando o Script

Após ajustar as chaves pública e privada, execute o script:

```bash
python desafio_stellar.py
```

### Critério de Aceite

Submeta o **hash da transação** no formulário de submissão como prova de que a transação foi concluída com sucesso.

## Links Úteis

- [Stellar Laboratory](https://laboratory.stellar.org/#explorer?resource=accounts&endpoint=single) – Para verificar a existência e o saldo de uma conta Stellar.
- [Stellar SDK para Python](https://stellar-sdk.readthedocs.io/) – Documentação da Stellar SDK em Python.

## Observações

- **Atenção**: Este script opera na Stellar Mainnet, então as transações são finais e exigem lumens (XLM) reais.
- **Confidencialidade**: Nunca compartilhe suas chaves privadas publicamente ou em repositórios públicos.
