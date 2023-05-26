import unittest
import json
from datetime import datetime
from flask import Flask
from flask.testing import FlaskClient
from unittest.mock import patch

from node import app, blockchain, Block

class TestBlockchainNode(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_block(self):
        # Mock de la funció get_latest_block per retornar un bloc de genesi
        def mock_get_latest_block():
            return Block(0, "01/01/2023", "Genesis Block", "0")

        with patch('node.blockchain.get_latest_block', mock_get_latest_block):
            data = 'Sample Data'
            expected_block_index = 1

            response = self.client.post('/add_block', json={'data': data})
            self.assertEqual(response.status_code, 200)
            response_data = json.loads(response.data)
            self.assertEqual(response_data['message'], 'Block added successfully')

            latest_block = blockchain.get_latest_block()
            self.assertEqual(latest_block.index, expected_block_index)
            self.assertEqual(latest_block.timestamp, datetime.now().strftime("%d/%m/%Y"))
            self.assertEqual(latest_block.data, data)
            self.assertEqual(latest_block.previous_hash, blockchain.chain[0].hash)
            self.assertEqual(latest_block.hash, latest_block.calculate_hash())

    def test_get_chain(self):
        # Mock de la cadena de blocs amb 3 blocs
        mock_chain = [
            Block(0, "01/01/2023", "Genesis Block", "0"),
            Block(1, "02/01/2023", "Data 1", "hash1"),
            Block(2, "03/01/2023", "Data 2", "hash2")
        ]
        blockchain.chain = mock_chain

        response = self.client.get('/get_chain')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        returned_chain = response_data['chain']
        self.assertEqual(len(returned_chain), len(mock_chain))

        for i, block_data in enumerate(returned_chain):
            self.assertEqual(block_data['index'], mock_chain[i].index)
            self.assertEqual(block_data['timestamp'], mock_chain[i].timestamp)
            self.assertEqual(block_data['data'], mock_chain[i].data)
            self.assertEqual(block_data['previous_hash'], mock_chain[i].previous_hash)
            self.assertEqual(block_data['hash'], mock_chain[i].hash)


if __name__ == '__main__':
    unittest.main()

    
    
    # En aquest exemple, s'utilitza la classe FlaskClient de flask.testing per realitzar les sol·licituds HTTP al node de la blockchain durant els tests.

# Els dos mètodes de test test_add_block i test_get_chain comproven el comportament de les rutes /add_block i /get_chain, respectivament.

# En test_add_block, s'utilitza un mock per substituir la funció get_latest_block de la cadena de blocs i assegurar que retorna un bloc de genesi. Es fa una sol·licitud POST a /add_block amb dades de prova i s'avalua si la resposta té el codi d'estat correcte i el missatge esperat. A continuació, es comprova si s'ha afegit un nou bloc a la cadena de blocs amb les dades correctes.

# En test_get_chain, s'estableix un mock de la cadena de blocs amb tres blocs de prova. Es
