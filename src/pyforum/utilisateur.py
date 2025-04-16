class Utilisateur():

    def __init__(self, id, username, email, password, liste_publications):
        # TODO: Ajouter les autres attributs nécessaires
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.liste_publications = liste_publications

    def __str__(self):
        return f"Utilisateur(id={self.id}, username='{self.username}')"
    
#je teste pour la creation de l'utilisateur du coups change pas en bas stp.
import csv
import os

# Définir le chemin du fichier CSV
chemin_fichier = os.path.join("src", "pyforum", "data", "utilisateurs.csv")

# Créer le dossier data s'il n'existe pas
os.makedirs(os.path.dirname(chemin_fichier), exist_ok=True)

# --- Création d'un utilisateur ---
print("\nCréation d'un utilisateur...")

username = input("Entrez le nom d'utilisateur: ")
email = input("Entrez l'adresse courriel: ")
mot_de_passe = input("Entrez un mot de passe: ")

# Lecture des utilisateurs existants
utilisateurs = []
try:
    with open(chemin_fichier, 'r', newline='', encoding='utf-8') as entree:
        lecteur = csv.DictReader(entree)
        utilisateurs = list(lecteur)
except FileNotFoundError:
    print("Le fichier utilisateurs.csv n'existe pas encore, il sera créé.")

# Générer un ID unique
nouvel_id = f"U{len(utilisateurs) + 1}"

# Créer le dictionnaire utilisateur
utilisateur = {
    "id": nouvel_id,
    "nom_utilisateur": username,
    "email": email,
    "mot_de_passe": mot_de_passe,
    "forums_inscrits": ""  # vide pour l'instant
}

# Ajouter à la liste et sauvegarder
utilisateurs.append(utilisateur)

with open(chemin_fichier, 'w', newline='', encoding='utf-8') as sortie:
    champs = ["id", "nom_utilisateur", "email", "mot_de_passe", "forums_inscrits"]
    ecrivain = csv.DictWriter(sortie, fieldnames=champs)
    ecrivain.writeheader()
    ecrivain.writerows(utilisateurs)

# Message final
print(f"\nUtilisateur {username} (ID: {nouvel_id}) ajouté avec succès.")
