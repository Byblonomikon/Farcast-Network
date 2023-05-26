from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def sign_file(private_key_path, file_path):
    # Carrega la clau privada des de l'arxiu
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )

    # Llegeix el contingut del fitxer a signar
    with open(file_path, "rb") as file:
        file_content = file.read()

    # Calcula el resum criptogràfic SHA-256 del contingut del fitxer
    digest = hashes.Hash(hashes.SHA256())
    digest.update(file_content)
    file_hash = digest.finalize()

    # Signa el resum criptogràfic amb la clau privada
    signature = private_key.sign(
        file_hash,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )

    # Retorna la signatura en format de bytes
    return signature

# Exemple d'ús
private_key_path = "private_key.pem"
file_path = "fitxer.txt"

signature = sign_file(private_key_path, file_path)
print("Signatura digital generada:")
print(signature.hex())



# En aquest exemple, s'utilitza la biblioteca cryptography per generar una signatura digital utilitzant la clau privada de la blockchain. El programa carrega la clau privada des de l'arxiu especificat i llegeix el contingut del fitxer que es vol signar.

# A continuació, es calcula el resum criptogràfic SHA-256 del contingut del fitxer i s'utilitza la clau privada per signar el resum. La signatura es retorna com a resultat en format de bytes.

# Per utilitzar aquest programa, assegura't de tenir la biblioteca cryptography instal·lada amb pip install cryptography. Guarda el codi en un fitxer Python, com ara digital_signature.py, i substitueix les rutes private_key_path i file_path amb les rutes adequades al teu entorn. Executa el programa amb python digital_signature.py i es mostrarà la signatura digital generada per al fitxer especificat.
