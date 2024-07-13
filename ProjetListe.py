import sys
import os

print("BIENVENU SUR L'enregistrement du produit\n")

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

LISTE = []

MENU = """Choisissez entre le menu ci-dessous pour effectuer les opération 👇:
1. Ajouter un seul produit
2. Afficher tous les produits existants
3. Retirer ou supprimer le produit
4. Vider le stock
5. Ajouter plusieurs produit
6. Quitter
Tapez votre choix :👇\n 
"""

CHOIX_MENU = ("1", "2", "3", "4", "5", "6")

devrait_continuer = True
while devrait_continuer:
    user_choice = ""
    while user_choice not in CHOIX_MENU:
        user_choice = input(MENU)
        if user_choice not in CHOIX_MENU:
            print("Choix invalide...\n")
            clear()
    
    if user_choice == "1":
        item = input("Entrez l'element à ajouter dans le stock: \n")
        LISTE.append(item)
        print(f"Le produit {item} a été ajouté succès\n")
        clear()
    elif user_choice == "2":
        if LISTE:
            print("Voici les produits disponible 👇:\n")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("Le stock est vide")
            clear()

    elif user_choice == "3":
        item = input("Entrez le produit à supprimer: \n")
        if item in LISTE:
            LISTE.remove(item)
            print(f"Le produit {item} a été supprimer du stock\n")
            clear()
        else:
            print(f"Le produit {item} n'existe pas dans le stock\n")
    elif user_choice == "4":
        verifier = input("Voulez-vous vider le stock ? 'oui' ou 'non' \n")
        if verifier == "oui":
            LISTE.clear()
            clear()
        else:
            if LISTE:
                print("Voici les produits disponible 👇:\n")
                for i, item in enumerate(LISTE, 1):
                    print(f"{i}. {item}")
    elif user_choice == "5":
        item = input("Ajouter plusieurs produits\n")
        LISTE.extend([item])
        clear()
        print("Les produits a été ajouté avec succès\n")
    elif user_choice == "6":
        print("Bonne journée")
        sys.exit()
    else:
        print("-" * 5)
