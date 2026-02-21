import time
import threading
import random

class PNJ:
    def __init__(self, nom, point_de_vie, recompense):
        self.nom = nom
        self.point_de_vie = point_de_vie
        self.recompense = recompense

    def est_vivant(self):
        return self.point_de_vie > 0

    # Méthode pour interagir avec le joueur, à personnaliser pour chaque type de PNJ
    def interagir(self):
        print(f"{self.nom} vous regarde avec un sourire.")

    def echanger(self, autre_pnj, ressource, quantite, prix_unitaire):
        """Effectue un échange de ressource entre PNJ."""
        total_prix = quantite * prix_unitaire

        # Vérifier si le vendeur a assez de stock
        if self.stock.get(ressource, 0) < quantite:
            print(f"{self.nom} n'a pas assez de {ressource} en stock.")
            return False

        # Vérifier si l'acheteur a assez d'argent
        if autre_pnj.caisse < total_prix:
            print(f"{autre_pnj.nom} n'a pas assez d'argent pour acheter {quantite} {ressource}.")
            return False

        # Effectuer l'échange
        self.stock[ressource] -= quantite
        autre_pnj.stock[ressource] = autre_pnj.stock.get(ressource, 0) + quantite
        self.caisse += total_prix
        autre_pnj.caisse -= total_prix

        print(f"Échange réussi ! {autre_pnj.nom} a acheté {quantite} {ressource} à {self.nom}.")
        return True