alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']


def casar(commencez_texte, nombre_decalage, direction_chiffre):
    fin_text = ""

    if direction_chiffre == "decoder":
        nombre_decalage *= -1
    for char in commencez_texte:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position - nombre_decalage
            fin_text += alphabet[new_position]
        else:
            fin_text += char
    print(f"Voici le texte {direction} : {fin_text}")

should_continu = True
while should_continu:
    direction = input("Type 'encoder' to encrypt, type 'decoder' to decrypt:\n")
    text = input("Tapez ton texte ici 👇:\n").lower()
    shift = int(input("Tapez le nombre de textes à décaler 👇:\n"))

    shift = shift % 26

    casar(commencez_texte= text, nombre_decalage= shift, direction_chiffre= direction)

    commencez = input("Tapez 'oui' si vous vous voulez continuer sinon 'non' \n")
    if commencez == "non":
        should_continu = False
        print("Au revoir")





































# def cryptogramme(text_simple, letter_decalage):
#     # une chaine de caractère qui doit recevoir le texte codé
#     cryptogramme = ""
#     #nous voulons connaitre l'index de la lttre que nous passons dans le boucle
#     for letter in text_simple:

#         postion = alphabet.index(letter)
#         new_position = postion + letter_decalage
#         new_letter = alphabet[new_position]

#         #Ici nous ajputer les texte choffré
#         cryptogramme += new_letter
#     print(f"Le texte encodé est : {cryptogramme}")

# def decrypt(cryptogramme, letter_decalage):
#     decryptogramme = ""
#     for letter in cryptogramme:
#         position = alphabet.index(letter)
#         new_position = position - letter_decalage
#         decryptogramme += alphabet[new_position]
#     print(f"le texte a decrypter est : {decryptogramme}")

# if direction == "encode":
#     cryptogramme(text_simple = text, letter_decalage = shift)
# elif direction == "decode":
#     decrypt(cryptogramme= text, letter_decalage= shift)