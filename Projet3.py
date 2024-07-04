import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
        ______)
        _______)
        _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image_jeux = [rock, paper, scissors]
choix_utilisateur = int(input("Choisissez votre choix entre 0 comme Pièrre, 1 comme Papier, 2 comme Sciseau"))

if choix_utilisateur >= 3 or choix_utilisateur < 0:
    print("Nombre invalide")
else:
    print("Choix utilisateur")
    print(image_jeux[choix_utilisateur])

choix_ordinateur = random.randint(0, 2)
print("choix ordinateur")
print(image_jeux[choix_ordinateur])

if choix_utilisateur == 0 and choix_ordinateur == 2:
    print("T'as gagné")
elif choix_ordinateur == 0 and choix_utilisateur == 2:
    print("T'as perdu")
elif choix_utilisateur > choix_ordinateur:
    print("T'as gagné encore")
elif choix_utilisateur == choix_ordinateur:
    print("Match nul")
elif choix_ordinateur > choix_utilisateur:
    print("T'as perdu")


