import os

def clear():
    # Pour Windows
    # Vérifie le type de système d'exploitation
    if os.name == 'nt': # Si le système d'exploitation est Windows
        os.system('cls') # Exécute la commande 'cls' pour effacer l'écran
    # Pour Mac et Linux (os.name est 'posix')
    else:
        os.system('clear') # Exécute la commande 'clear' pour effacer l'écran

offres = {}
offre_termine = False

def trouver_le_plusGrand_offre(score_offre):
    grand_enchere = 0
    gagant = ""
    #disons que nous avons deux soumissionnaires {"Inno": 345, "David": 464}
    for offre in score_offre:
        montant = score_offre[offre]
        if montant > grand_enchere:
            grand_enchere = montant
            gagant = offre
    print(f"Le gagant est {gagant} avec une offre de ${grand_enchere}")


while not offre_termine:
    nom = input("Entrez votre nom 👇:\n")
    prix = int(input("Entrez le prix 👇: \n$"))
    offres[nom] = prix

    should_continu = input("Y-a-t-il d'autres soumissionnaires ? 'oui' ou 'non' 👇 \n")
    if should_continu == "non":
        offre_termine = True
        trouver_le_plusGrand_offre(offres)
    elif should_continu == "oui":
        clear()

