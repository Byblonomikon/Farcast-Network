import hashlib
import ipfshttpclient
from datetime import datetime
from flask import Flask, jsonify, request

class Block:
    # ...

class Blockchain:
    # ...

# Crear una nova instància de Flask
app = Flask(__name__)

# Crear una instància de la cadena de blocs
blockchain = Blockchain()

# Ruta per afegir un nou bloc a la cadena de blocs
@app.route('/add_block', methods=['POST'])
def add_block():
    data = request.json['data']
    previous_block = blockchain.get_latest_block()
    new_block = Block(
        index=previous_block.index + 1,
        timestamp=datetime.now().strftime("%d/%m/%Y"),
        data=data,
        previous_hash=previous_block.hash
    )
    blockchain.add_block(new_block)
    response = {'message': 'Block added successfully'}
    return jsonify(response), 200

# Ruta per obtenir tota la cadena de blocs
@app.route('/get_chain', methods=['GET'])
def get_chain():
    chain = []
    for block in blockchain.chain:
        chain.append({
            'index': block.index,
            'timestamp': block.timestamp,
            'data': block.data,
            'previous_hash': block.previous_hash,
            'hash': block.hash
        })
    response = {'chain': chain}
    return jsonify(response), 200

if __name__ == '__main__':
    # Executar l'aplicació Flask en el port 5000
    app.run(port=5000)

    
 #   En aquest exemple, s'utilitza el framework Flask per crear una API web per al node de la blockchain. Es defineixen dues rutes: /add_block per afegir un nou bloc a la cadena de blocs i /get_chain per obtenir tota la cadena de blocs.

# La funció add_block s'activarà quan es rebi una sol·licitud POST a /add_block. Es llegirà el camp data de la sol·licitud JSON i s'afegirà un nou bloc a la cadena de blocs.

# La funció get_chain s'activarà quan es rebi una sol·licitud GET a /get_chain. Recorrerà tota la cadena de blocs i crearà una llista amb la informació dels blocs, que es retornarà com a resposta JSON.

# Per executar el node de la blockchain, guarda'l en un fitxer, com ara node.py, i des de la línia de comandes, executa python node.py. El node s'escoltarà en el port 5000 i estarà preparat per rebre sol·licituds per afegir blocs o obtenir la cadena de blocs.

# Pots utilitzar eines com Postman o fer sol·licituds HTTP des de Python per provar les rutes /add_block i /get_chain del node de la blockchain i veure com responen.
