import time
import threading
import random


class Niveau:
    def __init__(self):
        self.niveau_actuel = 1  # Niveau du personnage
        self.xp_actuelle = 0    # XP actuelle
        self.xp_niveau_suivant = 250  # XP pour atteindre le prochain niveau

    def ajouter_xp(self, xp):
        self.xp_actuelle += xp
        print(f"Vous avez gagné {xp} XP, XP totale: {self.xp_actuelle}/{self.xp_niveau_suivant}")

        while self.xp_actuelle >= self.xp_niveau_suivant:
            self.augmenter_niveau()

    def augmenter_niveau(self):
        self.niveau_actuel += 1
        self.xp_actuelle -= self.xp_niveau_suivant
        self.xp_niveau_suivant = int(self.xp_niveau_suivant * 1.2)  # Prochain niveau = (+20%)
        print(f"Félicitations, vous êtes maintenant au niveau {self.niveau_actuel} !")