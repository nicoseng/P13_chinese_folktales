# P13_chinese_folktales

# Projet P13 : Projet final : prêt pour le feu d'artifice !

Code source : https://github.com/nicoseng/P13_chinese_folktales
Programme rédigé sous Python3. Projet sous Virtual Env et Git 
Adresse de l’application web déployé : http://206.189.127.39/

# I°) Téléchargez le projet sur votre répertoire local

```
https://github.com/nicoseng/P13_chinese_folktales.git
```

# II°) Préparez l’environnement virtuel de développement

1.  Installez un environnement virtuel de développement depuis votre terminal. (python3 –m venv venv) ;
2.  Activez l’environnement virtuel en tapant selon votre situation :
- Pour Unix/MacOS :  
```
source venv/bin/activate
```
- Pour Windows : 
```
venv\Scripts\activate.bat
```

Une mention (venv) s’affiche à gauche de votre console indiquant la bonne activation de votre environnement virtuel.

# III°) Installez les dépendances du projet

```
pip install -r requirements.txt
```
# IV°) Ajoutez les données dans l'application

Dans le terminal, entrez la commande python manage.py insert_data. 
Cette commande permet d'ajouter les données nécessaires afin pouvoir profiter des histoires dans le site web.

# V°) Gérez l'application depuis django admin

Dans votre terminal, créez un super utilisateur (superuser) permet de pouvoir gérer votre application via une fenêtre d'administration Django. Pour ce faire, taper la commande suivante :
```
python manage.py createsuperuser
```
puis suivre les instructions fournies par la suite (username, password, etc.) 

Rendez-vous dans http://206.189.127.39/admin afin de pouvoir vous connecter avec votre username et votre password nouvellement créées.