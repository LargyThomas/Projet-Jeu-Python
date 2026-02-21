import time
import threading
import random

from pnj import PNJ

class Druide(PNJ):
    def __init__(self, nom, niveau=1, points_vie=100, mana=50, recompense=None):
        # Initialisation des attributs de la classe parent PNJ
        super().__init__(nom, points_vie, recompense)
        self.niveau = niveau
        self.points_vie_max = points_vie
        self.mana_max = mana
        self.mana = mana

    def soin_de_la_nature(self, cible):
        """Restaure des points de vie à un allié ou à lui-même."""
        soin = 10 + (self.niveau * 2)
        if self.mana >= 10:
            cible.point_de_vie += soin
            cible.point_de_vie = min(cible.point_de_vie, cible.point_de_vie_max)  # Limite au maximum
            self.mana -= 10
            print(f"{self.nom} utilise Soin de la Nature sur {cible.nom} et restaure {soin} points de vie.")
        else:
            print(f"{self.nom} n'a pas assez de mana pour lancer Soin de la Nature.")

    def appel_de_la_faune(self):
        """Invoque un animal aléatoire pour combattre."""
        if self.mana >= 15:
            animaux = ['loup', 'ours', 'aigle']
            animal = random.choice(animaux)
            self.mana -= 15
            print(f"{self.nom} invoque un {animal} pour combattre à ses côtés !")
            return animal
        else:
            print(f"{self.nom} n'a pas assez de mana pour invoquer un animal.")
            return None

    def vigueur_de_la_terre(self, cible):
        """Augmente temporairement les PV maximum d'un allié ou de lui-même."""
        if self.mana >= 20:
            augmentation_pv = 20 + (self.niveau * 3)
            cible.points_vie_max += augmentation_pv
            self.mana -= 20
            print(f"{self.nom} utilise Vigueur de la Terre sur {cible.nom}, augmentant ses PV max de {augmentation_pv} pour le combat.")
        else:
            print(f"{self.nom} n'a pas assez de mana pour lancer Vigueur de la Terre.")

    def racines_entravantes(self, ennemi):
        """Immobilise un ennemi pour un tour."""
        if self.mana >= 15:
            ennemi.point_de_vie = max(0, ennemi.point_de_vie - 10)  # Inflige des dégâts et empêche le mouvement
            self.mana -= 15
            print(f"{self.nom} utilise Racines Entravantes sur {ennemi.nom}, infligeant des dégâts et immobilisant l'ennemi.")
        else:
            print(f"{self.nom} n'a pas assez de mana pour utiliser Racines Entravantes.")
