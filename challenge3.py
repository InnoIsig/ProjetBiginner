def est_bisextile(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def jours_dans_mois(annee, Mois):
    Mois_jour = [31, 28, 31, 30, 31, 30, 31, 30, 31]
    if Mois == 2 and est_bisextile(annee):
        return 29
    else:
        return Mois_jour[Mois - 1]
Annee = int(input("Entrez l'année "))
Mois = int(input("Entrez le mois "))
Jour = jours_dans_mois(Annee, Mois)

print(Jour)

# def my_function(a):
#     if a < 40:
#         return
#         print("Terrible")
#     if a < 80:
#         return "Pass"
#     else:
#         return "Great"
# print(my_function(25))

# def outer_function(a, b):
#     def inner_function(c, d):
#         return c + d
#     return inner_function(a, b)
 
# result = outer_function(5, 10)
# print(result)

# def add(n1, n2):
#   return n1 + n2
 
# def subtract(n1, n2):
#   return n1 - n2
 
# def multiply(n1, n2):
#   return n1 * n2
 
# def divide(n1, n2):
#   return n1 / n2
 
# print(add(2, multiply(5, divide(8, 4))))
