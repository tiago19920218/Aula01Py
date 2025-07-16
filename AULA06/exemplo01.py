#Criação de página usando o Flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bem-vindo á aula de Python!!!"

@app.route("/sobre")
def sobre():
    return "Essa é a página Sobre."

if __name__ == "__main__":
    app.run(debug=True)