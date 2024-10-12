import requests
import json

# URL do endpoint para obter o token
url = "https://api.mercadopago.com/oauth/token"

# Credenciais da sua aplicação
client_id = "524008420608597"  # Substitua pelo seu Client ID
client_secret = "IkSgHh8MXrQGEqlP16BWlDQRu4SSmAf1"  # Substitua pelo seu Client Secret

# Dados para autenticação
data = {
    "client_secret": client_secret,
    "client_id": client_id,
    "grant_type": "client_credentials",
    "code": "TG-XXXXXXXX-241983636",  # Substitua pelo seu código
    "code_verifier": "47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU",  # Substitua pelo seu code_verifier
    "redirect_uri": "https://www.redirect-url.com?code=CODE&state=RANDOM_ID",  # Substitua pela sua URL de redirecionamento
    "refresh_token": "TG-XXXXXXXX-241983636",  # Substitua pelo seu refresh_token, se aplicável
    "test_token": "false"
}

# Fazendo a requisição POST para obter o token
response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))

# Verificando a resposta
if response.status_code == 200:
    token_info = response.json()
    access_token = token_info.get("access_token")
    print("Token de Acesso:", access_token)
else:
    print("Erro ao obter o token:", response.status_code, response.text)
