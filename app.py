import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        try:
            valor = float(request.form["valor"])
            juros = float(request.form["juros"])
            meses = int(request.form["meses"])
            # juros simples: M = C * (1 + i * t)
            resultado = valor * (1 + (juros/100) * meses)
        except:
            resultado = "Erro nos dados."
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway define a porta via variável de ambiente
    app.run(host="0.0.0.0", port=port, debug=True)
