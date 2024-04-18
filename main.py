import emoji
from dotenv import load_dotenv
import os
from  soustraction_division import *

def get_numbers():
    number_1 = float(input('Entrez le nombre 1: '))
    number_2 = float(input('Entrez le nombre 2: '))
    return number_1, number_2

def start_calculator():
    print(emoji.emojize('🫵  🫵  🫵    CALCULATRICE   🫵  🫵  🫵'))
    load_dotenv()
    historique = []
    if input('Rentrez votre mot de passe pour utiliser la calculatrice\n') != os.environ['MOT_DE_PASSE']:
        quit()
    print("Menu:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print('4. Division')

    while True:
        choice = input("Entrez votre choix (1 - 2 - 3 - 4 - <exit for exit> - <history for history) :")
        match choice:
            case '1':
                a, b = get_numbers()
                result = add_op(a, b)
                historique.append(f'{a} + {b} = {result}')
                print(result)
            case '2':
                a, b = get_numbers()
                result = sous_op(a, b)
                historique.append(f'{a} - {b} = {result}')
                print(result)
            case '3':
                a, b = get_numbers()
                result = mul_op(a, b)
                historique.append(f'{a} * {b} = {result}')
                print(result)
            case '4':
                a, b = get_numbers()
                if b == 0:
                    print("Erreur division par 0")
                else:
                    result = div_op(a, b)
                    historique.append(f'{a} / {b} = {result}')
                    print(result)
                        
            case 'history':
                for calcul in historique:
                    print(calcul)
            case 'exit':
                break
            
if __name__ == '__main__':
    start_calculator()