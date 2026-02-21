import time
import threading
import random

from monture import Monture

class Elephants(Monture):
    def __init__(self):
        super().__init__(nom="Éléphant", vitesse=8, endurance=150, attaque=30, sante=120, capacite_transport=4)

    def charger(self):
        """Charge avec force, dévastant tout sur son passage."""
        if self.endurance >= 15:
            self.endurance -= 15
            return f"{self.nom} charge avec force et dévaste tout sur son passage."
        else:
            return f"{self.nom} n'a pas assez d'endurance pour charger !"

    def competence_defense(self):
        """Augmente la résistance de l'éléphant aux attaques pendant un tour."""
        if self.endurance >= 10:
            self.endurance -= 10
            return f"{self.nom} utilise sa compétence Défense pour augmenter sa résistance aux attaques pendant un tour !"
        else:
            return f"{self.nom} n'a pas assez d'endurance pour se défendre !"