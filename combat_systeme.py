"""
Système de Combat - Combats RPG avec défense et parade
"""
import pygame
import sys
import random

pygame.init()

class CombatSysteme:
    def __init__(self, personnage, ennemi, ecran, audio):
        self.personnage = personnage
        self.ennemi = ennemi
        self.ecran = ecran
        self.audio = audio
        
        self.bouton_attaquer = None
        self.bouton_defendre = None
        self.bouton_fuir = None
        self.bouton_potion = None
    
    def afficher_interface_combat(self):
        """Affiche l'interface de combat"""
        BLANC = (255, 255, 255)
        NOIR = (0, 0, 0)
        VERT = (0, 255, 0)
        ROUGE = (255, 0, 0)
        BLEU = (0, 0, 255)
        ORANGE = (255, 165, 0)
        GRIS = (100, 100, 100)
        GRIS_FONCE = (50, 50, 50)
        JAUNE = (255, 255, 0)
        
        LARGEUR = 1250
        HAUTEUR = 800
        
        police_grande = pygame.font.SysFont("Arial", 40)
        police_normale = pygame.font.SysFont("Arial", 30)
        police_petite = pygame.font.SysFont("Arial", 20)
        
        # Fond
        self.ecran.fill(GRIS_FONCE)
        
        # Titre
        titre = police_grande.render("⚔️ COMBAT ⚔️", True, JAUNE)
        titre_rect = titre.get_rect(center=(LARGEUR // 2, 30))
        self.ecran.blit(titre, titre_rect)
        
        # ===== ZONE JOUEUR =====
        pygame.draw.rect(self.ecran, BLEU, (50, 100, 550, 200), 3)
        nom_joueur = police_normale.render(f"Joueur: {self.personnage.nom}", True, BLEU)
        self.ecran.blit(nom_joueur, (70, 110))
        
        # Barre de vie du joueur
        barre_max = 450
        barre_joueur = (self.personnage.vie / 10) * barre_max
        pygame.draw.rect(self.ecran, GRIS, (70, 160, barre_max, 40))
        couleur = JAUNE if self.personnage.vie < 3 else VERT
        pygame.draw.rect(self.ecran, couleur, (70, 160, barre_joueur, 40))
        pygame.draw.rect(self.ecran, BLANC, (70, 160, barre_max, 40), 2)
        
        # Texte PV
        texte_pv = police_petite.render(f"{self.personnage.vie:.0f} / {self.personnage.vie_max} PV", True, BLANC)
        self.ecran.blit(texte_pv, (150, 175))
        
        # Stats joueur
        stats = police_petite.render(f"Niveau {self.personnage.niveau} | ATK: {self.personnage.attaquer('droite')}", True, BLANC)
        self.ecran.blit(stats, (70, 220))
        
        # État défense
        if self.personnage.en_defense:
            etat_defense = police_petite.render("🛡️ EN DÉFENSE!", True, JAUNE)
            self.ecran.blit(etat_defense, (300, 220))
        
        # ===== ZONE ENNEMI =====
        pygame.draw.rect(self.ecran, ROUGE, (650, 100, 550, 200), 3)
        nom_ennemi = police_normale.render(f"Ennemi: {self.ennemi.nom}", True, ROUGE)
        self.ecran.blit(nom_ennemi, (670, 110))
        
        # Barre de vie de l'ennemi
        barre_ennemi_max = 450
        barre_ennemi = (self.ennemi.points_vie / self.ennemi.points_vie_max) * barre_ennemi_max
        pygame.draw.rect(self.ecran, GRIS, (670, 160, barre_ennemi_max, 40))
        pygame.draw.rect(self.ecran, ROUGE, (670, 160, barre_ennemi, 40))
        pygame.draw.rect(self.ecran, BLANC, (670, 160, barre_ennemi_max, 40), 2)
        
        # Texte PV ennemi
        texte_pv_ennemi = police_petite.render(f"{self.ennemi.points_vie:.0f} / {self.ennemi.points_vie_max} PV", True, BLANC)
        self.ecran.blit(texte_pv_ennemi, (750, 175))
        
        # Stats ennemi
        stats_e = police_petite.render(f"Dégâts: {self.ennemi.degats}", True, BLANC)
        self.ecran.blit(stats_e, (670, 220))
        
        # État défense ennemi
        if self.ennemi.en_defense:
            etat_def_e = police_petite.render("🛡️ EN DÉFENSE!", True, JAUNE)
            self.ecran.blit(etat_def_e, (900, 220))
        
        # ===== ZONE D'ACTIONS =====
        pygame.draw.rect(self.ecran, NOIR, (0, 350, LARGEUR, 450))
        pygame.draw.line(self.ecran, BLANC, (0, 350), (LARGEUR, 350), 3)
        
        titre_actions = police_petite.render("Choisissez votre action:", True, JAUNE)
        self.ecran.blit(titre_actions, (50, 370))
        
        # Boutons
        self.bouton_attaquer = pygame.Rect(100, 450, 180, 70)
        self.bouton_defendre = pygame.Rect(320, 450, 180, 70)
        self.bouton_potion = pygame.Rect(540, 450, 180, 70)
        self.bouton_fuir = pygame.Rect(760, 450, 180, 70)
        
        # Afficher les boutons
        pygame.draw.rect(self.ecran, VERT, self.bouton_attaquer)
        pygame.draw.rect(self.ecran, ORANGE, self.bouton_defendre)
        pygame.draw.rect(self.ecran, BLEU, self.bouton_potion)
        pygame.draw.rect(self.ecran, ROUGE, self.bouton_fuir)
        
        # Textes des boutons
        txt_attaquer = police_normale.render("🗡️ Attaquer", True, NOIR)
        txt_defendre = police_normale.render("🛡️ Défendre", True, NOIR)
        txt_potion = police_normale.render("💊 Potion", True, NOIR)
        txt_fuir = police_normale.render("🏃 Fuir", True, NOIR)
        
        self.ecran.blit(txt_attaquer, (self.bouton_attaquer.x + 15, self.bouton_attaquer.y + 18))
        self.ecran.blit(txt_defendre, (self.bouton_defendre.x + 15, self.bouton_defendre.y + 18))
        self.ecran.blit(txt_potion, (self.bouton_potion.x + 20, self.bouton_potion.y + 18))
        self.ecran.blit(txt_fuir, (self.bouton_fuir.x + 30, self.bouton_fuir.y + 18))
    
    def afficher_combat(self):
        """Boucle principale du combat"""
        en_cours = True
        
        while en_cours:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:
                    pos_souris = pygame.mouse.get_pos()
                    
                    # Clic sur ATTAQUER
                    if self.bouton_attaquer.collidepoint(pos_souris):
                        # Joueur attaque
                        degats = self.personnage.attaquer(self.personnage.main['droite'])
                        degats_appliques = self.ennemi.subir_degats(degats)
                        self.audio.jouer_son("coup")
                        
                        # Vérifier si ennemi est mort
                        if self.ennemi.points_vie <= 0:
                            print(f"{self.ennemi.nom} est mort!")
                            xp_gagnee = self.ennemi.recompense * 10
                            self.personnage.gagner_experience(xp_gagnee)
                            self.personnage.gagner_argent(self.ennemi.recompense)
                            
                            # Loot
                            loot = self.ennemi.obtenir_loot()
                            for item, quantite in loot.items():
                                if item == "or":
                                    self.personnage.argent += quantite
                                else:
                                    self.personnage.ajouter_objet(item, quantite)
                            
                            self.audio.jouer_son("victoire")
                            return "victoire"
                        
                        # Ennemi attaque
                        self.ennemi.se_defendre() if random.random() < 0.3 else None
                        self.ennemi.attaquer(self.personnage)
                        self.audio.jouer_son("coup_ennemi")
                        
                        # Vérifier si joueur est mort
                        if self.personnage.vie <= 0:
                            self.audio.jouer_son("defaite")
                            return "defaite"
                    
                    # Clic sur DÉFENDRE
                    elif self.bouton_defendre.collidepoint(pos_souris):
                        self.personnage.se_defendre()
                        print(f"{self.personnage.nom} se met en défense!")
                        self.audio.jouer_son("defense")
                        
                        # Ennemi attaque quand même
                        self.ennemi.attaquer(self.personnage)
                        self.audio.jouer_son("coup_ennemi")
                        
                        if self.personnage.vie <= 0:
                            self.audio.jouer_son("defaite")
                            return "defaite"
                    
                    # Clic sur POTION
                    elif self.bouton_potion.collidepoint(pos_souris):
                        if "potion" in self.personnage.inventaire and self.personnage.inventaire["potion"]["quantité"] > 0:
                            ancien_pv = self.personnage.vie
                            self.personnage.utiliser_objet("potion")
                            print(f"{self.personnage.nom} a utilisé une potion! +{int(self.personnage.vie - ancien_pv)} PV")
                            self.audio.jouer_son("potion")
                            
                            # Ennemi attaque
                            self.ennemi.attaquer(self.personnage)
                            self.audio.jouer_son("coup_ennemi")
                            
                            if self.personnage.vie <= 0:
                                self.audio.jouer_son("defaite")
                                return "defaite"
                        else:
                            print("Pas de potion!")
                    
                    # Clic sur FUIR
                    elif self.bouton_fuir.collidepoint(pos_souris):
                        print(f"{self.personnage.nom} a fui le combat!")
                        self.audio.jouer_son("fuite")
                        return "fuite"
            
            self.afficher_interface_combat()
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()
