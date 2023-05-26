# Per crear un programa que integri tots els scripts anteriors i proporcioni una interfície per penjar fitxers, signar-los digitalment, encriptar-los i emmagatzemar-los a IPFS, així com mantenir un seguiment dels fitxers emmagatzemats, es pot utilitzar un marc de treball web com Flask per implementar l'aplicació.


import os
import ipfshttpclient
from flask import Flask, render_template, request, redirect

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Crear una nova instància de Flask
app = Flask(__name__)

# Connectar-se al client IPFS local
client = ipfshttpclient.connect()

# Ruta principal de l'aplicació
@app.route('/')
def index():
    return render_template('index.html')

# Ruta per penjar fitxers i realitzar el procés de signatura, encriptació i emmagatzematge a IPFS
@app.route('/upload', methods=['POST'])
def upload():
    # Obtenir el fitxer penjat
    file = request.files['file']
    file_content = file.read()

    # Generar un parell de claus RSA per a l'usuari
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # Signar digitalment el fitxer amb la clau privada
    # Utilitza la funció de signatura digital que has creat anteriorment

    # Encriptar el fitxer signat amb una clau simètrica
    # Utilitza l'encriptació que has generat anteriorment

    # Afegir el fitxer encriptat a IPFS
    ipfs_response = client.add_bytes(encrypted_content)
    ipfs_file_hash = ipfs_response['Hash']

    # Registrar el fitxer a la blockchain amb el hash resultant i la clau pública de l'usuari
    # Utilitza les funcions i les estructures de la blockchain que has creat anteriorment

    # Redirigir a la pàgina de seguiment
    return redirect('/files')

# Ruta per mostrar la llista de fitxers emmagatzemats a IPFS
@app.route('/files')
def files():
    # Obtenir la llista de fitxers des de la blockchain o IPFS
    # Utilitza les funcions o API corresponents per obtenir la informació

    return render_template('files.html', files=files_list)

# Ruta per descarregar i desencriptar un fitxer amb la clau privada de l'usuari
@app.route('/download/<file_hash>')
def download(file_hash):
    # Obtenir el fitxer des d'IPFS
    # Utilitza la API d'IPFS per obtenir el contingut del fitxer

    # Desencriptar el fitxer amb la clau privada de l'usuari
    # Utilitza la funció de desencriptació que has creat anteriorment

    # Descarregar el fitxer desencriptat
    # Pots utilitzar la biblioteca Flask per retornar el fitxer com a resposta

    return file_content

if __name__ == '__main__':
    app.run(debug=True)

    
    # En aquest exemple, s'utilitza el marc de treball Flask per crear l'aplicació web. Hi ha tres rutes importants:

# La ruta principal (/) mostra una pàgina d'inici que permet a l'usuari penjar fitxers.
# La ruta /upload és responsable de penjar els fitxers i realitzar el procés de signatura, encriptació i emmagatzematge a IPFS.
# La ruta /files mostra una llista de fitxers emmagatzemats a IPFS o registrats a la blockchain.
# La ruta /download/<file_hash> permet a l'usuari descarregar i desencriptar un fitxer utilitzant la seva clau privada.
# El codi anterior és només un exemple i hauràs d'adaptar-lo a les teves necessitats. També caldrà implementar les funcions de signatura, encriptació, emmagatzematge a la blockchain i recuperació de fitxers des de l'IPFS segons les biblioteques i les estructures que estiguis utilitzant.

# A més, hauràs de crear les plantilles HTML (index.html i files.html) per a la interfície de l'aplicació. Pots personalitzar-les segons el teu disseny i les necessitats del teu projecte.

# Finalment, per executar l'aplicació, assegura't d'instal·lar les dependències necessàries (Flask, cryptography, ipfshttpclient) amb pip install flask cryptography ipfshttpclient i executa el programa amb python main.py. L'aplicació s'iniciarà i estarà disponible a l'adreça http://localhost:5000.
