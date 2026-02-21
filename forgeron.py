import time
import threading
import random

from pnj import PNJ

class Forgeron(PNJ):
    def __init__(self, nom, point_de_vie, recompense):
        super().__init__(nom, point_de_vie, recompense)
        self.stock = {
            'fer': 8,
            'or': 5,
            'diamant': 2
        }
        self.caisse = 2500

    def fabriquer_objet(self, type_objet):
        """Fabrique un objet à partir des matériaux disponibles et génère ses caractéristiques."""
        if type_objet == "arme":
            matiere = random.choice(['fer', 'or', 'diamant'])
            if self.stock[matiere] >= 1:
                self.stock[matiere] -= 1
                caracteristique = f"{matiere.capitalize()} épée"
                print(f"Le forgeron a fabriqué une {caracteristique}.")
                return caracteristique
            else:
                print("Matériaux insuffisants pour fabriquer l'objet.")
                return None
        else:
            print("Type d'objet inconnu.")
            return None

    def améliorer_objet(self, objet, niveau):
        """Améliore un objet à un niveau supérieur si les matériaux nécessaires sont disponibles."""
        niveaux = {
            'fer': ['fer I', 'fer II', 'fer III', 'fer IV', 'fer V'],
            'or': ['or I', 'or II', 'or III', 'or IV', 'or V'],
            'diamant': ['diamant I', 'diamant II', 'diamant III', 'diamant IV', 'diamant V'],
        }

        for matiere, niveaux_disponibles in niveaux.items():
            if objet in niveaux_disponibles:
                index = niveaux_disponibles.index(objet)
                if index < len(niveaux_disponibles) - 1:
                    niveau_suivant = niveaux_disponibles[index + 1]
                    cout_amelioration = 2  # Coût de l'amélioration

                    if self.stock[matiere] >= cout_amelioration:
                        self.stock[matiere] -= cout_amelioration
                        print(f"Le forgeron a amélioré {objet} en {niveau_suivant}.")
                        return niveau_suivant
                    else:
                        print("Matériaux insuffisants pour l'amélioration.")
                        return objet
                else:
                    print("L'objet est déjà au niveau maximum.")
                    return objet

        print("Objet inconnu ou non améliorable.")
        return objet

    def vendre_objet(self, objet, prix):
        """Vends un objet et ajoute le prix à la caisse."""
        self.caisse += prix
        print(f"Le forgeron a vendu {objet} pour {prix} pièces d'or.")

    def acheter_matieres(self, type_matiere, quantite, prix_unitaire):
        """Achète des matériaux si la caisse le permet."""
        cout_total = quantite * prix_unitaire
        if cout_total <= self.caisse:
            self.stock[type_matiere] = self.stock.get(type_matiere, 0) + quantite
            self.caisse -= cout_total
            print(f"Le forgeron a acheté {quantite} {type_matiere} pour {cout_total} pièces d'or.")
        else:
            print("Fonds insuffisants pour l'achat.")

    def interagir(self):
        """Personnalisation de l'interaction avec le forgeron."""
        print(f"{self.nom} vous propose ses services de forge. Voici ce qu'il peut fabriquer :")
        print("1. Armes (fer, or, diamant)")
        print("2. Amélioration d'objets (fer, or, diamant)")
        print("3. Achat de matériaux")
        print(f"Son stock actuel : {self.stock}")
        print(f"Sa caisse actuelle : {self.caisse} pièces d'or")
        # Ajout d'une interaction pour gagner de l'argent, même sans vente directe
        self.gagner_argent(500)  # Exemple, le menuisier gagne 500 pièces d'or à chaque interaction

