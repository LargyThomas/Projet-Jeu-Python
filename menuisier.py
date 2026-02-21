import time
import threading
import random

from pnj import PNJ

class Menuisier(PNJ):
    def __init__(self, nom, point_de_vie, recompense):
        super().__init__(nom, point_de_vie, recompense)
        self.stock_boiseries = {'chêne': 10, 'pin': 5}
        self.stock_objets = {'épée en bois': 0, 'barrière en bois': 0}
        self.caisse = 2000

    def collecter_bois(self, zone):
        bois_par_zone = {
            "forêt": ["chêne", "pin", "sapin"],
            "plaine": ["pin"],
            "montagne": ["chêne", "sapin"]
        }

        if zone in bois_par_zone:
            bois = random.choice(bois_par_zone[zone])
            self.stock_boiseries[bois] += 1
            print(f"Vous avez collecté 1 unité de {bois} dans la zone {zone}.")
        else:
            print("Zone inconnue. Aucune ressource à collecter.")

    def fabriquer_objet(self, type_objet):
        recettes = {
            "épée en bois": {"chêne": 2},
            "barrière en bois": {"pin": 3},
            "meuble": {"chêne": 1, "pin": 1}
        }

        if type_objet in recettes:
            recette = recettes[type_objet]
            if all(self.stock_boiseries.get(bois, 0) >= quantite for bois, quantite in recette.items()):
                for bois, quantite in recette.items():
                    self.stock_boiseries[bois] -= quantite
                self.stock_objets[type_objet] += 1
                print(f"Vous avez fabriqué une {type_objet}.")
            else:
                print(f"Vous n'avez pas assez de bois pour fabriquer une {type_objet}.")
        else:
            print(f"Type d'objet {type_objet} inconnu.")

    def ameliorer_objet(self, type_objet):
        if type_objet == "barrière en bois" and self.stock_objets["barrière en bois"] > 0:
            self.stock_objets["barrière en bois"] -= 1
            self.stock_objets["barrière en bois renforcé"] = self.stock_objets.get("barrière en bois renforcé", 0) + 1
            print("Vous avez amélioré la barrière en bois en barrière en bois renforcé.")
        else:
            print("Impossible d'améliorer cet objet.")

    def vendre_objet(self, objet, prix):
        self.caisse += prix
        print(f"Le menuisier a vendu {objet} pour {prix} pièces d'or.")

    def acheter_matieres(self, type_matiere, quantite, prix_unitaire):
        cout_total = quantite * prix_unitaire
        if cout_total <= self.caisse:
            self.stock_boiseries[type_matiere] += quantite
            self.caisse -= cout_total
            print(f"Le menuisier a acheté {quantite} {type_matiere} pour {cout_total} pièces d'or.")
        else:
            print("Fonds insuffisants pour l'achat.")

    def afficher_inventaire(self):
        print("Inventaire des boiseries :")
        for bois, quantite in self.stock_boiseries.items():
            print(f"{bois} : {quantite}")

        print("Inventaire des objets fabriqués :")
        for objet, quantite in self.stock_objets.items():
            print(f"{objet} : {quantite}")

    def interagir(self):
        print(f"{self.nom} vous propose ses services de menuiserie.")
        self.afficher_inventaire()
        # Ajout d'une interaction pour gagner de l'argent, même sans vente directe
        self.gagner_argent(500)  # Exemple, le menuisier gagne 500 pièces d'or à chaque interaction

