class Utilisateur:
    def __init__(self, id, username, courriel, mot_de_passe):
        self.id = id
        self.username = username
        self.courriel = courriel
        self.mot_de_passe = mot_de_passe
        self.forums = []

    def __str__(self):
        return f"Utilisateur({self.id}, {self.username})"

    def rejoindre_forum(self, forum_id):
        if forum_id not in self.forums:
            self.forums.append(forum_id)