# Script per a publicar el BlockHash resultant del PrivCript en la BlockChain de ComLog.py


from web3 import Web3
from eth_account import Account

# Connecta amb la xarxa Ethereum (Modifica la URL per la teva pròpia xarxa)
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Direcció del contracte intel·ligent
contract_address = "0x123456789..."

# Abi del contracte intel·ligent
contract_abi = [...]  # Inserta l'ABI del teu contracte aquí

def add_hash_to_blockchain(hash_value, document_title, private_key):
    account = Account.privateKeyToAccount(private_key)
    nonce = web3.eth.getTransactionCount(account.address)
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    tx_hash = contract.functions.addDocument(hash_value, document_title).buildTransaction({
        'chainId': 1,  # Ajusta el chainId segons la xarxa Ethereum que utilitzis
        'gas': 1000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': nonce,
    })

    signed_tx = web3.eth.account.signTransaction(tx_hash, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return web3.toHex(tx_hash)

def main():
    # Demana a l'usuari que introdueixi el hash i el títol del document
    hash_value = input("Introdueix el hash del document: ")
    document_title = input("Introdueix el títol del document: ")
    private_key = input("Introdueix la teva clau privada: ")

    # Afegeix el hash i el títol del document a la blockchain
    tx_hash = add_hash_to_blockchain(hash_value, document_title, private_key)
    print("Transacció enviada amb hash:", tx_hash)

if __name__ == "__main__":
    main()

Aquest script utilitza web3.py per interactuar amb una xarxa Ethereum. L'usuari introdueix el hash del document, el títol del document i la seva clau privada. A continuació, el script envia una transacció a un contracte intel·ligent que emmagatzema el hash i el títol del document. Assegura't de modificar les variables contract_address i contract_abi amb les teves pròpies dades de contracte. També, si estàs utilitzant una xarxa diferent de l'entorn de desenvolupament local, assegura't de canviar la URL del proveïdor de Web3.
