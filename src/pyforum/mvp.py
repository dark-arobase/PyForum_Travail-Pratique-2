from time import sleep
from bd import BD

def afficher_menu():
    print("\n---- Menu ----")
    print("1. Créer un utilisateur")
    print("2. Créer un forum")
    print("3. Créer une publication")
    print("4. Ajouter un commentaire à une publication")
    print("5. Joindre un forum")
    print("6. Quitter")

def main():
    bd = BD()
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-6): ")

        if choix == '1':
            username = input("Nom d'utilisateur: ")
            courriel = input("Courriel: ")
            mot_de_passe = input("Mot de passe: ")
            bd.creer_utilisateur(username, courriel, mot_de_passe)

        elif choix == '2':
            nom = input("Nom du forum: ")
            desc = input("Description (facultatif): ")
            bd.creer_forum(nom, desc)

        elif choix == '3':
            titre = input("Titre: ")
            contenu = input("Contenu: ")
            auteur = input("Nom d'utilisateur de l'auteur: ")
            forum = input("Nom du forum: ")
            u = bd.obtenir_utilisateur_par_nom(auteur)
            f = bd.obtenir_forum_par_nom(forum)
            if u and f:
                bd.creer_publication(titre, contenu, u.id, f.id)
            else:
                print("Auteur ou forum introuvable.")

        elif choix == '4':
            contenu = input("Contenu du commentaire: ")
            auteur = input("Nom d'utilisateur de l'auteur: ")
            titre_pub = input("Titre de la publication: ")
            u = bd.obtenir_utilisateur_par_nom(auteur)
            p = next((p for p in bd.publications if p.titre == titre_pub), None)
            if u and p:
                bd.creer_commentaire(contenu, u.id, p.id)
            else:
                print("Auteur ou publication introuvable.")

        elif choix == '5':
            utilisateur = input("Nom d'utilisateur: ")
            forum = input("Nom du forum à joindre: ")
            bd.joindre_forum(utilisateur, forum)

        elif choix == '6':
            print("\nMerci d'avoir utilisé PyForum. À bientôt!")
            break
        else:
            print("Option invalide. Veuillez essayer à nouveau.")

        sleep(1)