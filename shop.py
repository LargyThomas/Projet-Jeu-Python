import time
import threading
import random


class Shop:
    def __init__(self):
        self.stock = {
            'chaussure': [5, 2],  # [prix, quantité en stock]
            'pantalon': [6, 2],
            'bonnet': [2, 1],
            'poulet': [3, 3],
            'cochon': [4, 3],
            'epee_or': [1, 15],
            'epee_fer': [1, 10],
            'hache': [3, 7]
        }
        self.caisse = 5000

    def afficher_stock(self):
        print("--- Stock du magasin ---")
        for objet, info in self.stock.items():
            print(f"{objet.capitalize()} : Prix: {info[0]}, Quantité: {info[1]}")

    def acheter(self, objet, quantite, personnage):
        if objet in self.stock and self.stock[objet][1] >= quantite:
            total_prix = self.stock[objet][0] * quantite
            if personnage.argent >= total_prix:
                personnage.argent -= total_prix
                self.stock[objet][1] -= quantite
                print(f"{personnage.nom} a acheté {quantite} {objet}(s) pour {total_prix} pièces d'or.")
            else:
                print("Vous n'avez pas assez d'argent.")
        else:
            print("Cet objet n'est pas disponible en quantité suffisante.")