import json
import csv
import os
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

        racine = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        self.chemin_data = os.path.join(racine, "data")
        os.makedirs(self.chemin_data, exist_ok=True)

        rejoindre_path = os.path.join(self.chemin_data, "rejoindre_forum.csv")
        if not os.path.exists(rejoindre_path):
            with open(rejoindre_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["id_utilisateur", "nom_utilisateur", "id_forum", "nom_forum"])

        self.charger_donnees()

    def charger_donnees(self):
        try:
            with open(f"{self.chemin_data}/utilisateur.csv", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.utilisateurs = [
                    Utilisateur(int(row["id"]), row["username"], row["courriel"], row["mot_de_passe"])
                    for row in reader
                ]
        except:
            self.utilisateurs = []

        try:
            with open(f"{self.chemin_data}/forum.csv", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.forums = [
                    Forum(int(row["id"]), row["nom"], row["description"])
                    for row in reader
                ]
        except:
            self.forums = []

        try:
            with open(f"{self.chemin_data}/publications.json", "r") as f:
                self.publications = [Publication(**x) for x in json.load(f)]
        except:
            self.publications = []

        try:
            with open(f"{self.chemin_data}/commentaires.json", "r") as f:
                self.commentaires = [Commentaire(**x) for x in json.load(f)]
        except:
            self.commentaires = []

    def sauvegarder_utilisateurs(self):
        with open(f"{self.chemin_data}/utilisateur.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "username", "courriel", "mot_de_passe", "forums"])
            for u in self.utilisateurs:
                noms_forums = [f.nom for f in self.forums if f.id in u.forums]
                writer.writerow([u.id, u.username, u.courriel, u.mot_de_passe, ";".join(noms_forums)])


    def sauvegarder_forums(self):
        with open(f"{self.chemin_data}/forum.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "nom", "description"])
            for forum in self.forums:
                writer.writerow([forum.id, forum.nom, forum.description])

    def sauvegarder(self):
        self.sauvegarder_utilisateurs()
        self.sauvegarder_forums()
        with open(f"{self.chemin_data}/publications.json", "w", encoding="utf-8") as f:
            json.dump([p.__dict__ for p in self.publications], f, ensure_ascii=False, indent=2)
        with open(f"{self.chemin_data}/commentaires.json", "w", encoding="utf-8") as f:
            json.dump([c.__dict__ for c in self.commentaires], f, ensure_ascii=False, indent=2)

    def creer_utilisateur(self, username, courriel, mot_de_passe):
        if username in [u.username for u in self.utilisateurs]:
            print("Nom d'utilisateur déjà pris.")
            return
        new_id = len(self.utilisateurs) + 1
        u = Utilisateur(new_id, username, courriel, mot_de_passe)
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
        self.sauvegarder()
        print(f"Publication créée: {p}")

    def creer_commentaire(self, contenu, id_auteur, id_publication):
        new_id = len(self.commentaires) + 1
        c = Commentaire(new_id, id_auteur, contenu, id_publication)
        self.commentaires.append(c)
        self.sauvegarder()
        print(f"Commentaire ajouté: {c}")

    def joindre_forum(self, username, forum_nom):
        u = self.obtenir_utilisateur_par_nom(username)
        f = self.obtenir_forum_par_nom(forum_nom)

        if u and f:
            u.rejoindre_forum(f.id)

            with open(os.path.join(self.chemin_data, "rejoindre_forum.csv"), "a", newline="") as f_join:
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