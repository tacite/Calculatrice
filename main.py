import emoji
from dotenv import load_dotenv
import os

print(emoji.emojize('🫵  🫵  🫵    CALCULATRICE   🫵  🫵  🫵'))
load_dotenv()
historique = []
if input('Rentrez votre mot de passe pour utiliser la calculatrice\n') != os.environ['MOT_DE_PASSE']:
    quit()

while True:
    print("Menu:")
    print("1. Opération membre 1")
    print("2. Opération membre 2")
    print("3. Opération membre 3")
    print('4. Opération membre 4')
    choice = input("Entrez votre choix (1/2/3/4 <exit for exit>) :")
    match choice:
        case '1':
            # Appel de la fonction pour l'opération du membre 1
            print('operation 1')
        case '2':
            # Appel de la fonction pour l'opération du membre 2
            print('operation 2')
        case '3':
            # Appel de la fonction pour l'opération du membre 3
            print('operation 3')
        case '4':
            # Appel de la fonction pour l'opération du membre 4
            print('operation 4')
        case 'exit':
            # Quitter la boucle
            break
