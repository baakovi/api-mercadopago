# Importanto biblioteca do Mercado Pago
import mercadopago

# Foi cirada a função que gera toda a configuração de pagamento, retornando o link para iniciar o pagamento.
def gerar_link_pagamento():
    # Criando o SDK - integração do Mercado Pago com o código
    sdk = mercadopago.SDK("TEST-3013944780215666-042423-75f02526d3593d26e2edf4b95df950c6-1764101687")
    # sdk = mercadopago.SDK("YOUR_ACCESS_TOKEN")
    # YOUR_ACESS_TOKEN => colocar o Token de acesso dentro do parênteses (apenas com a conta criada)
    # Integrar a conta com a conta do mercado pago

    # Criação da cobrança, requisição
    payment_data = {
        # "transaction_amount": 100,
        # "token": "CARD_TOKEN",
        # "description": "Payment description",
        # "payment_method_id": 'visa',
        # "installments": 1,
        # "payer": {
        #     "email": 'test_user_123456@testuser.com'
        # }
        # Items --> itens que o usuário está comprando/pagando, lista de itens, dicionário
        "items" : [
        {
            "id" : "1",
            "title" : "Camisa",
            "quantity" : 1,
            "currency_id" : "BRL",
            "unit_price" : 259.99
        },
            # Exemplo com mais de um item
        # {
            #  "id" : "2",
            #  "title" : "Calça",
            #  "quantity" : 1,
            #  "currency_id" : "BRL",
            #  "unit_price" : 359.99
        # },
        ],
        # Os urls do back_urls são os links do site
        "back_urls": {
            # auto_return = direcionar automaticamente para o link de sucesso (compracerta).
            # Cria um pagamento executável, com todas as configurações do pagamento, como o ID do cliente, o link para o usuário ser direcionado para ele iniciar o processo de pagamento
            "success": "http://http://127.0.0.1:5000/compracerta",
            "failure": "http://http://127.0.0.1:5000/compraerrada",
            "pending": "http://http://127.0.0.1:5000/compraerrada",
        },
        "auto_return": "all"
        # Paramêtros: approved ou all
    }

    # Criar o pagamento, vai dar erro pois o código esta usando a API de preferência, não a de 'payment'.
    # result = sdk.payment().create(payment_data)

    # "sdk.payment" alterado para "sdk.preference"
    result = sdk.preference().create(payment_data)

    # Pegar o resultado do pagamento
    payment = result["response"]

    # Ao invés de retornar todo o resultado, retorna apenas o link do pagamento necessário localizado no "init_point".
    link_iniciar_pagamento = payment["init_point"]

    return link_iniciar_pagamento

    # Printar o resultado
    # print(payment)

# init_point ==> "https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=1764101687-8afa8268-1fb3-442f-96c2-d866d2da3c16". Link de início da cobrança