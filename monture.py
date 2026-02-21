import time
import threading
import random

from entité import Entite

class Monture(Entite):
    def __init__(self, nom, vitesse, endurance, attaque, sante, capacite_transport):
        super().__init__(nom, 1)  # Appelle le constructeur de la super-classe Entite
        self.vitesse = vitesse
        self.endurance = endurance
        self.attaque = attaque
        self.sante = sante
        self.capacite_transport = capacite_transport

    def se_deplacer(self):
        return f"{self.nom} se déplace à une vitesse de {self.vitesse}."

    def attaquer(self):
        return f"{self.nom} attaque avec {self.attaque} points de dégâts."

    def subir_degats(self, degats):
        self.sante -= degats
        if self.sante <= 0:
            return f"{self.nom} est vaincu !"
        return f"{self.nom} a maintenant {self.sante} points de vie."

    def transporter(self):
        return f"{self.nom} peut transporter jusqu'à {self.capacite_transport} personnes."

    def recuperer_endurance(self, amount):
        self.endurance += amount
        return f"{self.nom} récupère {amount} d'endurance. Endurance actuelle : {self.endurance}."

    def est_fatigue(self):
        return self.endurance < 20  # Détermine si la monture est fatiguée (par exemple, si l'endurance est inférieure à 20)