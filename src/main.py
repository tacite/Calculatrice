import emoji
from dotenv import load_dotenv
import os
from add_op import add_op
from div_op import div_op
from mul_op import mul_op
from sous_op import sous_op
from getpass import getpass

def get_numbers():
    number_1 = float(input('Entrez le nombre 1: '))
    number_2 = float(input('Entrez le nombre 2: '))
    return number_1, number_2

def start_calculator():
    print(emoji.emojize('🫵  🫵  🫵    CALCULATRICE   🫵  🫵  🫵'))
    load_dotenv()
    historique = []
    operations = {'1': add_op, '2': sous_op, '3': mul_op, '4': div_op}
    operators = {'1': '+', '2': '-', '3':'*', '4':'/'}
    if getpass('Rentrez votre mot de passe pour utiliser la calculatrice\n') != os.environ['MOT_DE_PASSE']:
        quit()
    print("Menu:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print('4. Division')

    while True:
        choice = input("Entrez votre choix (1 - 2 - 3 - 4 - <exit for exit> - <history for history) :")
        if choice == 'exit':
            break
        elif choice == "history":
            for calcul in historique:
                print(calcul)
        elif choice in ('1', '2', '3', '4'):
            a, b = get_numbers()
            result = operations[choice](a, b)
            historique.append(f'{a} {operators[choice]} {b} = {result}')
            print(f'resultat : {result}')
        else:
            print('Choix invalide')

if __name__ == '__main__':
    start_calculator()