"""
Système de Sauvegarde Persistent - Données du Jeu
Sauvegarde et charge la progression du joueur en JSON
"""
import json
import os
from datetime import datetime

class SystemeSauvegarde:
    def __init__(self, dossier_sauvegardes="sauvegardes"):
        self.dossier_sauvegardes = dossier_sauvegardes
        
        # Créer le dossier s'il n'existe pas
        if not os.path.exists(dossier_sauvegardes):
            os.makedirs(dossier_sauvegardes)
    
    def sauvegarder_partie(self, personnage, nom_fichier="partie_principale.json"):
        """Sauvegarde la partie complète du joueur"""
        donnees = {
            "nom_joueur": personnage.nom,
            "niveau": personnage.niveau,
            "experience": personnage.experience,
            "vie": personnage.vie,
            "vie_max": personnage.vie_max,
            "argent": personnage.argent,
            "inventaire": personnage.inventaire,
            "tenue": personnage.tenue,
            "main": personnage.main,
            "position_x": None,  # Sera défini par main
            "position_y": None,  # Sera défini par main
            "date_sauvegarde": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "en_defense": personnage.en_defense,
        }
        
        chemin = os.path.join(self.dossier_sauvegardes, nom_fichier)
        
        try:
            with open(chemin, 'w', encoding='utf-8') as fichier:
                json.dump(donnees, fichier, ensure_ascii=False, indent=2)
            print(f"[OK] Partie sauvegardee: {chemin}")
            return True
        except Exception as erreur:
            print(f"[ERR] Erreur sauvegarde: {erreur}")
            return False
    
    def charger_partie(self, nom_fichier="partie_principale.json"):
        """Charge une partie sauvegardée"""
        chemin = os.path.join(self.dossier_sauvegardes, nom_fichier)
        
        if not os.path.exists(chemin):
            print(f"[WARN] Aucune sauvegarde trouvee: {chemin}")
            return None
        
        try:
            with open(chemin, 'r', encoding='utf-8') as fichier:
                donnees = json.load(fichier)
            print(f"[OK] Partie chargee: {chemin}")
            return donnees
        except Exception as erreur:
            print(f"[ERR] Erreur chargement: {erreur}")
            return None
    
    def sauvegarder_avec_position(self, personnage, pos_x, pos_y, nom_fichier="partie_principale.json"):
        """Sauvegarde avec position du joueur"""
        donnees = {
            "nom_joueur": personnage.nom,
            "niveau": personnage.niveau,
            "experience": personnage.experience,
            "vie": personnage.vie,
            "vie_max": personnage.vie_max,
            "argent": personnage.argent,
            "inventaire": personnage.inventaire,
            "tenue": personnage.tenue,
            "main": personnage.main,
            "position_x": pos_x,
            "position_y": pos_y,
            "date_sauvegarde": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "en_defense": personnage.en_defense,
        }
        
        chemin = os.path.join(self.dossier_sauvegardes, nom_fichier)
        
        try:
            with open(chemin, 'w', encoding='utf-8') as fichier:
                json.dump(donnees, fichier, ensure_ascii=False, indent=2)
            print(f"[OK] Partie sauvegardee avec position ({pos_x}, {pos_y})")
            return True
        except Exception as erreur:
            print(f"[ERR] Erreur sauvegarde: {erreur}")
            return False
    
    def liste_sauvegardes(self):
        """Retourne la liste des sauvegardes disponibles"""
        fichiers = os.listdir(self.dossier_sauvegardes)
        sauvegardes = [f for f in fichiers if f.endswith('.json')]
        return sauvegardes
    
    def supprimer_sauvegarde(self, nom_fichier):
        """Supprime une sauvegarde"""
        chemin = os.path.join(self.dossier_sauvegardes, nom_fichier)
        
        try:
            if os.path.exists(chemin):
                os.remove(chemin)
                print(f"[OK] Sauvegarde supprimee: {nom_fichier}")
                return True
            else:
                print(f"[WARN] Fichier non trouve: {nom_fichier}")
                return False
        except Exception as erreur:
            print(f"[ERR] Erreur suppression: {erreur}")
            return False
