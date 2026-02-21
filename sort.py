import time
import threading
import random


class Sort:
    def __init__(self, nom, cout_mana, puissance):
        self.nom = nom
        self.cout_mana = cout_mana
        self.puissance = puissance

    def lancer(self, cible):
        """Effet du sort sur la cible."""
        print(f"{self.nom} est lancé sur {cible.nom}, infligeant {self.puissance} points de dégâts !")
