from flask import Flask, render_template, request
import os

app = Flask(__name__)

# ----------------------------------------
# Modo manutenção: ativar enquanto ajusta
@app.route("/")
def index():
    return "<h1>Site em manutenção, voltamos em breve!</h1>"
# ----------------------------------------

# ----------------------------------------
# Descomente esta parte quando quiser reativar a calculadora
# @app.route("/", methods=["GET", "POST"])
# def index():
#     resultado = None
#     if request.method == "POST":
#         try:
#             valor = float(request.form["valor"])
#             juros = float(request.form["juros"])
#             meses = int(request.form["meses"])
#             resultado = valor * (1 + (juros/100) * meses)
#         except:
#             resultado = "Erro nos dados."
#     return render_template("index.html", resultado=resultado)
# ----------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
