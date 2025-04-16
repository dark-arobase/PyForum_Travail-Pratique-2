# Importation des classes nécessaires
from time import sleep
from pyforum.bd import BD


def afficher_menu():
    """Affiche les options du menu."""
    print("\n---- Menu ----")
    print("1. Créer un utilisateur")
    print("2. Créer un forum")
    print("3. Créer une publication")
    print("4. Ajouter un commentaire à une publication")
    print("5. Joindre un forum")
    print("6. Quitter")


def main():

    # Initialisation de la base de données
    db = BD()

    while True:
        afficher_menu()

        # Demander à l'utilisateur de choisir une option
        choix = input("Choisissez une option (1-6): ")

        if choix == '1':
            # Créer un utilisateur
            print("\nCréation d'un utilisateur...")

            # Voici un exemple trivial de création d'un utilisateur. Vous devez le bonifier,
            # car il ne prend en compte que le nom d'utilisateur.
            username = input("Entrez le nom d'utilisateur: ")
            utilisateur = {'username': username}
            # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur

            # Le **utilisateur est une syntaxe Python pour déballer un dictionnaire.
            # C'est à dire que les clés du dictionnaire deviennent des arguments nommés.
            db.creer_utilisateur(**utilisateur)

        elif choix == '2':
            # Créer un forum
            print("\nCréation d'un forum...")
            # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
            # TODO: Ajouter l'appel à la base de donnée pour créer le forum

        elif choix == '3':
            # Créer une publication
            print("\nCréation d'une publication...")
            # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
            # TODO: Ajouter l'appel à la base de donnée pour créer la publication

        elif choix == '4':
            # Ajouter un commentaire
            print("\nAjouter un commentaire...")
            # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
            # TODO: Ajouter l'appel à la base de donnée pour créer le commentaire

        elif choix == '5':
            # Joindre un forum
            print("\nJoindre un forum...")
            # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
            # TODO: Ajouter les appels à la base de donnée pour ajouter l'utilisateur au forum

        elif choix == '6':
            # Quitter le programme
            print("\nMerci d'avoir utilisé PyForum. À bientôt!")
            break

        else:
            print("Option invalide. Veuillez essayer à nouveau.")

        sleep(1)  # Pause de 1 secondes pour rendre l'interface plus agréable
