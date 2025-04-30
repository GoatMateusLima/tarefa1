from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 9000},
    {"id": 2, "nome": "Iphone", "preco": 700},
    {"id": 3, "nome": "Pc Gamer", "preco": 9000},
    {"id": 4, "nome": "carro", "preco": "150.000.000.000.900,00"},
    {"id": 5, "nome": "copo", "preco": 7300},
    {"id": 6, "nome": "mesa", "preco": 5900}
]

@app.route('/produtos')
def listar_produtos():
    return jsonify(produtos)

if __name__ == '__main__':
    app.run(port=5030)