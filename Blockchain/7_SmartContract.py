pragma solidity ^0.8.0;

contract DocumentRegistry {
    struct Document {
        string title;
        string hashValue;
    }

    mapping(string => Document) private documents;

    event DocumentAdded(string indexed hashValue, string title);

    function addDocument(string memory hashValue, string memory title) public {
        require(bytes(hashValue).length > 0, "Hash value cannot be empty");
        require(bytes(title).length > 0, "Title cannot be empty");
        require(documents[hashValue].hashValue == "", "Document already exists");

        documents[hashValue] = Document(title, hashValue);
        emit DocumentAdded(hashValue, title);
    }

    function getDocument(string memory hashValue) public view returns (string memory title, string memory hash) {
        Document memory doc = documents[hashValue];
        require(bytes(doc.hashValue).length > 0, "Document not found");

        return (doc.title, doc.hashValue);
    }
}


# Aquest contracte té dues funcions principals: addDocument per afegir un document nou i getDocument per obtenir informació sobre un document existent.
# Per a utilitzar aquest contracte, primer hauràs de desplegar-lo a la xarxa Ethereum. Un cop desplegat, utilitzaràs la seva adreça i el seu ABI (interfície d'aplicació binària) en el teu script Python per interactuar amb ell, com ja es mostra a l'exemple anterior.
# Assegura't de provar el teu contracte en un entorn de desenvolupament o de proves abans de desplegar-lo en una xarxa en viu. També assegura't d'entendre els costos associats amb les transaccions de contractes intel·ligents en la xarxa Ethereum.


