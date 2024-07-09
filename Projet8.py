map = input("Entrez le mot de passe (min 8)")

if len(map) == 0:
    print("Votre mot de passe est trè court")
elif len(map) < 8:
    print("Votre mot de passe est trè court")
elif map.isdigit():
    print("Ton mot de passe contient que des chiffres")
else:
    print("Vérification terminéé")
    