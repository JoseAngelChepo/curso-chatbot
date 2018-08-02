from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello():
    tipo_de_peticion = request.method
    json_de_entrada = request.get_json()
    print(tipo_de_peticion)
    print(json_de_entrada)
    json_de_respuesta = {
        "text": "Hola Mundo",
        "tipo_peticion": tipo_de_peticion
    }
    return jsonify(json_de_respuesta)

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    tipo_de_peticion = request.method
    if tipo_de_peticion == 'GET':
        if request.args.get('hub.verify_token') == 'PALABRA_SECRETA':
            return request.args.get('hub.challenge')
        else:
            return "NECESITAS INGRESAR EL TOKEN DE VERIFICACION :D"
    elif tipo_de_peticion == 'POST':
        print("LLEGÓ UN MENSAJE NUEVO")
        mensaje = request.get_json()
        print(mensaje)

if __name__ == '__main__':
    app.run()
