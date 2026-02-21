import time
import threading
import random

from pnj import PNJ

class MaitreDesEcrits(PNJ):
    def __init__(self, nom, point_de_vie, recompense):
        super().__init__(nom, point_de_vie, recompense)
        self.livres_epiques = 0  # Compte les livres épiques en possession du Maître des Écrits

    def donner_livres_epiques(self, nombre, joueur):
        if joueur.inventaire["livres_epiques"] >= nombre:
            joueur.inventaire["livres_epiques"] -= nombre
            self.ajouter_livre_epique(nombre)
        else:
            print(f"{joueur.nom} n'a pas assez de livres épiques.")

    def donner_livre_legendaire(self, joueur):
        livre = self.creer_livre_legendaire()
        if livre:
            joueur.inventaire["livres_legendaires"] += 1
            print(f"{joueur.nom} a reçu un Livre Légendaire !")

    def ajouter_livre_epique(self, nombre):
        """Ajoute un certain nombre de livres épiques à l'inventaire du Maître des Écrits."""
        if nombre > 0:
            self.livres_epiques += nombre
            print(f"{nombre} Livre(s) Épique(s) ajouté(s) à l'inventaire de {self.nom}.")
        else:
            print("Le nombre de livres ajoutés doit être positif.")

    def peut_creer_livre_legendaire(self):
        """Vérifie si le Maître des Écrits a assez de livres épiques pour créer un livre légendaire."""
        return self.livres_epiques >= 25

    def creer_livre_legendaire(self):
        """Crée un Livre Légendaire si les conditions sont remplies."""
        if self.peut_creer_livre_legendaire():
            self.livres_epiques -= 25  # Réduit le nombre de livres épiques requis
            livre_legendaire = LivreDeSorts(type_livre="Légendaire")
            print(f"{self.nom} a créé un Livre Légendaire !")
            return livre_legendaire
        else:
            print(f"{self.nom} n'a pas assez de livres épiques pour créer un Livre Légendaire.")
            return None

    def afficher_inventaire(self):
        """Affiche le nombre de livres épiques en possession."""
        print(f"{self.nom} possède {self.livres_epiques} Livre(s) Épique(s).")

    def interagir(self):
        """Interaction spécifique pour le Maître des Écrits."""
        print(f"{self.nom} vous propose de transformer vos livres épiques en livres légendaires.")
        self.afficher_inventaire()
