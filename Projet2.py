print("BIENVENU SUR MON PROJET 2\n")

taille = int(input("Entrez ta taille en cm 👇\n"))
poids = int(input("Entrez ton poid en kg 👇\n"))
facture = 0

if taille >= 120 and poids >= 70:
    print("Premier test reçu")
    age = int(input("Entrez ton age 👇\n"))
    if age < 30:
        facture = 25
        print("Tu payes $25")
    elif age >= 30 and age < 40:
        facture = 35
        print("Tu payes $35")
    elif age >= 40 and age < 55:
        facture = 45
        print("Tu payes $45")
    elif age >= 55 and age < 65:
        facture = 60
        print("Tu payes $60")
    else:
        facture = 100
        print("Tu payes $100")
    photo = input('Voulez vous ajouter une photo ? "Oui" ou "Non" 👇\n')
    if photo == "Oui":
        facture += 5
    else:
        facture -= 3
    print(f"La facture à payer est ${facture}")
else:
    print("Test échoué. Tu dois beaucoup t'entrenners")

