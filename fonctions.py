from pathlib import Path
import pickle
from random import choice

from donnees import *

# Gestion des scores

def récupérer_scores():
    chemin_scores = Path(nom_fichier_scores)
    if chemin_scores.exists():
        with chemin_scores.open("rb") as fichier_scores:
            mon_depickler = pickle.Unpickler(fichier_scores)
            scores = mon_depickler.load()
    else:
        scores = {}
    
    return scores
    
    
def enregistrer_scores(scores):
    with open(nom_fichier_scores, "wb") as fichier_scores:
        mon_pickler = pickle.Pickler(fichier_scores)
        mon_pickler.dump(scores)


def récupérer_nom_utilisateur():
    nom_utilisateur = input("Tapez votre nom : ")
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() or len(nom_utilisateur) < 4:
        print("Ce nom est invalide")
        return récupérer_nom_utilisateur() # On appelle de nouveau la fonction pour avoir un autre nom
    else:
        return nom_utilisateur
        

def récupérer_lettre():
    lettre = input("Tapez une lettre : ")
    lettre = lettre.lower()
    if len(lettre) > 1 or not lettre.isalpha():
        print("Vous n'avez pas saisi une lettre valide.")
        return récupérer_lettre()
    else:
        return lettre
        

def choisir_mot():
    return choice(liste_mots)
    
    
def récupérer_mot_masqué(mot_complet, lettres_trouvées):
    mot_masqué = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvées:
            mot_masqué += lettre
        else:
            mot_masqué += "*"
    
    return mot_masqué