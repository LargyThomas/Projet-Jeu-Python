import time
import threading
import random

from pnj import PNJ

class Fermier(PNJ):
    def __init__(self, nom, point_de_vie, recompense):
        super().__init__(nom, point_de_vie, recompense)
        self.ferme = {'poule': 15, 'cochon': 5, 'vache': 12, 'mouton': 15}
        self.caisse = 2500
        self.ressources = {
            'oeufs': 0,
            'lait': 0,
            'laine': 0,
            'poulet': 0,
            'porc': 0,
            'boeuf': 0
        }

    def recuperer_ressources(self):
        self.ressources['oeufs'] += self.ferme['poule'] * 1  # 1 œuf par poule
        self.ressources['lait'] += self.ferme['vache'] * 2   # 2 litres de lait par vache
        self.ressources['laine'] += self.ferme['mouton'] * 0.5  # 0.5 kg de laine par mouton
        self.ressources['poulet'] += self.ferme['poule'] * 1  # 1 poulet par poule
        self.ressources['porc'] += self.ferme['cochon'] * 1   # 1 porc par cochon
        self.ressources['boeuf'] += self.ferme['vache'] * 1   # 1 boeuf par vache

    def payer_soins(self):
        frais = (self.ferme['poule'] + self.ferme['cochon'] + self.ferme['vache'] + self.ferme['mouton']) * 5
        if self.caisse >= frais:
            self.caisse -= frais
            print(f"Frais de soins payés : {frais} pièces.")
        else:
            print("Pas assez d'argent pour payer les soins.")

    def vendre_animal(self, animal, prix):
        if animal in self.ferme and self.ferme[animal] > 0:
            self.ferme[animal] -= 1
            self.caisse += prix
            print(f"{animal.capitalize()} vendu pour {prix} pièces.")
        else:
            print("Pas d'animal à vendre.")

    def acheter_animal(self, animal, prix):
        if self.caisse >= prix:
            self.ferme[animal] += 1
            self.caisse -= prix
            print(f"{animal.capitalize()} acheté pour {prix} pièces.")
        else:
            print("Pas assez d'argent.")

    def interagir(self):
        print(f"{self.nom} vous propose des produits de la ferme.")
        print(f"Voici ce que vous avez dans votre ferme : {self.ferme}")
        print(f"Ressources disponibles : {self.ressources}")
        # Tu peux ajouter d'autres actions ici, par exemple vendre ou acheter des animaux
