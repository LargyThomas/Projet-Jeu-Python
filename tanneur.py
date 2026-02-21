import time
import threading
import random

from pnj import PNJ

class Tanneur(PNJ):
    def __init__(self, nom, point_de_vie, recompense):
        super().__init__(nom, point_de_vie, recompense)
        self.stock_cuir = {'cuir_brun': 5, 'cuir_noir': 3, 'cuir_royal': 1}
        self.stock_produits = {'armure_basique': 2, 'ceinture_en_cuir': 1}
        self.caisse = 1800

    def collecter_cuir(self, zone):
        animaux_par_zone = {
            "plaines verdoyantes": ["biche", "lapin"],
            "forêt sombre": ["ours", "renard", "loup"],
            "montagne": ["chamois", "roc", "dragon"],
            "village abandonné": ["sanglier", "serpent"],
            "désert": ["lézard géant", "scorpion géant"],
            "caverne": ["chauve-souris géante"],
            "château abandonné": ["araignée géante"]
        }

        if zone in animaux_par_zone:
            animal = random.choice(animaux_par_zone[zone])
            cuir_type = self._determiner_type_cuir(animal)
            self.stock_cuir[cuir_type] += 1
            print(f"{self.nom} a collecté du {cuir_type} de {animal} dans la zone {zone}.")
        else:
            print("Zone inconnue. Aucun cuir à collecter.")

    def _determiner_type_cuir(self, animal):
        types_cuir = {
            "biche": "cuir_brun",
            "lapin": "cuir_brun",
            "ours": "cuir_noir",
            "renard": "cuir_noir",
            "loup": "cuir_noir",
            "chamois": "cuir_royal",
            "roc": "cuir_royal",
            "dragon": "cuir_royal",
            "sanglier": "cuir_brun",
            "serpent": "cuir_noir",
            "lézard géant": "cuir_brun",
            "scorpion géant": "cuir_royal",
            "chauve-souris géante": "cuir_noir",
            "araignée géante": "cuir_royal"
        }
        return types_cuir.get(animal, "cuir_brun")

    def fabriquer_produit(self, type):
        recettes_produits = {
            "armure_basique": {"cuir_brun": 2},
            "ceinture_en_cuir": {"cuir_brun": 1, "cuir_noir": 1},
            "armure_avancee": {"cuir_noir": 3, "cuir_royal": 1},
            "bottes_en_cuir": {"cuir_brun": 2, "cuir_royal": 1}
        }

        if type in recettes_produits:
            recette = recettes_produits[type]
            if all(self.stock_cuir.get(cuir, 0) >= quantite for cuir, quantite in recette.items()):
                for cuir, quantite in recette.items():
                    self.stock_cuir[cuir] -= quantite
                self.stock_produits[type] = self.stock_produits.get(type, 0) + 1
                print(f"{self.nom} a fabriqué une {type}. Il vous reste {self.stock_cuir} de cuirs.")
            else:
                print(f"{self.nom} n'a pas assez de cuir pour fabriquer une {type}.")
        else:
            print(f"Type de produit {type} inconnu.")

    def vendre_objet(self, objet, prix):
        self.caisse += prix
        print(f"{self.nom} a vendu {objet} pour {prix} pièces d'or. Caisse actuelle: {self.caisse} pièces d'or.")

    def acheter_matieres(self, type_matiere, quantite, prix_unitaire):
        cout_total = quantite * prix_unitaire
        if cout_total <= self.caisse:
            self.stock_cuir[type_matiere] += quantite
            self.caisse -= cout_total
            print(f"{self.nom} a acheté {quantite} {type_matiere} pour {cout_total} pièces d'or.")
        else:
            print("Fonds insuffisants pour l'achat.")

    def afficher_inventaire(self):
        print(f"Inventaire de {self.nom} :")
        for cuir, quantite in self.stock_cuir.items():
            print(f"{cuir} : {quantite}")
        print("Produits fabriqués :")
        for produit, quantite in self.stock_produits.items():
            print(f"{produit} : {quantite}")

    def interagir(self):
        print(f"{self.nom} vous propose des services de tannage et de fabrication.")
        self.afficher_inventaire()
        # Ajout d'une interaction pour gagner de l'argent, même sans vente directe
        self.gagner_argent(500)  # Exemple, le menuisier gagne 500 pièces d'or à chaque interaction
