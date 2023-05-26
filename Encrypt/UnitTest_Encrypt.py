import unittest
import json
from flask import Flask
from flask.testing import FlaskClient
from unittest.mock import patch, MagicMock
from hashlib import sha256

from sha256_and_ipfs import app, calculate_sha256

class TestSHA256AndIPFS(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_encrypted_file(self):
        # Mock de la sol·licitud POST
        file_content = b'Sample File Content'
        file_hash = sha256(file_content).hexdigest()

        mocked_file = MagicMock()
        mocked_file.read.return_value = file_content

        with patch('sha256_and_ipfs.request') as mocked_request:
            mocked_request.files = {'file': mocked_file}

            with patch('sha256_and_ipfs.client.add_bytes') as mocked_add_bytes:
                ipfs_file_hash = 'QmTestFileHash'
                mocked_add_bytes.return_value = {'Hash': ipfs_file_hash}

                response = self.client.post('/add_encrypted_file')
                self.assertEqual(response.status_code, 200)
                response_data = json.loads(response.data)
                returned_file_hash = response_data['file_hash']
                returned_ipfs_file_hash = response_data['ipfs_file_hash']

                self.assertEqual(returned_file_hash, file_hash)
                self.assertEqual(returned_ipfs_file_hash, ipfs_file_hash)

    def test_calculate_sha256(self):
        file_content = b'Sample File Content'
        expected_hash = sha256(file_content).hexdigest()

        calculated_hash = calculate_sha256(file_content)

        self.assertEqual(calculated_hash, expected_hash)


if __name__ == '__main__':
    unittest.main()

    
    #En aquest exemple, s'utilitza la classe FlaskClient de flask.testing per realitzar les sol·licituds HTTP durant els tests.

# El mètode de test test_add_encrypted_file comprova el comportament de la ruta /add_encrypted_file. S'utilitzen mocks per simular una sol·licitud POST i l'addició del fitxer a IPFS. Es comprova si la resposta té el codi d'estat correcte i si el resum criptogràfic SHA-256 i el hash del fitxer a IPFS retornats coincideixen amb els valors esperats.

# El mètode de test test_calculate_sha256 comprova la funció calculate_sha256, assegurant que el resum criptogràfic SHA-256 calculat pel fitxer de mostra coincideix amb el valor esperat.

# Per executar els tests, guarda'l en un fitxer, com ara test_sha256_and_ipfs.py, i des de la línia de comandes, executa python test_sha256_and_ipfs.py. Es mostrarà el resultat dels tests que s'han executat.
