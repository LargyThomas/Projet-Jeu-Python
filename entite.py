import time
import threading
import random

class Entite:
    def __init__(self, nom, niveau):
        self.nom = nom
        self.niveau = niveau
        self.points_de_vie = 100  # Par exemple, à personnaliser selon les entités
        self.faim = 10

    def restaurer_PV(self, points):
        """Méthode pour restaurer des points de vie"""
        self.points_de_vie += points
        if self.points_de_vie > 100:  # Limiter à un maximum de PV
            self.points_de_vie = 100
        print(f"{self.nom} a restauré {points} PV. Points de vie actuels : {self.points_de_vie}")