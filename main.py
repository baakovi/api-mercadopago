from flask import Flask, render_template

from apimercadopago import gerar_link_pagamento

app = Flask(__name__)

@app.route("/")
def homepage():
    link_iniciar_pagamento = gerar_link_pagamento()
    return render_template("homepage.html", link_pagamento=link_iniciar_pagamento)

@app.route("/compracerta")
def compra_certa():
    return render_template("compracerta.html")

@app.route("/compraerrada")
def compra_errada():
    return render_template("compraerrada.html")

if __name__ == "__main__":
    app.run()

# Resposta do pagamento:
# http://127.0.0.1:5000/compracerta?collection_id=1322856265&collection_status=approved&payment_id=1322856265&status=approved&external_reference=null&payment_type=credit_card&merchant_order_id=18036994131&preference_id=1764101687-add69a25-29c4-41b7-8a36-c1ff0f636222&site_id=MLB&processing_mode=aggregator&merchant_account_id=null
# Para evitar esta URL grande, é necessário encurtar o URL

# ID do pagamento: https://sandbox.mercadopago.com.br/checkout/v1/redirect?pref_id=1764101687-8afa8268-1fb3-442f-96c2-d866d2da3c16