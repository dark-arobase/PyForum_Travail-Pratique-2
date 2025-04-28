class Forum:
    #class forum
    def __init__(self, id, nom, description=""):
        self.id = id
        self.nom = nom
        self.description = description
        self.publications = []

    def __str__(self):
        return f"Forum({self.id}, {self.nom})"