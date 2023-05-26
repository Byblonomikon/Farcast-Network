  # Aquí tens un exemple bàsic d'un codi Python per crear una blockchain per a un projecte de gestió documental on s'inclou el hash resultant d'incloure fitxers en IPFS
  
import hashlib
import ipfshttpclient

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.index).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8')
        )
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "01/01/2023", "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


# Exemple d'ús
if __name__ == '__main__':
    blockchain = Blockchain()
    client = ipfshttpclient.connect()  # Connexió amb el client IPFS local

    # Exemple d'afegir un document a la blockchain
    document_path = '/path/to/document.txt'
    with open(document_path, 'rb') as file:
        file_content = file.read()

    # Afegir el document a IPFS
    ipfs_response = client.add_bytes(file_content)
    file_hash = ipfs_response['Hash']

    # Crear un nou bloc i afegir-lo a la blockchain
    latest_block = blockchain.get_latest_block()
    new_block = Block(
        index=latest_block.index + 1,
        timestamp="26/05/2023",
        data=file_hash,
        previous_hash=latest_block.hash
    )
    blockchain.add_block(new_block)

    # Validar la cadena de blocs
    is_valid = blockchain.validate_chain()
    if is_valid:
        print("La cadena de blocs és vàlida.")
    else:
        print("La cadena de blocs no és vàlida.")

        
        
      
# En aquest exemple, es defineixen dues classes principals: Block i Blockchain. La classe Block representa un bloc individual de la cadena de blocs i conté els atributs com l'índex, la data i el hash. La classe Blockchain és responsable de gestionar tota la cadena de blocs.

# Per afegir un document a la blockchain, es fa servir la llibreria ipfshttpclient per a connectar-se amb un client IPFS local. En l'exemple d'ús, s'obre el fitxer de document desitjat, es llegeix el seu contingut i s'afegeix a IPFS amb l'ajuda de la funció add_bytes del client IP
