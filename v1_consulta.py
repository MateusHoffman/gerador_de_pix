import requests
import json

class GerencianetAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.token_type = None
        self.expiry_in = None
        self.get_access_token()

    def get_access_token(self):
        url = "https://api.gerencianet.com.br/v1/token"
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            token_info = response.json()
            self.access_token = token_info['access_token']
            self.token_type = token_info['token_type']
            self.expiry_in = token_info['expires_in']
        else:
            raise Exception("Failed to obtain access token")

    def verificar_pagamento(self, codigo_pix):
        url = f"https://api.gerencianet.com.br/v1/charge/{codigo_pix}"
        headers = {
            "Authorization": f"{self.token_type} {self.access_token}",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            pagamento_info = response.json()
            return pagamento_info  # Retorna detalhes do pagamento
        else:
            return f"Erro ao verificar pagamento: {response.status_code} - {response.text}"

if __name__ == '__main__':
    client_id = ""
    client_secret = ""
    
    gerencianet = GerencianetAPI(client_id, client_secret)
    
    # Substitua 'codigo_pix_aqui' pelo seu código PIX para consulta
    codigo_pix = "00020126580014BR.GOV.BCB.PIX0136024cc8b4-c919-4e47-8ab8-f9553c54bafb52040000530398654040.015802BR5903PIX6006cidade62080504test63044CD3"
    status_pagamento = gerencianet.verificar_pagamento(codigo_pix)
    print(status_pagamento)
