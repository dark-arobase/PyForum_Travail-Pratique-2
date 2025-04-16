class Publication():

    def __init__(self, id, titre, contenu,  date_creation, id_auteur, id_forum, liste_commentaires):

        # TODO: Ajouter les autres attributs nécessaires
        self.id = id
        self.titre = titre
        self.contenu = contenu
        self.date_creation = date_creation
        self.id_auteur = id_auteur
        self.id_forum = id_forum
        self.liste_commentaires = liste_commentaires
    
    def __str__(self):
        return f"Publication(id={self.id}, titre='{self.titre}', contenu='{self.contenu}', date_creation='{self.date_creation}', id_auteur='{self.id_auteur}', id_forum='{self.id_forum}')"