class Quete:
    def __init__(self, nom, description, types_objectifs, objectifs, recompense, quantite):
        self.nom = nom
        self.description = description
        self.types_objectifs = types_objectifs  # Types d'objectifs : "Combat", "Collecte", "Exploration"

        #Utilisation d'un dictionnaire pour chaque objectif
        self.objectifs = {objectif: {"quantite": quantite, "etat": "non commencé"} for objectif in objectifs}

        self.recompense = recompense
        self.etat = "non commencée"  # État de la quête : "non commencée", "en cours", "complétée"

    def demarrer_quete(self):
        self.etat = "en cours"
        print(f"Quête {self.nom} commencée !")

    def verifier_objectifs(self, compteurs):
        """
        Vérifie les objectifs de la quête en fonction des compteurs donnés (ex. : ennemis vaincus, objets ramassés, zones explorées).
        """
        if self.etat != "en cours":
            return False

        tous_completes = True
        for objectif, details in self.objectifs.items():
            valeur_attendue = details["quantite"]  # Correction : on récupère la quantité de l'objectif
            etat = details["etat"]

            # Vérifier si l'objectif est atteint
            if compteurs.get(objectif, 0) >= valeur_attendue and etat != "complété":
                self.objectifs[objectif]["etat"] = "complété"
                print(f"Objectif '{objectif}' complété !")
            elif etat != "complété":
                tous_completes = False

        if tous_completes:
            self.terminer_quete()
            return True
        return False

    def terminer_quete(self):
        """Marque la quête comme terminée si tous les objectifs sont complétés."""
        if all(details["etat"] == "complété" for details in self.objectifs.values()):
            self.etat = "complétée"
            self.donner_recompense()
            print(f"Quête {self.nom} terminée !")
            return True
        else:
            print(f"Quête {self.nom} non terminée.")
            return False

    def afficher_info(self):
        """Affiche les informations de la quête."""
        print(f"Quête : {self.nom}")
        print(f"Description : {self.description}")
        print(f"État : {self.etat}")
        for objectif, details in self.objectifs.items():
            etat = details["etat"]
            quantite = details["quantite"]
            print(f"{objectif} : {etat} ({quantite})")

    def donner_recompense(self):
        """Gère la récompense donnée à la fin de la quête."""
        print(f"Récompense pour la quête {self.nom}: {self.recompense}")
        # Ajoute la récompense au joueur si besoin (ajouter l'intégration avec une classe joueur ou inventaire)