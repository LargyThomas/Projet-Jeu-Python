import time
import threading
import random

from pnj import PNJ

class MageElementaire(PNJ):
    def __init__(self, nom, point_de_vie, recompense, niveau=1, mana=100):
        # Appel du constructeur de PNJ pour les attributs généraux
        super().__init__(nom, point_de_vie, recompense)

        # Attributs spécifiques à MageElementaire
        self.niveau = niveau
        self.mana = mana
        self.vie = 50 + niveau * 10  # Points de vie augmentés avec le niveau
        self.element = None
        self.compteur_essence = {"feu": 0, "eau": 0, "terre": 0, "air": 0}

    def choisir_element(self, element):
        if element in ["feu", "eau", "terre", "air"]:
            self.element = element
            print(f"{self.nom} a choisi l'élément {self.element}.")
        else:
            print("Élément non valide !")

    def accumuler_essence(self):
        if self.element:
            self.compteur_essence[self.element] += 1
            print(f"{self.nom} accumule de l'essence de {self.element} ({self.compteur_essence[self.element]} points).")
        else:
            print("Aucun élément choisi pour accumuler de l'essence.")

    def boule_de_feu(self, ennemi):
        if self.element == "feu" and self.mana >= 20:
            degats = 15 + 5 * self.niveau
            ennemi.vie -= degats
            self.mana -= 20
            self.accumuler_essence()
            print(f"{self.nom} lance Boule de Feu ! {ennemi.nom} perd {degats} points de vie.")
        else:
            print("Pas assez de mana ou élément incorrect.")

    def mur_d_eau(self):
        if self.element == "eau" and self.mana >= 15:
            self.mana -= 15
            self.accumuler_essence()
            print(f"{self.nom} crée un Mur d'Eau, réduisant les dégâts subis pour le prochain tour.")
        else:
            print("Pas assez de mana ou élément incorrect.")

    def terre_ecrasante(self, ennemi):
        if self.element == "terre" and self.mana >= 25:
            self.mana -= 25
            ennemi.etat = "étourdi"
            self.accumuler_essence()
            print(f"{self.nom} utilise Terre Écrasante ! {ennemi.nom} est étourdi.")
        else:
            print("Pas assez de mana ou élément incorrect.")

    def tempete_de_vent(self):
        if self.element == "air" and self.mana >= 20:
            self.mana -= 20
            self.accumuler_essence()
            print(f"{self.nom} lance une Tempête de Vent, augmentant sa vitesse et réduisant celle de l'ennemi.")
        else:
            print("Pas assez de mana ou élément incorrect.")

    def regenerer_mana(self):
        regen = 10 + 2 * self.niveau
        self.mana += regen
        print(f"{self.nom} régénère {regen} points de mana.")

    def lancer_sort_ultime(self, ennemi):
        if self.element == "feu" and self.compteur_essence["feu"] >= 5:
            degats = 50 + 10 * self.niveau
            ennemi.vie -= degats
            self.compteur_essence["feu"] = 0
            print(f"{self.nom} déclenche *Explosion Ardente*! {ennemi.nom} perd {degats} points de vie.")

        elif self.element == "eau" and self.compteur_essence["eau"] >= 5:
            soins = 40 + 5 * self.niveau
            self.vie += soins
            self.compteur_essence["eau"] = 0
            print(f"{self.nom} déclenche *Tsunami Régénérateur*! {self.nom} récupère {soins} points de vie.")

        elif self.element == "terre" and self.compteur_essence["terre"] >= 5:
            bouclier = 30 + 5 * self.niveau
            self.vie += bouclier
            self.compteur_essence["terre"] = 0
            print(f"{self.nom} déclenche *Barrière de Roches*! {self.nom} gagne {bouclier} points de vie en bouclier.")

        elif self.element == "air" and self.compteur_essence["air"] >= 5:
            degats = 35 + 8 * self.niveau
            ennemi.vie -= degats
            self.compteur_essence["air"] = 0
            print(f"{self.nom} déclenche *Tempête Divine*! {ennemi.nom} perd {degats} points de vie et est désorienté.")

        else:
            print("Pas assez d'essence accumulée pour lancer le sort ultime.")

    def interagir(self):
        print(f"{self.nom} vous regarde avec un sourire mystérieux.")
        print("Il vous propose de l'aide pour maîtriser les éléments.")
        print(f"Voici les éléments que vous pouvez choisir : feu, eau, terre, air.")

        if self.element:
            print(f"Actuellement, vous maîtrisez l'élément : {self.element}.")
        else:
            print("Vous n'avez pas encore choisi d'élément.")

        print(f"Mana disponible : {self.mana}")
        print(f"Essence accumulée : {self.compteur_essence}")

        # Actions possibles
        print("Que voulez-vous faire ?")
        print("1. Choisir un élément.")
        print("2. Accumuler de l'essence.")
        print("3. Regénérer du mana.")
        print("4. Quitter l'interaction.")

        # Exemple d'une action, à développer selon l'input du joueur
        action = input("Entrez le numéro de l'action souhaitée : ")

        if action == "1":
            element = input("Quel élément voulez-vous choisir (feu, eau, terre, air) ? ")
            self.choisir_element(element)
        elif action == "2":
            self.accumuler_essence()
        elif action == "3":
            self.regenerer_mana()
        elif action == "4":
            print("Vous quittez l'interaction.")
        else:
            print("Action invalide.")
