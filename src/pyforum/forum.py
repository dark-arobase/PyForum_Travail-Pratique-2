class Forum():

    def __init__(self, id, username, description,liste_publications):
        # TODO: Ajouter les autres attributs nécessaires
        self.id = id
        self.username = username
        self.description = description
        self.liste_publications = liste_publications

    def __str__(self):
        return f"Utilisateur(id={self.id}, username='{self.username}')"
    