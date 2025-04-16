class Utilisateur():

    def __init__(self, id, username):
        # TODO: Ajouter les autres attributs nécessaires
        self.id = id
        self.username = username

    def __str__(self):
        return f"Utilisateur(id={self.id}, username='{self.username}')"
