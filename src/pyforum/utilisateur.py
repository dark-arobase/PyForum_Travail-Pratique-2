class Utilisateur:
    # Constructeur de la classe Utilisateur
    def __init__(self, id, username, courriel, mot_de_passe, liste_forums=None):
        self.id = id
        self.username = username
        self.courriel = courriel
        self.mot_de_passe = mot_de_passe
        self.forums = liste_forums if liste_forums is not None else []
    # Méthode spéciale pour afficher une représentation lisible de l'objet
    def __str__(self):
        return f"Utilisateur({self.id}, {self.username})"
    # Méthode pour permettre à l'utilisateur de rejoindre un forum
    def rejoindre_forum(self, forum_id):
        if forum_id not in self.forums:
            self.forums.append(forum_id)