## Clonar el Repositori: Clona el repositori del projecte des de GitHub utilitzant la comanda següent:

git clone https://github.com/YourUsername/YourRepository.git


## Crear un Entorn Virtual: Es recomana utilitzar un entorn virtual per a mantenir les dependències del projecte aïllades. Navega fins al directori del projecte i crea un entorn virtual:

cd YourRepository
python -m venv venv


## Activar l'Entorn Virtual: Activa l'entorn virtual per a utilitzar-lo a la teva terminal o consola:

En Windows: venv\Scripts\activate

En MacOS/Linux: source venv/bin/activate


## Instal·lar les Dependències: Executa la següent comanda per a instal·lar les dependències del projecte utilitzant el fitxer requirements.txt:

pip install -r requirements.txt


## Configurar l'Aplicació Edita el fitxer de configuració config.py per a adaptar-lo a les teves necessitats.

#Executar l'Aplicació: Ara que tot està configurat, pots executar l'aplicació amb la següent comanda:

python app.py

L'aplicació s'iniciarà i estarà disponible a l'adreça http://localhost:5000.

## Finalitzar: L'aplicació ha estat instal·lada i s'ha iniciat correctament. Ara pots interactuar amb ella mitjançant l'adreça local indicada anteriorment.
