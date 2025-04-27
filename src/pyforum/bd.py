import json
import csv
from utilisateur import Utilisateur
from forum import Forum
from publication import Publication
from commentaire import Commentaire
from datetime import datetime

class BD:
    def __init__(self):
        self.utilisateurs = []
        self.forums = []
        self.publications = []
        self.commentaires = []

        with open("data/rejoindre_forum.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id_utilisateur", "nom_utilisateur", "id_forum", "nom_forum"])

        self.charger_donnees()

    def charger_donnees(self):
        try:
            with open("data/forum.csv", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.forums = []
                for row in reader:
                    forum = Forum(int(row["id"]), row["nom"], row["description"])
                    if "publications" in row and row["publications"]:
                        forum.publications = list(map(int, row["publications"].split(";")))
                    self.forums.append(forum)
        except:
            self.forums = []

        try:
            with open("data/utilisateur.csv", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.utilisateurs = [
                    Utilisateur(int(row["id"]), row["username"], row["courriel"], row["mot_de_passe"], row["forums"].split(";") if row["forums"] else [])
                    for row in reader
                ]
        except:
            self.utilisateurs = []

        try:
            
            with open("data/publications.json", "r", encoding="utf-8") as f:
                    publications_data = json.load(f)
                    self.publications = []
            for pub_data in publications_data:
                     p = Publication(
                    pub_data["id"],
                    pub_data["titre"],
                    pub_data["contenu"],
                    pub_data["date_creation"],
                    pub_data["id_auteur"],
                    pub_data["id_forum"]
            )
            p.commentaires = pub_data.get("commentaires", [])
            self.publications.append(p)
        except:
            self.publications = []

        try:
            with open("data/commentaires.json", "r", encoding="utf-8") as f:
                self.commentaires = [Commentaire(**x) for x in json.load(f)]
        except:
            self.commentaires = []

    def sauvegarder_utilisateurs(self):
        with open("data/utilisateur.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "username", "courriel", "mot_de_passe", "forums"])
            for u in self.utilisateurs:
                noms_forums = [f.nom for f in self.forums if f.id in u.forums]
                writer.writerow([u.id, u.username, u.courriel, u.mot_de_passe, ";".join(noms_forums)])

    def sauvegarder_forums(self):
        with open("data/forum.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "nom", "description", "publications"])
            for forum in self.forums:
                publications_str = ";".join(str(pub_id) for pub_id in forum.publications) 
                writer.writerow([forum.id, forum.nom, forum.description, publications_str])
    def sauvegarder(self):
        self.sauvegarder_utilisateurs()
        self.sauvegarder_forums()

        publications_a_sauver = []
        for p in self.publications:
            pub_data = {
                "id": p.id,
                "titre": p.titre,
                "contenu": p.contenu,
                "date_creation": p.date_creation,
                "id_auteur": p.id_auteur,
                "id_forum": p.id_forum,
                "commentaires": [
                    next((c.contenu for c in self.commentaires if c.id == id_commentaire), "")
                    for id_commentaire in p.commentaires
                ]
            }
            publications_a_sauver.append(pub_data)

        with open("data/publications.json", "w", encoding="utf-8") as f:
            json.dump(publications_a_sauver, f, ensure_ascii=False, indent=2)

        with open("data/commentaires.json", "w", encoding="utf-8") as f:
            json.dump([c.__dict__ for c in self.commentaires], f, ensure_ascii=False, indent=2)

    def creer_utilisateur(self, username, courriel, mot_de_passe):
        if username in [u.username for u in self.utilisateurs]:
            print("Nom d'utilisateur déjà pris.")
            return
        new_id = len(self.utilisateurs) + 1
        u = Utilisateur(new_id, username, courriel, mot_de_passe,[])
        self.utilisateurs.append(u)
        self.sauvegarder()
        print(f"Utilisateur créé: {u}")

    def creer_forum(self, nom, description=""):
        if nom in [f.nom for f in self.forums]:
            print("Nom du forum déjà pris.")
            return
        new_id = len(self.forums) + 1
        f = Forum(new_id, nom, description)
        self.forums.append(f)
        self.sauvegarder()
        print(f"Forum créé: {f}")

    def creer_publication(self, titre, contenu, id_auteur, id_forum):
        new_id = len(self.publications) + 1
        date = datetime.now().isoformat()
        p = Publication(new_id, titre, contenu, date, id_auteur, id_forum)
        self.publications.append(p)

        forum = self.obtenir_forum_par_id(id_forum)
        if forum:
            forum.publications.append(p.id)

        self.sauvegarder()
        print(f"Publication créée: {p}")

    def creer_commentaire(self, contenu, id_auteur, id_publication):
        new_id = len(self.commentaires) + 1
        c = Commentaire(new_id, id_auteur, contenu, id_publication)
        self.commentaires.append(c)

        publication = self.obtenir_publication_par_id(id_publication)
        if publication:
            publication.commentaires.append(c.id)

        
        self.sauvegarder()
        print(f"Commentaire ajouté: {c}")


    def joindre_forum(self, username, forum_nom):
        u = self.obtenir_utilisateur_par_nom(username)
        f = self.obtenir_forum_par_nom(forum_nom)

        if u and f:
            u.rejoindre_forum(f.id)
            with open("data/rejoindre_forum.csv", "a", newline="") as f_join:
                writer = csv.writer(f_join)
                writer.writerow([u.id, u.username, f.id, f.nom])
            self.sauvegarder()
            print(f"{username} a rejoint le forum {forum_nom}.")
        else:
            print("Utilisateur ou forum introuvable.")

    def obtenir_utilisateur_par_nom(self, nom_utilisateur):
        return next((u for u in self.utilisateurs if u.username == nom_utilisateur), None)

    def obtenir_forum_par_nom(self, nom_forum):
        return next((f for f in self.forums if f.nom == nom_forum), None)

    def obtenir_forum_par_id(self, id_forum):
        return next((f for f in self.forums if f.id == id_forum), None)

    def obtenir_publication_par_id(self, id_publication):
        return next((p for p in self.publications if p.id == id_publication), None)
