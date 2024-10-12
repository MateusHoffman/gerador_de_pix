from pixqrcodegen import Payload
import requests

# Função para gerar QR Code PIX
def gerar_pix(txtId):
    # Criando a Payload com os parâmetros necessários
    payload = Payload(
        nome='PIX',  # Nome do recebedor
        chavepix='024cc8b4-c919-4e47-8ab8-f9553c54bafb',  # Chave Pix (CPF, CNPJ, e-mail, telefone ou chave aleatória)
        valor='0.01',  # Valor da transação
        cidade='cidade',  # Cidade do recebedor
        txtId=txtId  # Identificador da transação (opcional)
    )

    # Gerar a Payload do Pix e o QR Code
    qr_code_payload = payload.gerarPayload()
    print("QR Code gerado com sucesso!")
    return qr_code_payload

# Função para consultar o status do pagamento
def consultar_transacao(access_token, txtId):
    url = f"https://api.mercadopago.com/v1/payments/search?external_reference={txtId}"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        transaction_info = response.json()
        if transaction_info['results']:
            payment = transaction_info['results'][0]
            print("Status da Transação:", payment.get("status"))
            print("Valor:", payment.get("transaction_details", {}).get("total_paid_amount"))
            print("Data da Transação:", payment.get("date_created"))
        else:
            print("Transação não encontrada. Verifique se o pagamento foi realizado.")
    else:
        print("Erro ao consultar a transação:", response.status_code, response.text)

if __name__ == "__main__":
    # Substitua pelo txtId da transação que você deseja consultar
    txtId = "01NJOFNWAONFAWOINFOWIAN"  # Exemplo de ID da transação

    # Gerar o QR Code
    qr_code_payload = gerar_pix(txtId)

    # Token de Acesso obtido anteriormente
    access_token = "APP_USR-524008420608597-093014-86ae2aec3d7d75b7e0cb26f34e621de2-2014593674"  # Coloque aqui seu token

    if access_token:
        # Consultando a transação
        consultar_transacao(access_token, txtId)
