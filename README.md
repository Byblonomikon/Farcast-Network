# Document Organization and Management Software

This project aims to develop a mobile app and computer software that facilitates the organization of digital documentation for users. The primary objective of this software is to classify and digitize documents of interest to the user, which may not necessarily be within the literary or academic spectrum. These documents are considered personal and private, such as certificates, academic titles, employment contracts, rental agreements, and more. As public administration increasingly transitions to digital formats, there is a need to have information under control and prevent loss due to computer or system errors.

The idea behind this project is to analyze existing similar projects in the market and propose improvements, with a particular focus on handling sensitive data, whether personal or academic. To achieve this, distributed ledger technology (DLT) or blockchain will be applied for storing the information. This approach ensures the permanent availability of data from any location while guaranteeing immutability through decentralization of information control.

The project will consist of several phases. Initially, an analysis of the current state of the topic will be conducted, including studying various existing similar projects, identifying their strengths and weaknesses. Subsequently, the functionalities and architecture of the software will be explained, serving as the core of the project. The application's operation will be described, involving different elements that form the blockchain and IPFS ecosystem.

## Features

+ Document classification and organization
+ Digitization of personal and private documents
+ Secure storage using distributed ledger technology
+ Availability of data from any location
+ Guaranteed immutability of information
+ Robust handling of sensitive data

The resulting application will have the following basic functionalities:

1. **Storage System**: Utilizes IPFS for encrypted storage of various file types, ensuring immutability and permanence to mitigate information loss risks.

2. **Document Creation Accreditation**: Includes a tool to register document creation information, such as creation date and author, using digital signatures to ensure authenticity. Blockchain integration verifies authorized access and prevents unauthorized distribution.

3. **Sharing and Access Management**: Allows defining conditions for granting permissions, including temporal limitations, copy restrictions, and permission delegation. Users can control access to specific digital content through the application's interaction.

4. **Digital Testament**: Introduces the concept of a digital testament, addressing the need for proper transmission of digital knowledge in society. This functionality ensures the preservation and transfer of valuable digital assets.

These functionalities enhance the application's capabilities for efficient document organization, secure storage, authorized access control, and safeguarding digital legacies.

## Architecture

The software architecture follows a client-server model, with the client component available as a mobile app and computer software. The server component incorporates blockchain technology for distributed storage and IPFS (InterPlanetary File System) for decentralized file management. The integration of these elements ensures data security, availability, and immutability.

+ **Nodes**: Initially, it will be necessary to establish which nodes will be part of the network. It is crucial for these nodes to have a high level of trust. The project will propose the utilization of public library computers as potential nodes. The current project will work with the Round Robin consensus model, a Proof of Trust approach where nodes have a specific time window to randomly publish a block. This model ensures that all nodes contribute to block creation, avoiding concentration of block production by a single node as seen in Proof of Stake or Proof of Work models.

However, this model does not require significant computational power. It would be beneficial to involve the public administration in establishing the network of nodes to ensure minimal possibility of malicious nodes attempting to monopolize block writing through the creation of numerous nodes. Since this network does not involve digital assets in the form of cryptocurrencies and personal documents sent to IPFS are encrypted, the risk of malicious nodes becomes almost irrelevant, and this possibility can be easily dismissed.

The current project will operate on a permissioned network since the sensitivity of the information to be safeguarded requires a high level of privacy and the user's ability to choose with whom they want to share this data, whether medical, financial, legal, etc. This necessitates a certain level of trust among the network participants.

The project will define Full Nodes for writing, which will consist of the public library network, and validation nodes or Light Nodes, which can be installed by DApp users to reinforce the network's functionality and robustness


+ **Encryption Software**: To encrypt files before including them in IPFS, asymmetric encryption software will be used. VeraCrypt will be employed for encryption. VeraCrypt is an open-source software compatible with Linux, macOS, and Microsoft Windows, allowing file encryption.

+ **Digital Signature Software**: To ensure the authorship of documents included in IPFS, digital signature software will be used. PandaDoc, one of the most popular electronic signature services, will be utilized for this purpose. The software enables the integration of electronic document signing functionality into the developed application through interaction with the PandaDoc API.

+ **IPFS**: In IPFS, digitally signed and encrypted files will be included. The resulting hash will be stored in the Blockchain.

+ **Blockchain**: The Ethereum blockchain will be utilized, and the following information will be included:

+ **File creation information**: When a file is added to IPFS, the Blockchain will record the file's creation information (date, author, digital signature) and its corresponding hash. Metadata related to the file content will also be included to facilitate searchability by other users.

+ **Access management information**: The Blockchain will maintain a registry of activated access permissions, which will be managed through user interactions within the application.

To set up the Blockchain, Geth will be used. Geth is a command-line interface responsible for communication and information exchange with other nodes in the Ethereum network.

+ **Smart Contract for Digital Testament**: Users will have the ability to designate individuals who will inherit custody and access rights to their digital assets after their death, similar to a testament. This functionality will be implemented through a Smart Contract once the user's death is verified. Several potential models can be considered, which would need to be defined in collaboration with the application developer.

One possible model involves the author of the testament specifying trusted parties, such as family or friends, responsible for certifying their death. However, this model raises concerns about the potential for malicious use by users. To address this, requirements for unanimous confirmation of death could be established to enhance the reliability of the model.

## Installation

To install and run the software, follow these steps:

+ Clone the repository to your local machine.
+ Install the required dependencies and libraries.
+ Configure the database connection and security settings.
+ Build and compile the software.
+ Start the application.


## Usage

Once the software is up and running, users can perform the following actions:

+ Register an account and log in.
+ Upload and classify documents.
+ View and search for stored documents.
+ Access documents from any location.
+ Update or delete documents when necessary.




## Contributing

Contributions to this project are welcome. If you have suggestions for improvements or would like to report any issues, please submit a pull request or open an issue in the project repository.


### License




### Acknowledgments




### Contact

For any inquiries or further information about this project, please contact:

