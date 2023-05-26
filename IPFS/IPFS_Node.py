import ipfshttpclient
from flask import Flask, jsonify, request

# Crear una nova instància de Flask
app = Flask(__name__)

# Connectar-se al client IPFS local
client = ipfshttpclient.connect()

# Ruta per afegir un fitxer a IPFS
@app.route('/add_file', methods=['POST'])
def add_file():
    file = request.files['file']
    file_content = file.read()
    ipfs_response = client.add_bytes(file_content)
    file_hash = ipfs_response['Hash']
    response = {'file_hash': file_hash}
    return jsonify(response), 200

# Ruta per obtenir un fitxer des de IPFS
@app.route('/get_file/<string:file_hash>', methods=['GET'])
def get_file(file_hash):
    ipfs_response = client.cat(file_hash)
    file_content = ipfs_response.read()
    response = {'file_content': file_content.decode('utf-8')}
    return jsonify(response), 200

if __name__ == '__main__':
    # Executar l'aplicació Flask en el port 5000
    app.run(port=5000)

    # En aquest exemple, s'utilitza la llibreria ipfshttpclient per connectar-se a un client IPFS local.

# La funció add_file s'activarà quan es rebi una sol·licitud POST a /add_file. Llegeix el fitxer que s'ha enviat amb la sol·licitud i el contingut es guarda en una variable file_content. A continuació, es fa servir el client IPFS per afegir el contingut a IPFS amb l'ajuda de la funció add_bytes. Es recupera el hash del fitxer resultant i es retorna com a resposta JSON.

# La funció get_file s'activarà quan es rebi una sol·licitud GET a /get_file/<file_hash>, on <file_hash> és el hash del fitxer desitjat a IPFS. S'utilitza el client IPFS per obtenir el contingut del fitxer mitjançant la funció cat. El contingut es retorna com a resposta JSON.

# Per executar el node d'IPFS, guarda'l en un fitxer, com ara ipfs_node.py, i des de la línia de comandes, executa python ipfs_node.py. El node s'escoltarà en el port 5000 i estarà preparat per rebre sol·licituds per afegir i obtenir fitxers des de IPFS.

# Pots utilitzar eines com Postman o fer sol·licituds HTTP des de Python per provar les rutes /add_file i /get_file del node d'IPFS i veure com responen.
