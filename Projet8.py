map = input("Entrez le mot de passe (min 8)")

if len(map) == 0:
    print("Votre mot de passe est trè court")
elif len(map) < 8:
    print("Votre mot de passe est trè court")
elif map.isdigit():
    print("Ton mot de passe contient que des chiffres")
else:
    print("Vérification terminéé")
    
    autre = input("Avez-vous besoin d'une autre nouvelle ? oui ou non")
    if autre == "oui":
        print("inscrivez-vous sur notre page cliquez ici 👇")
        print("https://www.msn.com/fr-xl?ocid=wispr&pc=u477")
    else:
        print("Merci pour votre confiance")