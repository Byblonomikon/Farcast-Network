import unittest
import hashlib
import ipfshttpclient
from datetime import datetime

class Block:
    # ...

class Blockchain:
    # ...


class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_create_genesis_block(self):
        genesis_block = self.blockchain.create_genesis_block()
        self.assertEqual(genesis_block.index, 0)
        self.assertEqual(genesis_block.timestamp, "01/01/2023")
        self.assertEqual(genesis_block.data, "Genesis Block")
        self.assertEqual(genesis_block.previous_hash, "0")
        self.assertEqual(genesis_block.hash, genesis_block.calculate_hash())

    def test_get_latest_block(self):
        latest_block = self.blockchain.get_latest_block()
        self.assertEqual(latest_block, self.blockchain.chain[0])

    def test_add_block(self):
        previous_block = self.blockchain.get_latest_block()
        data = "Sample Data"
        new_block = Block(
            index=previous_block.index + 1,
            timestamp=datetime.now().strftime("%d/%m/%Y"),
            data=data,
            previous_hash=previous_block.hash
        )
        self.blockchain.add_block(new_block)

        latest_block = self.blockchain.get_latest_block()
        self.assertEqual(latest_block.index, previous_block.index + 1)
        self.assertEqual(latest_block.timestamp, datetime.now().strftime("%d/%m/%Y"))
        self.assertEqual(latest_block.data, data)
        self.assertEqual(latest_block.previous_hash, previous_block.hash)
        self.assertEqual(latest_block.hash, latest_block.calculate_hash())

    def test_validate_chain_valid(self):
        is_valid = self.blockchain.validate_chain()
        self.assertTrue(is_valid)

    def test_validate_chain_invalid(self):
        # Modify the data of a block to make the chain invalid
        block_to_modify = self.blockchain.chain[0]
        block_to_modify.data = "Modified Data"

        is_valid = self.blockchain.validate_chain()
        self.assertFalse(is_valid)


if __name__ == '__main__':
    unittest.main()

    
    
    #En aquest exemple, s'han creat diversos mètodes de test per comprovar el funcionament de la classe Blockchain. El mètode setUp s'executa abans de cada test i s'inicialitza una nova instància de Blockchain per mantenir l'estat aïllat entre els tests.

#Els mètodes de test comproven diversos aspectes com la creació del bloc de genesi, l'afegir un nou bloc, obtenir l'últim bloc de la cadena, validar la cadena de blocs i comprovar la validesa de la cadena en cas d'haver modificat dades.

#Per executar aquests tests, guarda'l en un fitxer, com ara test_blockchain.py, i des de la línia de comandes, executa python test_blockchain.py. Es mostrarà el resultat dels tests que s'han executat.
