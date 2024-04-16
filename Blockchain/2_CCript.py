# Script per a encriptar fitxers utilitzant la C obtinguda prèviament del KeyGen


pip install cryptography

import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import ipfshttpclient
import os

def generate_random_key():
    return os.urandom(32)  # Genera una clau aleatòria de 32 bytes

def generate_key_from_ipfs(ipfs_hash):
    # Suposem que la funció get_key_from_ipfs obté la clau de la base de dades IPFS
    # El codi aquí és només un exemple i necessitaràs adaptar-lo a les teves necessitats
    with ipfshttpclient.connect() as client:
        key_data = client.cat(ipfs_hash)
        return base64.b64decode(key_data)

def encrypt_file(file_path, ipfs_hash):
    key = generate_key_from_ipfs(ipfs_hash)

    with open(file_path, 'rb') as f:
        plaintext = f.read()

    # Usem SHA-256 per obtenir una clau de 32 bytes
    key_hash = hashlib.sha256(key).digest()

    # Generem un vector d'inicialització aleatori
    iv = os.urandom(16)  # Genera un IV aleatori

    # Configurem l'algorisme de xifrat
    cipher = Cipher(algorithms.AES(key_hash), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Xifrem el contingut del fitxer
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Escriure el contingut xifrat a un nou fitxer
    with open(file_path + '.enc', 'wb') as f:
        f.write(ciphertext)

    print("Fitxer xifrat amb èxit.")
    print("Hash SHA-256 del contingut xifrat:", hashlib.sha256(ciphertext).hexdigest())

# Exemple d'ús
def main():
    file_path = input("Arrossega i deixa anar el fitxer que vols encriptar: ").strip()
    ipfs_hash = 'IPFS_HASH_DE_LA_CLAU'  # Has d'assignar l'adreça IPFS de la clau

    encrypt_file(file_path, ipfs_hash)

if __name__ == "__main__":
    main()



#En aquest script:
# S'ha afegit una funció generate_random_key que genera una clau aleatòria de 32 bytes per a la teva encriptació.
# S'ha canviat l'ús de l'IV per utilitzar os.urandom(16) per generar un vector d'inicialització aleatori.
# A més, la funció main permet a l'usuari arrossegar i deixar anar un fitxer per encriptar.
# Recorda adaptar la variable ipfs_hash amb l'adreça IPFS correcta de la clau de la base de dades i gestionar la clau generada de manera segura en el teu sistema.
