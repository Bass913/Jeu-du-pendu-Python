from donnees import *
from fonctions import *

scores = récupérer_scores()

utilisateur = récupérer_nom_utilisateur()

if utilisateur not in scores.keys():
    scores[utilisateur] = 0

continuer_partie = "o"

while continuer_partie != "n":
    print(f"Joueur {utilisateur}: {scores[utilisateur]} point(s)")
    mot_à_trouver = choisir_mot()
    lettres_trouvées = set()
    mot_trouvé = récupérer_mot_masqué(mot_à_trouver, lettres_trouvées)
    nb_chances = nb_coups
    while mot_à_trouver != mot_trouvé and nb_chances > 0:
        print(f"Mot à trouver {mot_trouvé} (encore {nb_chances} chances)")
        lettre = récupérer_lettre()
        if lettre in lettres_trouvées:
            print("Vous avez déja choisi cette lettre")
        elif lettre in mot_à_trouver:
            print("Bien joué.")
        else:
            nb_chances -= 1
            print("... non, cette lettre ne se trouve pas dans le mot...")
            
        lettres_trouvées.add(lettre)
        
        mot_trouvé = récupérer_mot_masqué(mot_à_trouver, lettres_trouvées)
        
    if mot_à_trouver == mot_trouvé:
        print(f"Félicitations ! Vous avez trouvé le mot {mot_à_trouver}.")
    else: 
        print("PENDU !!! Vous avez perdu.")
        
    scores[utilisateur] += nb_chances
    
    continuer_partie = input("Souhaitez-vous continuer la partie (O/N) ?")
    
    continuer_partie = continuer_partie.lower()
    
enregistrer_scores(scores)
    
print(f"Vous finissez la partie avec {scores[utilisateur]} points.")
    
    
    
    
    
        
            