import requests

# Função para consultar o status do pagamento
def consultar_transacao(access_token, txtId):
    url = f"https://api.mercadopago.com/v1/payments/search?external_reference={txtId}"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    print(f"Consultando a transação para txtId: {txtId}")  # Log da consulta

    if response.status_code == 200:
        transaction_info = response.json()
        print("Resposta da API:", transaction_info)  # Log da resposta completa
        if transaction_info['results']:
            payment = transaction_info['results'][0]
            print("Status da Transação:", payment.get("status"))
            print("Valor:", payment.get("transaction_details", {}).get("total_paid_amount"))
            print("Data da Transação:", payment.get("date_created"))
        else:
            print("Transação não encontrada. Verifique se o pagamento foi realizado e se o txtId está correto.")
    else:
        print("Erro ao consultar a transação:", response.status_code, response.text)

if __name__ == "__main__":
    # Substitua pelo txtId da transação que você deseja consultar
    txtId = "01NJOFNWAONFAWOINFOWIAN"  # Exemplo de ID da transação

    # Obtendo o token de acesso
    access_token = "APP_USR-524008420608597-093014-86ae2aec3d7d75b7e0cb26f34e621de2-2014593674"

    if access_token:
        # Consultando a transação
        consultar_transacao(access_token, txtId)
