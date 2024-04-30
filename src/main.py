import emoji
from dotenv import load_dotenv
import os
from src.add_op import add_op
from src.div_op import div_op
from src.mul_op import mul_op
from src.sous_op import sous_op
from getpass import getpass

class Calculatrice:
    historique = []
    operations = {'1': add_op, '2': sous_op, '3': mul_op, '4': div_op}
    operators = {'1': '+', '2': '-', '3':'*', '4':'/'}
    
    def __init__(self) -> None:
        self.historique = []
    
    
    def get_numbers(self):
        number_1 = float(input('Entrez le nombre 1: '))
        number_2 = float(input('Entrez le nombre 2: '))
        return number_1, number_2

    def start_calculator(self):
        print(emoji.emojize('🫵  🫵  🫵    CALCULATRICE   🫵  🫵  🫵'))
        load_dotenv()
#        if getpass('Rentrez votre mot de passe pour utiliser la calculatrice\n') != os.environ['MOT_DE_PASSE']:
 #           quit()
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
                for calcul in self.historique:
                    print(calcul)
            elif choice in ('1', '2', '3', '4'):
                a, b = self.get_numbers()
                result = self.operations[choice](a, b)
                self.historique.append(f'{a} {self.operators[choice]} {b} = {result}')
                print(f'resultat : {result}')
            else:
                print('Choix invalide')