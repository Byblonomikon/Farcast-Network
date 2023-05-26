from setuptools import setup, find_packages

setup(
    name='nom-del-teu-projecte',
    version='1.0.0',
    author='El teu nom',
    author_email='elteuemail@example.com',
    description='Descripció del teu projecte',
    packages=find_packages(),
    install_requires=[
        'Flask==2.1.0',
        'cryptography==3.4.7',
        'ipfshttpclient==0.8.0',
        'pytest==6.2.4',
        'pysha3==1.0.2'
    ],
    entry_points={
        'console_scripts': [
            'nom-del-teu-script=nom_del_modul:metode_principal',
        ],
    },
)


# Assegura't de canviar els valors com nom-del-teu-projecte, El teu nom, elteuemail@example.com, Descripció del teu projecte, nom-del-teu-script i nom_del_modul:metode_principal perquè coincideixin amb les dades del teu projecte.

# Aquest setup.py defineix el nom del projecte, la versió, l'autor, l'email, la descripció, les llibreries requerides i l'entrada dels scripts en el teu projecte. Pots afegir altres opcions o metadades segons les teves necessitats.

# Guarda aquest contingut en un fitxer anomenat setup.py al directori principal del teu projecte. Això permetrà que pip i altres eines de distribució de paquets puguin instal·lar i distribuir correctament el teu projecte.
