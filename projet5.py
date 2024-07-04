print("Application Vodacom\n")

Utilisateur = input("Entrez le code M-pesa pour vérifier la balance: ")
if Utilisateur == "1122":
    MENU1 = input("""Veuillez Selectionner
    1. Compte M-pesa USD
    2. Compte M-pesa FC
    3. Inviter un proche
    4. Balence Rallonge (gratuit)
    5. Compte Bonus
    \n""")
    if MENU1 == "1":
        verification = input("annuler ou envoyer ").lower()
        if verification == "envoyer":
            compte_USD = input("""Compte M-pesa USD
            1. Envoi Argent
            2. Achat crédit ou Forfaits
            3. Retirer du cash
            4. Services Financiers
            5. Mes Paiements
            6. Bureau d'echange
            7. Service Compte
            8. Retour
            """)
            if compte_USD == "1":
                verification = input("annuler ou envoyer ").lower()
                if verification == "envoyer":
                    Envoi = input("""
                    1. Envoi USD en Fc
                    2. Envoi sans frais de retrait
                    3. Envoi + frais de retrait
                    4. Envoi a la banque
                    5. Envoi-Autres reseaux
                    6. Forfaits Envoi
                    7. Affaires Entre Anis
                    """)
                    
                else:
                    print("Demande annuler")
        else:
            print("Demande annuler")
            
    elif MENU1 == "2":
        verification = input("annuler ou envoyer ").lower()
        if verification == "envoyer":
            compte_USD = input("""Compte M-pesa CDF
            1. Envoi Argent
            2. Achat crédit ou Forfaits
            3. Retirer du cash
            4. Services Financiers
            5. Mes Paiements
            6. Bureau d'echange
            7. Service Compte
            8. Retour
            """)
        else:
            print("Demande annuler")
else:
    print("Code invalide")

            
    # choix_utilisateur = input("1 2 3 4 5")
    # verification = input("annuler ou envoyer").lower()
    # if ValueError == "envoyer":

    
