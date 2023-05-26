import ipfshttpclient
import hashlib
from flask import Flask, request, jsonify

# Crear una nova instància de Flask
app = Flask(__name__)

# Connectar-se al client IPFS local
client = ipfshttpclient.connect()

# Funció per calcular el resum criptogràfic SHA-256 d'un fitxer
def calculate_sha256(file_content):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(file_content)
    return sha256_hash.hexdigest()

# Ruta per afegir un fitxer encriptat a IPFS utilitzant SHA-256
@app.route('/add_encrypted_file', methods=['POST'])
def add_encrypted_file():
    file = request.files['file']
    file_content = file.read()

    # Calcular el resum criptogràfic SHA-256 del contingut del fitxer
    file_hash = calculate_sha256(file_content)

    # Afegir el fitxer a IPFS
    ipfs_response = client.add_bytes(file_content)
    ipfs_file_hash = ipfs_response['Hash']

    response = {'file_hash': file_hash, 'ipfs_file_hash': ipfs_file_hash}
    return jsonify(response), 200

if __name__ == '__main__':
    # Executar l'aplicació Flask en el port 5000
    app.run(port=5000)

    
    # En aquest exemple, s'utilitza la biblioteca hashlib de Python per calcular el resum criptogràfic SHA-256 del contingut del fitxer mitjançant la funció calculate_sha256.

# La ruta /add_encrypted_file permet afegir un fitxer encriptat a IPFS utilitzant l'algoritme SHA-256. S'envia el fitxer com a part de la sol·licitud POST i es calcula el resum criptogràfic SHA-256 del contingut del fitxer. A continuació, s'afegeix el fitxer a IPFS mitjançant el client IPFS. Finalment, es retorna el resum criptogràfic SHA-256 i el hash del fitxer a IPFS com a resposta JSON.

# Per executar el programa, guarda'l en un fitxer, com ara sha256_and_ipfs.py, i des de la línia de comandes, executa python sha256_and_ipfs.py. El programa s'escoltarà en el port 5000 i estarà preparat per rebre sol·licituds per afegir fitxers encriptats utilitzant SHA-256 a IPFS.
