# Script per a Encriptar el hash resultant de IPFS (InCClude) amb la clau Privada de l’usuari i obtenir el BlockHash, que s’inclourà a la blockchain publica



from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def encrypt_with_private_key(data, private_key):
    private_key_bytes = serialization.load_pem_private_key(
        private_key.encode(), password=None, backend=default_backend())
    
    encrypted_data = private_key_bytes.sign(
        data.encode(), padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    return encrypted_data

def main():
    # L'usuari introdueix el hash resultant del fitxer IPFS
    file_hash = input("Introdueix el hash resultant del fitxer IPFS: ")

    # L'usuari introdueix la seva clau privada
    private_key_pem = input("Introdueix la teva clau privada (en format PEM): ")

    # Encripta el hash resultant amb la clau privada de l'usuari
    encrypted_hash = encrypt_with_private_key(file_hash, private_key_pem)
    print("Hash encriptat amb la clau privada:", encrypted_hash.hex())

if __name__ == "__main__":
    main()



En aquesta versió, el programa demana a l'usuari que introdueixi el hash resultant del fitxer IPFS i també la seva clau privada en format PEM. A continuació, utilitza aquesta informació per encriptar el hash amb la funció encrypt_with_private_key. Això permet que l'usuari introdueixi dinàmicament la seva pròpia clau privada en lloc de tenir-la fixada en el codi font.
