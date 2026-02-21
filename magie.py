import time
import threading
import random


from perso import Perso

class Magie(Perso):
    def __init__(self, nom, pv, endurance, mana):
        super().__init__(nom, pv, endurance)
        self.mana = mana
        self.livre_de_sorts = LivreDeSorts()

    def apprendre_sort(self, sort):
        self.livre_de_sorts.ajouter_sort(sort)

    def lancer_sort(self, indice_sort, cible):
        sort = self.livre_de_sorts.sorts[indice_sort]
        if self.mana >= sort.cout_mana:
            self.mana -= sort.cout_mana
            sort.lancer(cible)
        else:
            print("Mana insuffisant pour lancer ce sort.")

    def afficher_sorts(self):
        self.livre_de_sorts.afficher_sorts()