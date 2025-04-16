class Commentaire():

    def __init__(self, id, id_auteur, contenu_commentaire, id_publication):

        # TODO: Ajouter les autres attributs nécessaires
        self.id = id
        self.id_auteur = id_auteur
        self.contenu_commentaire = contenu_commentaire
        self.id_publication = id_publication
    
    def __str__(self):
        return f"Commentaire(id={self.id}, id_auteur='{self.id_auteur}', contenu_commentaire='{self.contenu_commentaire}', id_publication='{self.id_publication}')"
        
        
    def __str__(self):
        return f"Commentaire de {self.auteur_id} : {self.contenu}"