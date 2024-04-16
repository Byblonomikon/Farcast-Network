# Aqui presentem un exemple de creació de xarxa BC.


import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)  # Creem el bloc genèric de la cadena

    def new_block(self, proof, previous_hash=None):
        """
        Creem un nou bloc a la cadena de blocs
        :param proof: La prova donada per l'algorisme de prova de treball
        :param previous_hash: Hash del bloc anterior
        :return: Nou bloc
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reiniciem la llista de transaccions actuals
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Afegir una nova transacció a la llista de transaccions pendents
        :param sender: Adreça del remitent
        :param recipient: Adreça del destinatari
        :param amount: Quantitat
        :return: L'índex del bloc que contindrà aquesta transacció
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Generem un hash SHA-256 d'un bloc
        :param block: Bloc
        :return: String que conté el hash
        """

        # Ordenem el diccionari per assegurar la consistència del hash
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Retorna l'últim bloc de la cadena
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Algoritme de prova de treball:
        - Trobar un nombre p' tal que hash(pp') conté 4 zeros a l'inici, on p és l'anterior prova i p' és la nova prova
        :param last_proof: Prova anterior
        :return: Nova prova
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Verifiquem si la prova és vàlida o no
        :param last_proof: Prova anterior
        :param proof: Prova actual
        :return: True si la prova és vàlida, False si no
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Comprovem si els 4 primers caràcters del hash són zeros

# Exemple d'ús:

# Inicialitzem la cadena
blockchain = Blockchain()

# Exemple de nova transacció
blockchain.new_transaction("emissor1", "receptor1", 10)

# Exemple de prova de treball
last_block = blockchain.last_block
last_proof = last_block['proof']
proof = blockchain.proof_of_work(last_proof)

# Afegim el nou bloc a la cadena
previous_hash = blockchain.hash(last_block)
block = blockchain.new_block(proof, previous_hash)

print("Cadena de blocs:", blockchain.chain)
