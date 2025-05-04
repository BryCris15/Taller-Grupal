import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def llamar_servicio_b():
    respuesta = requests.get("http://servicio_b:5002")
    return f"Respuesta del nodo B: {respuesta.text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
