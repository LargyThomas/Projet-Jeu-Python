import time
import threading
import random

class LivreDeSorts:
    def __init__(self, type_livre="Épique"):
        if type_livre not in ["Épique", "Légendaire"]:
            raise ValueError("Type de livre invalide, choisir entre 'Épique' ou 'Légendaire'")
        self.type_livre = type_livre
        self.sorts = []
        self.sorts_max = 5 if type_livre == "Épique" else 15

    def ajouter_sort(self, sort):
        if len(self.sorts) < self.sorts_max:
            self.sorts.append(sort)
            print(f"Le sort '{sort.nom}' a été ajouté au {self.type_livre} livre.")
        else:
            print(f"Le {self.type_livre} livre est plein.")

    def lancer_sort(self, indice_sort, cible):
        if indice_sort < len(self.sorts):
            sort = self.sorts[indice_sort]
            sort.lancer(cible)
        else:
            print("Sort non disponible.")

    def améliorer_livre(self):
        if self.type_livre == "Épique" and MaitreDesEcrits.peut_creer_livre_legendaire():
            self.type_livre = "Légendaire"
            self.sorts_max = 15
            print("Le livre a été amélioré en Livre Légendaire !")
        else:
            print("Conditions non remplies pour améliorer le livre.")

    def afficher_sorts(self):
        print(f"--- {self.type_livre} Livre de Sorts ---")
        for i, sort in enumerate(self.sorts, start=1):
            print(f"{i}. {sort.nom}")
