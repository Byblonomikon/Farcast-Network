# Script per a instal·lar un node IPFS en l’ordinador


from ipfshttpclient import connect

def main():
    # Connecta amb el node IPFS local
    ipfs = connect('/ip4/127.0.0.1/tcp/5001/http')

    # Exemple d'emmagatzematge d'un fitxer
    file_contents = b"Hello, IPFS World!"
    file_hash = ipfs.add_bytes(file_contents)
    print("Fitxer emmagatzemat a IPFS amb hash:", file_hash)

if __name__ == "__main__":
    main()

