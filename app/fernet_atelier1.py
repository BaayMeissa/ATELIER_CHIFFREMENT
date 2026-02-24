import os
from cryptography.fernet import Fernet

def charger_cle():
    # Récupère la clé stockée dans le Secret GitHub via la variable d'environnement
    cle = os.getenv("FERNET_KEY")
    if not cle:
        raise ValueError("Erreur : La variable d'environnement FERNET_KEY est absente.")
    return cle.encode()

def encoder_fichier(nom_fichier, texte):
    cle = charger_cle()
    f = Fernet(cle)
    token = f.encrypt(texte.encode())
    with open(nom_fichier, "wb") as fichier:
        fichier.write(token)
    print(f"Fichier {nom_fichier} encodé avec succès.")

def decoder_fichier(nom_fichier):
    cle = charger_cle()
    f = Fernet(cle)
    with open(nom_fichier, "rb") as fichier:
        token = fichier.read()
    texte_clair = f.decrypt(token)
    return texte_clair.decode()

if __name__ == "__main__":
    nom_test = "secret.txt"
    message = "Ceci est un message protégé par un secret GitHub"
    
    # Test de l'encodage
    encoder_fichier(nom_test, message)
    
    # Test du décodage
    resultat = decoder_fichier(nom_test)
    print(f"Message décodé : {resultat}")
