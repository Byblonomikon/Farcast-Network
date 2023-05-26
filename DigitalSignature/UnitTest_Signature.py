import unittest
import os
from cryptography.hazmat.primitives import serialization
from digital_signature import sign_file

class TestDigitalSignature(unittest.TestCase):
    def test_sign_file(self):
        # Rutes als arxius de prova
        private_key_path = "private_key.pem"
        file_path = "fitxer.txt"

        # Genera la signatura digital
        signature = sign_file(private_key_path, file_path)

        # Comprova si la signatura s'ha generat
        self.assertIsNotNone(signature)

        # Comprova si la signatura té la longitud esperada
        self.assertEqual(len(signature), 256)

        # Elimina l'arxiu de prova després de cada execució del test
        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()

    
    #En aquest exemple, s'utilitza la classe unittest.TestCase de la biblioteca unittest per escriure el test. El mètode test_sign_file prova la funció sign_file amb els arxius de prova private_key.pem i fitxer.txt.

# Dins del test, s'assegura que la signatura s'ha generat i no és None. També es comprova si la longitud de la signatura és la longitud esperada (en aquest cas, 256 bytes). Finalment, s'elimina l'arxiu de prova fitxer.txt després de cada execució del test.

# Per executar el test, guarda'l en un fitxer Python com ara test_digital_signature.py i des de la línia de comandes, executa python test_digital_signature.py. Es mostrarà el resultat del test que s'ha executat.
