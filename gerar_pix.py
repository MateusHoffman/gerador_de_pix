# Importando o módulo
from pixqrcodegen import Payload

# Criando a Payload com os parâmetros necessários
payload = Payload(
    nome='PIX',         # Nome do recebedor
    chavepix='024cc8b4-c919-4e47-8ab8-f9553c54bafb',        # Chave Pix (CPF, CNPJ, e-mail, telefone ou chave aleatória)
    valor='0.01',                  # Valor da transação
    cidade='cidade',      # Cidade do recebedor
    txtId='NGOEIRNGIEONGOEINOIGA'                 # Identificador da transação (opcional)
)

# Gerar a Payload do Pix e o QR Code
payload.gerarPayload()

# Informar ao usuário que o QR Code foi gerado
print("QR Code gerado com sucesso!")
