while True:
    print("Menu:")
    print("1. Opération membre 1")
    print("2. Opération membre 2")
    print("3. Opération membre 3")
    choice = input("Entrez votre choix (1/2/3) : ")


    if choice == '1':
        # Appel de la fonction pour l'opération du membre 1
        print(operation_membre1(10, 5))
    elif choice == '2':
        # Appel de la fonction pour l'opération du membre 2
        print(operation_membre2(10, 5))
    elif choice == '3':
        # Appel de la fonction pour l'opération du membre 3
        print(operation_membre3(10, 5))
    else:
        print("Choix invalide. Veuillez choisir 1, 2 ou 3.")
