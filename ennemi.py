import time
import threading
import random
import pygame

pygame.init()


from pnj import PNJ

class Ennemi(PNJ):
    def __init__(self, nom, point_de_vie, degats, recompense, x, y, zone, loot=None):
        super().__init__(nom, point_de_vie, recompense)
        self.degats = degats
        self.type = "ennemi"
        self.rect = pygame.Rect(x, y, 50, 50)
        self.loot = loot or {}  # Dictionnaire du loot à dropper
        self.vitesse = 100
        self.direction = [1, 0] # Déplacement vers la droite par défaut
        self.zone = zone        # Définir une zone pour l'ennemi


    def attaquer(self, perso):
        perso.vie -= self.degats
        print(f"{self.nom} attaque {perso.nom}.")
        print(f"Il reste {perso.vie} points de vie à {perso.nom}.")

    def obtenir_loot(self):
        """Retourne le loot dropper par cet ennemi"""
        return self.loot.copy()

    def deplacer_aleatoirement(self, dt):       # dt -> delta temps = temps écoulé entre deux itérations
        # 10% de chance de changer de direction
        if random.random() < 0.1:
            self.direction = [random.choice([-1, 1]), random.choice([-1, 1])]

        # Déplacer l'ennemi
        self.rect.x += self.direction[0] * dt
        self.rect.y += self.direction[1] * dt

        # Empêcher l'ennemi de sortir de sa zone
        if self.rect.left < self.zone.left:
            self.rect.left = self.zone.left
            self.direction[0] *= -1
        if self.rect.right > self.zone.right:
            self.rect.right = self.zone.right
            self.direction[0] *= -1
        if self.rect.top < self.zone.top:
            self.rect.top = self.zone.top
            self.direction[1] *= -1
        if self.rect.bottom > self.zone.bottom:
            self.rect.bottom = self.zone.bottom
            self.direction[1] *= -1

    @staticmethod                    # Méthode statique = appartient à la classe elle-même plutôt qu'a une instance de cette classe. La méthode génère juste un ennemi en fonction de la zone, pas besoin d'accès aux attributs; elle est lié à la classe Ennemi mais ne dépend pas d'une instance.
    def generer_ennemis_zone(zone):
        return random.choice(zone)

'''#Ennemis !!!! ATTENTION JE N'AI PAS MIS LES POSITIONS X ET Y !!!!!
Foret_Sombre = [
    Ennemi("Loup", point_de_vie=8, degats=3, recompense={"or": random.randint(0,5)}, None),
    Ennemi("Sorcière", point_de_vie=20, degats=5, recompense={"or": random.randint(10,15), "enchantement":1}, None),
    Ennemi("Gobelin", point_de_vie=15, degats=4, recompense={"or": random.randint(5,10), "potion":1}, None),
]

#Ennemis
Montagne = [
    Ennemi("Troll", point_de_vie=30, degats=6, recompense={"or": random.randint(15,20),"hache":1}, None),
    Ennemi("Roc", point_de_vie=25, degats=4, recompense={"or": random.randint(10,15)}, None),   #Roc = Aigle avec une tête muté -> C'est pas un rocher
    Ennemi("Dragon", point_de_vie=80, degats=10, recompense={"or": random.randint(90,100),"epee_legendaire":1}, None),
]

#Ennemis
Village_Abandonne = [
    Ennemi("Zombie", point_de_vie=15, degats=3, recompense={"or": random.randint(5,10)}, None),
    Ennemi("Fantome", point_de_vie=10, degats=2, recompense={"or": random.randint(0,5)}, "Effrayer"),
    Ennemi("Bandit", point_de_vie=25, degats=5, recompense={"or": random.randint(10,15),"bracelet":1}, None),
]

#Ennemis
Desert = [
    Ennemi("Scorpion_geant", point_de_vie=15, degats=4, recompense={"or": random.randint(5,10), "aiguille_scorpion":1}, None),
    Ennemi("Voleur_de_caverne", point_de_vie=20, degats=6, recompense={"or": random.randint(10,15)}, None),
    Ennemi("Mirage", point_de_vie=8, degats=1, recompense={"or": random.randint(0,5)}, "Teleportation"),
]

#Ennemis
Plaines_Verdoyantes = [
    Ennemi("Bandit_de_la_route", point_de_vie=25, degats=5, recompense={"or": random.randint(5,10)}, None),
    Ennemi("Fee_malicieuse", point_de_vie=15, degats=3, recompense={"or": random.randint(0,8), "potion_guerison":1}, "Guerison"),
    Ennemi("Slime", point_de_vie=20, degats=4, recompense={"or": random.randint(0,5)}, None),
]

#Ennemis
Caverne = [
    Ennemi("Chauve-souris_geante", point_de_vie=10, degats=2, recompense={"or": random.randint(0,5), "potion":1}, None),
    Ennemi("Golem_de_pierre", point_de_vie=40, degats=8, recompense={"or": random.randint(20,25), "pierre_précieuse":1}, None),
    Ennemi("Esprit_des_cavernes", point_de_vie=30, degats=6, recompense={"or": random.randint(15,20), "enchantement":1}, "Paralyse"),
]

#Ennemis
Chateau_en_Ruines = [
    Ennemi("Chevalier_fantome", point_de_vie=35, degats=6, recompense={"or": random.randint(25,30), "epee":1}, None),
    Ennemi("Araigne_geante", point_de_vie=25, degats=5, recompense={"or": random.randint(15,20), "potion_venimeuse":1}, None),
    Ennemi("Sorcier", point_de_vie=30, degats=7, recompense={"or": random.randint(35,40), "livre_de_sort":1}, "Brulure"),       #Livre de sort: sert a stocker tous les sorts que tu pourras lancé quand le perso aura l'objet en main.
]'''