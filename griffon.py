import time
import threading
import random

from monture import Monture

class Griffon(Monture):
    def __init__(self):
        super().__init__(nom="Griffon", vitesse=15, endurance=100, attaque=25, sante=80, capacite_transport=1)

    def voler(self):
        """Fait s'envoler le Griffon dans les airs."""
        return f"{self.nom} s'envole dans les airs avec agilité."

    def competence_vol(self, cible):
        """Utilise la compétence Vol pour attaquer un cible."""
        if self.endurance >= 10:
            self.endurance -= 10  # Coût d'endurance pour utiliser la compétence
            return f"{self.nom} utilise sa compétence Vol pour attaquer {cible} depuis les airs !"
        else:
            return f"{self.nom} n'a pas assez d'endurance pour voler !"

    def buff_attaque(self):
        """Augmente temporairement l'attaque du Griffon."""
        if self.endurance >= 5:
            self.attaque += 5  # Augmentation temporaire de l'attaque
            self.endurance -= 5
            return f"{self.nom} utilise sa compétence de buff pour augmenter son attaque à {self.attaque} pendant un tour !"
        else:
            return f"{self.nom} n'a pas assez d'endurance pour se buff !"