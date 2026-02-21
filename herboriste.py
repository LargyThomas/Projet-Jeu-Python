import time
import threading
import random

from pnj import PNJ

class Herboriste(PNJ):
    def __init__(self, nom, point_de_vie, recompense):
        super().__init__(nom, point_de_vie, recompense)  # Appel du constructeur de PNJ
        self.stock_plantes = {'herbe_medecinale': 5, 'fleur_mystique': 3, 'champignon': 9}
        self.stock_potions = {'potion_guerison': 4, 'potion_force': 1, 'potion_rapidite': 2}
        self.caisse = 1500

    def collecter_plante(self, zone):
        plantes_par_zone = {
            "plaines verdoyantes": ["herbe médicinale", "feuille de chêne"],
            "forêt sombre": ["nénuphar", "champignon étrange"],
            "montagne": ["fleur de givre", "racine ancienne"],
            "village abandonné": ["ortie", "lierre grimpant", "fleur noire"],
            "désert": ["cactus épineux", "sauge du désert", "fleur de sable"],
            "caverne": ["mousse luminescente", "champignon des ténèbres", "lichen rouge"],
            "château abandonné": ["rose fanée", "bruyère spectrale", "herbe maudite"]
        }

        if zone in plantes_par_zone:
            plante = random.choice(plantes_par_zone[zone])
            self.stock_plantes[plante] = self.stock_plantes.get(plante, 0) + 1
            print(f"Vous avez collecté {plante} dans la zone {zone}.")
        else:
            print("Zone inconnue. Aucune plante à collecter.")

    def preparer_potion(self, type):
        recettes_potions = {
            "potion de guérison": {"herbe médicinale": 2, "fleur sauvage": 1},
            "potion de résistance": {"racine ancienne": 1, "fleur de givre": 1},
            "potion de force": {"fleur noire": 1, "cactus épineux": 2},
            "potion de rapidité": {"pissenlit": 2, "feuille de chêne": 1},
            "potion de mana": {"mousse luminescente": 1, "lichen rouge": 1},
            "potion de régénération": {"ortie": 1, "nénuphar": 1, "sauge du désert": 1},
            "potion maudite": {"herbe maudite": 1, "rose fanée": 1}
        }

        if type in recettes_potions:
            recette = recettes_potions[type]
            if all(self.stock_plantes.get(plante, 0) >= quantite for plante, quantite in recette.items()):
                for plante, quantite in recette.items():
                    self.stock_plantes[plante] -= quantite
                print(f"Vous avez préparé une {type}.")
            else:
                print(f"Vous n'avez pas assez de plantes pour préparer une {type}.")
        else:
            print(f"Type de potion {type} inconnu.")

    def ameliorer_potion(self, niveau):
        recettes = {
            1: {"fleur noire": 1, "fleur bleue": 1},
            2: {"fleur noire": 1, "cactus épineux": 2},
            3: {"fleur rouge": 1, "fleur bleue": 2},
            4: {"fleur rouge": 2, "cactus épineux": 1},
        }

        if niveau not in recettes:
            print("Niveau de potion non reconnu.")
            return None

        recette = recettes[niveau]

        if all(self.stock_plantes.get(plante, 0) >= quantite for plante, quantite in recette.items()):
            for plante, quantite in recette.items():
                self.stock_plantes[plante] -= quantite

            potion = None
            if niveau == 1:
                potion = Potion("Potion de soin de niveau 1", "Restaure 5 PV")
            elif niveau == 2:
                potion = Potion("Potion de force", "Augmente la force de 5 points pendant 10 minutes")
            elif niveau == 3:
                potion = Potion("Potion de soin de niveau 3", "Restaure 10 PV")
            elif niveau == 4:
                potion = Potion("Potion de force améliorée", "Augmente la force de 10 points pendant 15 minutes")

            print(f"Vous avez créé {potion.nom}!")
            return potion
        else:
            print("Vous n'avez pas assez d'ingrédients pour créer cette potion.")
            return None

    def vendre_objet(self, objet, prix):
        self.caisse += prix
        print(f"L'herboriste a vendu {objet} pour {prix} pièces d'or.")

    def acheter_matieres(self, type_matiere, quantite, prix_unitaire):
        cout_total = quantite * prix_unitaire
        if cout_total <= self.caisse:
            self.stock_plantes[type_matiere] = self.stock_plantes.get(type_matiere, 0) + quantite
            self.caisse -= cout_total
            print(f"L'herboriste a acheté {quantite} {type_matiere} pour {cout_total} pièces d'or.")
        else:
            print("Fonds insuffisants pour l'achat.")

    def afficher_inventaire(self):
        print("Inventaire des plantes :")
        for plante, quantite in self.stock_plantes.items():
            print(f"{plante} : {quantite}")

    def interagir(self):
        print(f"{self.nom} vous propose des services de préparation de potion ou remède.")
        self.afficher_inventaire()
        # Ajout d'une interaction pour gagner de l'argent, même sans vente directe
        self.gagner_argent(500)  # Exemple, le menuisier gagne 500 pièces d'or à chaque interaction

