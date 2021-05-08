from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/saludo/superman', methods=['GET'])
def superman():
    return jsonify({"respuesta" : "hola soy superman"})

@app.route('/saludo/batman' , methods=['GET'])
def batman():
    return jsonify({"respuesta" : "hola soy batman"})

@app.route('/poderes' , methods=['POST'])
def poderes():
    content = request.get_json()
    respuestaGeneral = []
    for i in content:
        if i["super heroe"]["nombre"] == 'superman' :
            respuestaGeneral.append({ "super heroe": i["super heroe"]["nombre"]})
            respuesta= []
            respuesta.append({" poder" : "superfuerza"})
            respuesta.append({" debilidad" : "criptonita"})
            respuestaGeneral.append(respuesta)
        if i["super heroe"]["nombre"] == 'batman' :
            respuestaGeneral.append({ "super heroe": i["super heroe"]["nombre"]})
            respuesta= []
            respuesta.append({ "poder": "dinero"})
            respuesta.append({" debilidad": "espalda :v"})
            respuestaGeneral.append(respuesta)
    return jsonify(respuestaGeneral)

def main():
    app.run(host="0.0.0.0", port="4000", debug=True)

if __name__ =='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("saliendo")
        exit()

