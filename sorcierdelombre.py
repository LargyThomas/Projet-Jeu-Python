import time
import threading
import random

from pnj import PNJ

class SorcierDeLOmbre(PNJ):
    def __init__(self, nom, points_vie, points_mana, puissance_sombre, recompense):
        super().__init__(nom, points_vie, recompense)  # Héritage des attributs de PNJ
        self.points_mana = points_mana
        self.puissance_sombre = puissance_sombre  # Augmente les effets des attaques d'ombre

    def attaque_ombre(self, ennemi):
        """Inflige des dégâts d'ombre et vole des points de vie à l'ennemi."""
        degats = 5 + self.puissance_sombre
        ennemi.points_vie -= degats
        self.points_vie = min(self.points_vie + 2, 100)  # Récupère des PV sans dépasser le max
        print(f"{self.nom} inflige {degats} points de dégâts d'ombre à {ennemi.nom} et récupère 2 points de vie.")

    def voile_de_tenebres(self):
        """Rend invisible pour éviter une attaque."""
        if self.points_mana >= 10:
            self.points_mana -= 10
            print(f"{self.nom} devient invisible pour un tour !")
            # Effet : l'ennemi rate la prochaine attaque contre le Sorcier
        else:
            print(f"{self.nom} n'a pas assez de mana pour utiliser Voile de Ténèbres.")

    def invocation_esprit(self, ennemi):
        """Invoque un esprit qui attaque l'ennemi pour un tour."""
        if self.points_mana >= 15:
            esprit_degats = 8 + self.puissance_sombre
            ennemi.points_vie -= esprit_degats
            self.points_mana -= 15
            print(f"{self.nom} invoque un esprit qui inflige {esprit_degats} points de dégâts à {ennemi.nom}.")
        else:
            print(f"{self.nom} n'a pas assez de mana pour invoquer un esprit.")

    def malediction(self, ennemi):
        """Réduit les dégâts de l'ennemi pour plusieurs tours."""
        if self.points_mana >= 20:
            self.points_mana -= 20
            ennemi.degats_reduits = True  # Marque l'ennemi comme maudit
            print(f"{self.nom} maudit {ennemi.nom}, réduisant ses dégâts pendant 3 tours.")
        else:
            print(f"{self.nom} n'a pas assez de mana pour lancer Malédiction.")

    def interagir(self):
        print(f"{self.nom} vous fixe d'un regard perçant, son pouvoir sombre flottant autour de lui.")
