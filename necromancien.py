import time
import threading
import random

from pnj import PNJ

class Necromancien(PNJ):
    def __init__(self, nom, points_de_vie, recompense, niveau):
        # Appel du constructeur de la classe de base PNJ
        super().__init__(nom, points_de_vie, recompense)
        self.niveau = niveau
        self.squelettes_invokes = 0

    def souffle_de_vie(self, ennemi):
        """Récupère de la vie en infligeant des dégâts à l'ennemi."""
        degats = 10 + self.niveau * 2  # Dégâts augmentés par le niveau
        ennemi.points_de_vie -= degats
        self.points_de_vie += degats // 2  # Récupération de la moitié des dégâts infligés
        print(f"{self.nom} utilise Souffle de Vie sur {ennemi.nom}, inflige {degats} dégâts!")
        print(f"{ennemi.nom} a maintenant {ennemi.points_de_vie} points de vie.")
        print(f"{self.nom} a maintenant {self.points_de_vie} points de vie.")

    def invoquer_squelette(self):
        """Fait apparaître un squelette qui combat pour le Nécromancien."""
        self.squelettes_invokes += 1
        print(f"{self.nom} invoque un squelette! Total de squelettes invoqués : {self.squelettes_invokes}")

    def malediction_des_morts(self, ennemi):
        """Inflige des dégâts à un ennemi et réduit ses dégâts."""
        degats = 15 + self.niveau * 3  # Dégâts augmentés par le niveau
        ennemi.points_de_vie -= degats
        print(f"{self.nom} utilise Malédiction des Morts sur {ennemi.nom}, inflige {degats} dégâts!")
        print(f"{ennemi.nom} a maintenant {ennemi.points_de_vie} points de vie.")
        # Effet de réduction des dégâts (à implémenter dans la classe ennemi)

    def rituel_de_resurrection(self, allié):
        """Ramène un allié à la vie avec une partie de ses points de vie."""
        if allié.points_de_vie <= 0:
            points_recuperes = 5 + self.niveau * 2  # Points de vie récupérés augmentés par le niveau
            allié.points_de_vie += points_recuperes
            print(f"{self.nom} utilise Rituel de Résurrection sur {allié.nom}. {allié.nom} revient à la vie avec {allié.points_de_vie} points de vie!")
        else:
            print(f"{allié.nom} est déjà en vie!")
