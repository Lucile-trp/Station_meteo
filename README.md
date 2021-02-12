# ZEUS API



**PROJET CUBES**
---

Description :



Par :

Mariam EL-ALLALI
Hugo DOURLEN
Grégory LEBLOND
Lucile TRIPIER



## LIENS UTILES 

```
Pour accéder à la documentation de l'api : localhost:5000/api OU http://zeus.fr/api

Pour accéder au site web : localhost:5001

```


## INSTALLATION ET CONFIGURATION SERVEUR 
Démarche à suivre pour une nouvelle installation

```
Configuration du RASPBERRY (après connexion en SSH)

apt update -y // Mise à jour du système
apt upgrade -y // Mise à jour du système
apt install git // Installation de git
apt install python3-pip // installation de pip 
apt install mariadb-server // Installation du SGBDR
mysql_secure_installation // Sécurisation de la Base de Données

```
### Récupération du respository GIT
git clone https://github.com/Lucile-trp/Station_meteo.git // clonage du dépôt github

### installationdes dépendances de L'API
```
cd falsk-api/project // Déplacement dans le fichier API 
pip3 install requirements.txt // Installation des dépendances
```
### Créer l'utilisateur 'zeus' dans la bdd, lui donner tout les droits sur la base station_meteo.
```
mysql -u zeus -p station_meteo < db_schema.sql // Nourrir la base de données.

python3 main.py // Mise en route de l'API
```

## INSTALLATION DU CAPTEUR ESP8266
### Installation de esptool
```
//installation de esptool sur un système linux
sudo apt install esptool
//installation via python3
pip3 install esptools
```
### Installation de l'IDE
Installer Thonny
### Ajouter un nouveau gestionnaire de board dans Thonny
File -> Preferences -> URl de gestionnaire de cartes supplémentaires
### Télécharger la librairie ESP8266
Type de carte -> ESP8266 -> Generic ESP8266
### Créer le fichier si7021.py
### Importer le fichier si7021.py dans boot.py

## FRONT

```
Remplacer tout les 'IP:mbp-de-lucile' par :
-   Soit l'adresse IP du Raspberry si vous hébergez la Web App sur un autre serveur
        (requis: le serveur doit être connecté au même wifi que le Raspberry et le capteur)
-   Soit localhost ou 127.0.0.1 si vous hébergez sur le Raspberry Pi

```
