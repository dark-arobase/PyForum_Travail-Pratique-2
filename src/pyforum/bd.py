from pyforum.utilisateur import Utilisateur


class BD:
    def __init__(self):
        self.utilisateurs: list[Utilisateur] = []
        self.forums = []
        self.publications = []
        self.commentaires = []
        self.utilisateurs_forums = {}
        print("Base de données initialisée.")

    def creer_utilisateur(self, username: str) -> Utilisateur:
        #                       ^^^^^^^^^^^^^^
        #            # TODO:    Vous devez ajouter les autres paramètres requis

        # Vérifier si l'utilisateur existe déjà
        if username in [u.username for u in self.utilisateurs]:
            print(f"[Simulé] L'utilisateur {username} existe déjà.")
            return

        # Créer un nouvel identifiant pour l'utilisateur
        new_id = max([u.id for u in self.utilisateurs], default=0) + 1

        # Instancier un nouvel utilisateur et l'ajouter à la liste
        u = Utilisateur(new_id, username)
        self.utilisateurs.append(u)
        print(f"[Simulé] Sauvegarde de l'utilisateur: {u}")

        # Retourner l'utilisateur créé
        return u

    def obtenir_utilisateur_par_nom(self, nom_utilisateur: str):
        for u in self.utilisateurs:
            if u.username == nom_utilisateur:
                return u

    def creer_forum(self, nom):
        #                ^^^^^^
        #                Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour créer un forum
        pass

    def creer_publication(self, publication):
        #                       ^^^^^^^^^^^
        #                       Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour créer une publication
        pass

    def creer_commentaire(self, commentaire):
        #                       ^^^^^^^^^^^
        #                       Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour créer un commentaire
        pass

    def obtenir_forum_par_nom(self, nom_forum):
        # TODO: Implanter la logique pour chercher un forum à partir de son nom
        pass

    def obtenir_publication_par_titre(self, titre_publication):
        # TODO: Implanter la logique pour chercher une publication à partir de son titre
        pass

    def mettre_a_jour_forum(self, forum):
        #                         ^^^^^^
        #                         Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour mettre à jour le forum et retourner le forum mis à jour
        pass
