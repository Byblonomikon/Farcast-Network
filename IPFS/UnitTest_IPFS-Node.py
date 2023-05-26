import unittest
import json
from flask import Flask
from flask.testing import FlaskClient
from unittest.mock import patch, MagicMock

from ipfs_node import app, client

class TestIPFSNode(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_file(self):
        # Mock de la sol·licitud POST
        file_content = b'Sample File Content'
        mocked_file = MagicMock()
        mocked_file.read.return_value = file_content

        with patch('ipfs_node.request') as mocked_request:
            mocked_request.files = {'file': mocked_file}

            response = self.client.post('/add_file')
            self.assertEqual(response.status_code, 200)
            response_data = json.loads(response.data)
            file_hash = response_data['file_hash']

            # Comprova si el fitxer existeix a IPFS
            ipfs_response = client.cat(file_hash)
            ipfs_file_content = ipfs_response.read()
            self.assertEqual(ipfs_file_content, file_content)

    def test_get_file(self):
        # Mock de la sol·licitud GET
        file_hash = 'QmTestFileHash'
        file_content = b'Sample File Content'

        mocked_response = MagicMock()
        mocked_response.read.return_value = file_content
        mocked_client = MagicMock()
        mocked_client.cat.return_value = mocked_response

        with patch('ipfs_node.client', mocked_client):
            response = self.client.get(f'/get_file/{file_hash}')
            self.assertEqual(response.status_code, 200)
            response_data = json.loads(response.data)
            returned_file_content = response_data['file_content']
            self.assertEqual(returned_file_content, file_content.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
    
    
    # En aquest exemple, s'utilitza la classe FlaskClient de flask.testing per realitzar les sol·licituds HTTP al node d'IPFS durant els tests.

# Els dos mètodes de test test_add_file i test_get_file comproven el comportament de les rutes /add_file i /get_file, respectivament.

# En test_add_file, es simula una sol·licitud POST a /add_file mitjançant un mock de la classe request i s'assegura que la resposta té el codi d'estat correcte. A continuació, es comprova si el fitxer ha estat afegit correctament a IPFS utilitzant el mock del client IPFS.

# En test_get_file, es simula una sol·licitud GET a /get_file/<file_hash> mitjançant un mock del client IPFS. S'assegura que la resposta té el codi d'estat correcte i que el contingut del fitxer obtingut coincideix amb el contingut esperat.

# Per executar els tests, guarda'l en un fitxer, com ara test_ipfs_node.py, i des de la línia de comandes, executa python test_ipfs_node.py. Es mostrarà el resultat dels tests que s'han executat.
