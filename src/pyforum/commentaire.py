class Commentaire:
    def __init__(self, id, id_auteur, contenu, id_publication):
        self.id = id
        self.id_auteur = id_auteur
        self.contenu = contenu
        self.id_publication = id_publication

    def __str__(self):
        return f"Commentaire({self.id}, auteur={self.id_auteur})"