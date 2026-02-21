import time
import threading
import random

from monture import Monture

class LoupGeant(Monture):
    def __init__(self):
        super().__init__(nom="Loup Géant", vitesse=12, endurance=80, attaque=20, sante=70, capacite_transport=2)

    def chasser(self):
        """Prépare le Loup Géant à chasser ses proies."""
        return f"{self.nom} se prépare à chasser ses proies."

    def competence_ambush(self, cible):
        """Utilise la compétence Embuscade pour attaquer une cible."""
        if self.endurance >= 10:
            self.endurance -= 10
            return f"{self.nom} utilise sa compétence Embuscade pour attaquer {cible} !"
        else:
            return f"{self.nom} n'a pas assez d'endurance pour l'embuscade !"

    def debuff_enemi(self, cible):
        """Réduit l'attaque de l'ennemi de 5 points pendant un tour."""
        if self.endurance >= 5:
            self.endurance -= 5
            return f"{self.nom} utilise sa compétence de débuff pour réduire l'attaque de {cible} de 5 points pendant un tour !"
        else:
            return f"{self.nom} n'a pas assez d'endurance pour débuff !"