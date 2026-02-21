class Histoire:
    def __init__(self):
        self.chapitre = 0  # Commence à l’étape 0 (début)

    def avancer(self, condition):
        if condition:  # Si la condition est remplie
            self.chapitre += 1
            if self.chapitre == 1:
                print("Nouvelle zone débloquée : Forêt Sombre !")
                # Tu pourrais par exemple ajouter un événement, débloquer des ennemis, etc.
            elif self.chapitre == 2:
                print("Vous avez gagné une récompense spéciale pour avoir vaincu le premier ennemi !")
                # Récompense, nouvelle quête, ou changement dans l'environnement.

