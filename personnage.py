"""
Classe Personnage - Joueur principal du jeu RPG
"""

class Personnage:
    def __init__(self, nom):
        self.nom = nom
        self.niveau = 1
        self.experience = 0
        self.vie = 10
        self.vie_max = 10
        self.faim = 10
        self.argent = 1000
        self.inventaire = {}
        self.tenue = {
            'tete': 'casquette',
            'haut': 'pull',
            'bas': 'pantalon',
            'pieds': 'basket'
        }
        self.main = {
            'gauche': 'rien',
            'droite': 'hache'
        }
        self.en_defense = False  # Est-on en train de défendre?
        self.reduction_defense = 0.5  # Réduit les dégâts de 50%
    
    def obtenir_nom(self):
        """Retourne le nom du personnage"""
        return self.nom
    
    def changer_argent(self, montant):
        """Change le montant d'argent"""
        self.argent = montant
    
    def gagner_experience(self, quantite_xp):
        """Ajoute de l'expérience et vérifie si level up"""
        self.experience += quantite_xp
        seuil_levelup = self.niveau * 100
        
        if self.experience >= seuil_levelup:
            self.monter_de_niveau()
    
    def monter_de_niveau(self):
        """Augmente le niveau et les stats"""
        self.niveau += 1
        self.experience = 0
        self.vie_max += 2
        self.vie = self.vie_max
        print(f"{self.nom} a atteint le niveau {self.niveau}!")
        print(f"PV max augmenté à {self.vie_max}")
    
    def gagner_argent(self, montant):
        """Ajoute de l'argent"""
        self.argent += montant
        print(f"{self.nom} a gagné {montant} pièces d'or!")
    
    def ajouter_objet(self, item, quantite=1):
        """Ajoute un objet à l'inventaire"""
        if item in self.inventaire:
            self.inventaire[item]["quantité"] += quantite
        else:
            self.inventaire[item] = {"quantité": quantite}
        print(f"{quantite} {item}(s) ajouté(s) à l'inventaire de {self.nom}.")
    
    def retirer_objet(self, item, quantite=1):
        """Retire un objet de l'inventaire"""
        if item in self.inventaire:
            self.inventaire[item]["quantité"] -= quantite
            if self.inventaire[item]["quantité"] <= 0:
                del self.inventaire[item]
    
    def attaquer(self, arme):
        """Calcule les dégâts basés sur l'arme"""
        arme = self.main['droite']
        
        if arme == 'hache':
            degats = 7
        elif arme == 'épée_fer':
            degats = 5
        elif arme == 'épée_premium':
            degats = 8
        elif arme == 'épée_or':
            degats = 10
        else:
            degats = 2  # À mains nues
        
        return degats
    
    def se_defendre(self):
        """Active le mode défense pour réduire les dégâts"""
        self.en_defense = True
    
    def subir_degats(self, degats):
        """Réduit la vie en fonction des dégâts"""
        if self.en_defense:
            degats = int(degats * self.reduction_defense)
            self.en_defense = False
        
        self.vie -= degats
        if self.vie < 0:
            self.vie = 0
        
        return degats
    
    def restaurer_pv(self, quantite):
        """Restaure des points de vie"""
        self.vie += quantite
        if self.vie > self.vie_max:
            self.vie = self.vie_max
    
    def utiliser_objet(self, item):
        """Utilise un objet de l'inventaire"""
        if item == "potion" and item in self.inventaire:
            if self.inventaire[item]["quantité"] > 0:
                self.restaurer_pv(5)
                self.retirer_objet(item, 1)
                return True
        return False
