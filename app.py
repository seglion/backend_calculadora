from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/sumar',methods=['GET'])
def sumar():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    
    return jsonify({'resultado':a+b})

@app.route('/restar', methods=['GET'])
def restar():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({"resultado": a - b})

@app.route('/multiplicar', methods=['GET'])
def multiplicar():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({"resultado": a * b})

@app.route('/dividir', methods=['GET'])
def dividir():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    if b == 0:
        return jsonify({"error": "División entre cero no permitida"}), 400
    return jsonify({"resultado": a / b})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
