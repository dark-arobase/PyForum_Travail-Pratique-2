class Publication:
    # Constructeur de la classe Publication
    def __init__(self, id, titre, contenu, date_creation, id_auteur, id_forum):
        self.id = id
        self.titre = titre
        self.contenu = contenu
        self.date_creation = date_creation
        self.id_auteur = id_auteur
        self.id_forum = id_forum
        self.commentaires = []
    # Méthode spéciale pour afficher une représentation lisible de l'objet
    def __str__(self):
        return f"Publication({self.id}, {self.titre})"