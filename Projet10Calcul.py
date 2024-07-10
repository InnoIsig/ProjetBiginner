#Importation du module logo2
from logo2 import logo
print(logo)

#fonction addition
def addition(nombre1, nombre2):
    return nombre1 + nombre2

def soustraction(nombre1, nombre2):
    return nombre1 - nombre2

#fonction multiplication
def multiplication(nombre1, nombre2):
    return nombre1 * nombre2

#fonction division
def division(nombre1, nombre2):
    if nombre2 == 0:
        print("Impossible de diviser un nombre par zero")
    else:
        return nombre1 / nombre2

#je cree le dictionnaire
operation ={
    "+": addition,
    "-": soustraction,
    "*": multiplication,
    "/": division
}

nombre_1 = int(input("Entrez le premier nombre\n"))
nombre_2 = int(input("Entrez le deuxieme nombre\n"))

for symbole in operation:
    print(symbole)
operation_symbole = input("Choisissez entre les differents symbole ci-haut: ")

calculation_fonction = operation[operation_symbole]
reponse_1 = calculation_fonction(nombre_1, nombre_2)



print(f"{nombre_1} {operation_symbole} {nombre_2} = {reponse_1}")
continu = input("Voulez-vous continuer à faire l'opération ? 'oui' ou 'non' ")
if continu == "oui":
    nombre_3 = int(input("Entrez le troisieme nombre\n"))
    operation_symbole = input("Choisissez un autre opérateur: ")
    calculation_fonction = operation[operation_symbole]
    reponse_2 = calculation_fonction(calculation_fonction (nombre_1, nombre_2), nombre_3)

    print(f"{reponse_1} {operation_symbole} {nombre_3} = {reponse_2}")
else:
    print("Merci et bonne suite de temps")



