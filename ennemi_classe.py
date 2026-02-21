"""
Classe Ennemi - Adversaires du jeu
"""
import random
import pygame

pygame.init()

class Ennemi:
    def __init__(self, nom, points_vie, degats, recompense, x, y, zone, loot=None):
        self.nom = nom
        self.points_vie = points_vie
        self.points_vie_max = points_vie
        self.degats = degats
        self.recompense = recompense
        self.loot = loot or {}
        self.rect = pygame.Rect(x, y, 50, 50)
        self.zone = zone
        self.vitesse = 50
        self.direction = [random.choice([-1, 1]), random.choice([-1, 1])]
        
        # Système de défense
        self.en_defense = False
        self.reduction_defense = 0.5
        self.chance_parade = 0.3  # 30% de chance de parer
    
    def attaquer(self, personnage):
        """L'ennemi attaque le personnage"""
        # Chance de parer l'attaque
        if random.random() < self.chance_parade:
            print(f"{self.nom} a paré l'attaque!")
            return 0  # Aucun dégât
        
        # Sinon attaque normale
        degats_finaux = self.degats
        if personnage.en_defense:
            degats_finaux = int(self.degats * self.reduction_defense)
            personnage.en_defense = False
            print(f"{self.nom} attaque, mais {personnage.nom} se défend!")
        
        personnage.vie -= degats_finaux
        print(f"{self.nom} attaque {personnage.nom} et inflige {degats_finaux} dégâts!")
        print(f"Il reste {max(0, personnage.vie)} points de vie à {personnage.nom}.")
        
        return degats_finaux
    
    def se_defendre(self):
        """L'ennemi se met en défense"""
        self.en_defense = True
        print(f"{self.nom} se met en position défensive!")
    
    def subir_degats(self, degats):
        """L'ennemi reçoit des dégâts"""
        # Chance d'esquive ou parade
        if random.random() < self.chance_parade:
            print(f"{self.nom} a esquivé l'attaque!")
            return 0
        
        # Réduction de défense si actif
        if self.en_defense:
            degats = int(degats * self.reduction_defense)
            self.en_defense = False
            print(f"{self.nom} se défend et réduit les dégâts!")
        
        self.points_vie -= degats
        print(f"{self.nom} subit {degats} dégâts!")
        print(f"Il reste {max(0, self.points_vie)} points de vie au {self.nom}.")
        
        return degats
    
    def deplacer_aleatoirement(self, dt):
        """Déplace l'ennemi aléatoirement dans sa zone"""
        # 10% de chance de changer de direction
        if random.random() < 0.1:
            self.direction = [random.choice([-1, 1]), random.choice([-1, 1])]
        
        # Déplacer
        self.rect.x += self.direction[0] * dt
        self.rect.y += self.direction[1] * dt
        
        # Limiter à la zone
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
    
    def obtenir_loot(self):
        """Retourne le loot de l'ennemi"""
        return self.loot.copy()
