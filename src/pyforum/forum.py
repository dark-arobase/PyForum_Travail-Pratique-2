class Forum:
    # Constructeur de la classe Forum
    def __init__(self, id, nom, description=""):
        self.id = id
        self.nom = nom
        self.description = description
        self.publications = []
    # Méthode spéciale pour afficher une représentation lisible de l'objet
    def __str__(self):
        return f"Forum({self.id}, {self.nom})"