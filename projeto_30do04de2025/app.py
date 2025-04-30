from flask import Flask, jsonify,request
import requests

app = Flask(__name__)

pedidos = []

@app.route('/pedidos', methods=['POST'])
def  novo_pedido():
    dados = request.json
    id_produto = dados.get('id_produto')

    resposta = requests.get('http://localhost:5030/produtos')
    lista_produtos = resposta.json()

    produto = next((p for p in lista_produtos if p ['id'] == id_produto), None)

    if not produto:
        return jsonify({"erro": "Produto não encontra"}), 404

    pedido = {
        "produto": produto['nome'],
        "valor": produto['preco']
    }

    pedidos.append(pedido)

    return jsonify(pedido), 201

@app.route('/pedidos')
def listar_pedidos():
    return jsonify(pedidos)

if __name__ == '__main__':
    app.run(debug=True, port=5050)