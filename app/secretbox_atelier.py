import os
import nacl.secret
import nacl.utils
from nacl.encoding import Base64Encoder

def charger_cle():
    # Récupération du secret GitHub (stocké en Base64 pour PyNaCl)
    cle_brute = os.getenv("FERNET_KEY") # On réutilise le même nom de secret
    if not cle_brute:
        raise ValueError("Secret FERNET_KEY manquant dans l'environnement")
    
    # La clé doit faire 32 octets pour SecretBox
    # On l'encode ou on la décode selon le format stocké
    return cle_brute.encode()[:32]

def executer_secretbox():
    cle = charger_cle()
    box = nacl.secret.SecretBox(cle)

    # 1. Chiffrement
    message = "Message ultra-sécurisé avec PyNaCl"
    # SecretBox génère automatiquement un 'nonce' (nombre à usage unique)
    chiffre = box.encrypt(message.encode())
    
    print(f"Message chiffré (octets) : {chiffre}")

    # 2. Déchiffrement
    message_clair = box.decrypt(chiffre)
    print(f"Message déchiffré : {message_clair.decode()}")

if __name__ == "__main__":
    try:
        executer_secretbox()
    except Exception as e:
        print(f"Erreur : {e}")
