from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Entrega Solution Sprint 5 - FIAP"

if __name__ == '__main__':
    app.run()
