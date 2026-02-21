"""
Système de Quêtes Amélioré - Gestion complète
"""
import json
import os

class Quete:
    def __init__(self, nom, description, types_objectifs, objectifs, recompense_argent, quantite_objectifs):
        self.nom = nom
        self.description = description
        self.types_objectifs = types_objectifs
        self.objectifs = {objectif: {"quantite": quantite_objectifs, "etat": "non_commencee", "progression": 0} 
                         for objectif in objectifs}
        self.recompense_argent = recompense_argent
        self.etat = "non_commencee"  # non_commencee, en_cours, completee
        self.date_debut = None
        self.date_fin = None
    
    def demarrer(self):
        """Démarre la quête"""
        self.etat = "en_cours"
        from datetime import datetime
        self.date_debut = datetime.now()
        print(f"[OK] Quete demarree: {self.nom}")
    
    def completer_objectif(self, nom_objectif):
        """Marque un objectif comme complété"""
        if nom_objectif in self.objectifs:
            self.objectifs[nom_objectif]["etat"] = "completee"
            self.objectifs[nom_objectif]["progression"] = self.objectifs[nom_objectif]["quantite"]
            print(f"[OK] Objectif complete: {nom_objectif}")
            
            # Vérifier si toute la quête est complétée
            return self.verifier_completion()
        return False
    
    def augmenter_progression(self, nom_objectif, quantite=1):
        """Augmente la progression d'un objectif"""
        if nom_objectif in self.objectifs:
            obj = self.objectifs[nom_objectif]
            obj["progression"] = min(obj["progression"] + quantite, obj["quantite"])
            
            if obj["progression"] >= obj["quantite"]:
                obj["etat"] = "completee"
            
            return bool(obj["progression"] >= obj["quantite"])
        return False
    
    def verifier_completion(self):
        """Vérifie si tous les objectifs sont complétés"""
        tous_completes = all(details["etat"] == "completee" for details in self.objectifs.values())
        
        if tous_completes and self.etat == "en_cours":
            self.terminer()
            return True
        return False
    
    def terminer(self):
        """Marque la quête comme terminée"""
        self.etat = "completee"
        from datetime import datetime
        self.date_fin = datetime.now()
        print(f"[DONE] Quete terminee: {self.nom}")
    
    def get_progression_totale(self):
        """Retourne le pourcentage d'avancement"""
        total_obj = len(self.objectifs)
        obj_completes = sum(1 for obj in self.objectifs.values() if obj["etat"] == "completee")
        return (obj_completes / total_obj * 100) if total_obj > 0 else 0
    
    def to_dict(self):
        """Convertit la quête en dictionnaire (pour sauvegardes)"""
        return {
            "nom": self.nom,
            "description": self.description,
            "types_objectifs": self.types_objectifs,
            "objectifs": self.objectifs,
            "recompense_argent": self.recompense_argent,
            "etat": self.etat,
            "date_debut": str(self.date_debut) if self.date_debut else None,
            "date_fin": str(self.date_fin) if self.date_fin else None,
        }


class GestionnaireQuetes:
    """Gère toutes les quêtes du jeu"""
    
    def __init__(self):
        self.quetes_par_etat = {
            "non_commencee": [],
            "en_cours": [],
            "completee": []
        }
        self.quetes_completees_total = 0
    
    def ajouter_quete(self, quete):
        """Ajoute une quête non commencée"""
        self.quetes_par_etat["non_commencee"].append(quete)
    
    def demarrer_quete(self, quete):
        """Démarre une quête"""
        if quete in self.quetes_par_etat["non_commencee"]:
            self.quetes_par_etat["non_commencee"].remove(quete)
            quete.demarrer()
            self.quetes_par_etat["en_cours"].append(quete)
            return True
        return False
    
    def completer_quete(self, quete):
        """Complète une quête"""
        if quete in self.quetes_par_etat["en_cours"]:
            self.quetes_par_etat["en_cours"].remove(quete)
            quete.terminer()
            self.quetes_par_etat["completee"].append(quete)
            self.quetes_completees_total += 1
            return True
        return False
    
    def augmenter_progression_quete(self, nom_objectif):
        """Augmente la progression des quêtes en cours avec cet objectif"""
        for quete in self.quetes_par_etat["en_cours"]:
            if nom_objectif in quete.objectifs:
                if quete.augmenter_progression(nom_objectif):
                    if quete.verifier_completion():
                        self.completer_quete(quete)
    
    def get_quetes_actives(self):
        """Retourne les quêtes en cours"""
        return self.quetes_par_etat["en_cours"]
    
    def get_toutes_quetes(self):
        """Retourne toutes les quêtes"""
        return {
            "non_commencee": self.quetes_par_etat["non_commencee"],
            "en_cours": self.quetes_par_etat["en_cours"],
            "completee": self.quetes_par_etat["completee"]
        }
    
    def get_stats_quetes(self):
        """Retourne les statistiques des quêtes"""
        total = sum(len(quetes) for quetes in self.quetes_par_etat.values())
        completees = len(self.quetes_par_etat["completee"])
        en_cours = len(self.quetes_par_etat["en_cours"])
        
        return {
            "total": total,
            "completees": completees,
            "en_cours": en_cours,
            "non_commencees": len(self.quetes_par_etat["non_commencee"]),
            "pourcentage": (completees / total * 100) if total > 0 else 0
        }
