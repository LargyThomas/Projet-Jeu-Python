import time
import threading
import random

class Nourriture:
    def __init__(self, nom, points_de_vie, quantite):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.quantite = quantite

    def nombre_unite(self):
        return self.quantite

    def manger(self):
        if self.quantite > 0:
            self.quantite -= 1
            return self.points_de_vie  # Retourne les points de vie récupérés
        return 0  # Si la nourriture est épuisée, retourne 0