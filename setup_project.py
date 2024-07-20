import os
import subprocess

# Nom du projet et de l'application
project_name = 'ExpressionsApp'
app_name = 'expressions'

# Création du projet Django
subprocess.run(['django-admin', 'startproject', project_name])

# Changement du répertoire de travail pour se placer dans le projet Django
os.chdir(project_name)

# Création de l'application Django
subprocess.run(['python', 'manage.py', 'startapp', app_name])

# Création des répertoires pour les templates et les fichiers statiques de l'application
os.makedirs(f'{app_name}/templates/{app_name}', exist_ok=True)
os.makedirs(f'{app_name}/static/{app_name}/css', exist_ok=True)
os.makedirs(f'{app_name}/static/{app_name}/js', exist_ok=True)
os.makedirs(f'{app_name}/static/{app_name}/img', exist_ok=True)

# Création des templates HTML de base
templates = ['base.html', 'main_menu.html', 'learn_expressions.html', 
             'generate_interrogative.html', 'display_meaning.html', 'quiz.html']
for template in templates:
    with open(f'{app_name}/templates/{app_name}/{template}', 'w') as file:
        file.write(f'<!-- {template} -->\n')
        file.write('<h1>Placeholder for ' + template.replace('.html', '') + '</h1>\n')

# Création du fichier requirements.txt
with open('../requirements.txt', 'w') as file:
    file.write('Django\n')

# Affichage d'instructions finales
print("Projet Django créé avec succès.")

