# Discord Bot en Python

Ce projet contient un bot Discord simple écrit en Python utilisant la bibliothèque `discord.py`.

## Prérequis

1. Avant de commencer, assurez-vous d'avoir installé Python 3.8 ou une version supérieure sur votre machine. Vous pouvez vérifier cela en exécutant la commande suivante dans votre terminal :

    ```bash
    python --version

## Instalation

1. Clonez le repo:

    ```bash
    git clone 

2. Créez un environnement virtuel

    ```bash
    python -m venv venv

3. Activez l'environnement virtuel :

    ```bash
    venv\Scripts\activate       # Sur Windows
    source venv/bin/activate    # Sur Mac/Linux 

4. Installez les dépendances :
    Utilisez `pip` pour installer les bibliothèques listées dans le fichier `requirements.txt` :
        
        ```bash
        pip install -r requirements.txt

## Création d'un bot sur Discord

1. Avant de pouvoir utiliser le bot, vous devez en créer un sur Discord :
    - Allez sur [Discord Developer Portal](https://discord.com/developers/applications).
    - Cliquez sur "New Application" et donnez un nom à votre application.
    - Dans l'onglet "Bot", cliquez sur "Add Bot".
    - Copiez le **Token** du bot (vous en aurez besoin pour vous connecter).
   
   
## Utilisation du Bot

1. Ouvrez le fichier Python où le bot est configuré (par exemple `bot.py`).
2. Remplacez `VOTRE_TOKEN_ICI` dans le code par le **Token** que vous avez copié précédemment.
   ```bash
   bot.run('VOTRE_TOKEN_ICI')
3. Exécutez le bot en utilisant la commande suivante :
    ```bash
    python bot.py
4. Le bot devrait maintenant être connecté et prêt à recevoir des commandes sur votre serveur Discord.



## Inviter le Bot sur Votre Serveur Discord

1. Allez dans le [Discord Developer Portal](https://discord.com/developers/applications).
2. Sélectionnez votre application et allez dans l'onglet "OAuth2".
3. Sous "OAuth2 URL Generator", cochez les cases `bot` et les permissions dont vous avez besoin.
4. Utilisez l'URL générée pour inviter votre bot sur votre serveur Discord.