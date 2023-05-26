import unittest
from unittest.mock import MagicMock

class TestIPFS(unittest.TestCase):

    def test_ipfs_add_file(self):
        # Mock del mòdul IPFS i de la instància
        ipfs_mock = MagicMock()
        ipfs_module_mock = MagicMock(return_value=ipfs_mock)
        ipfs_module_mock.once = MagicMock()

        with unittest.mock.patch.dict('sys.modules', {'ipfs': ipfs_module_mock}):
            import main  # Fitxer principal amb el codi

            # Mock del resultat de la crida a ipfs.add()
            files_added_mock = MagicMock()
            files_added_mock.cid = MagicMock()
            files_added_mock.cid.toString.return_value = 'Qm123456'
            ipfs_mock.add.return_value = files_added_mock

            # Execució del codi
            main.ipfs.once('ready')()

            # Comprovació dels resultats
            ipfs_mock.add.assert_called_once_with({
                'path': 'nom-del-document.txt',
                'content': MagicMock()
            })
            files_added_mock.cid.toString.assert_called_once()
            self.assertEqual(main.fileHash, 'Qm123456')
            print_output = main.print_output.getvalue().strip()
            self.assertEqual(print_output, "El document s'ha emmagatzemat a l'adreça Qm123456")

if __name__ == '__main__':
    unittest.main()
