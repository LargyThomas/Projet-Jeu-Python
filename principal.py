# ===== CONSTANTES, COULEURS, POLICES, ÉCRAN =====
LARGEUR_FENETRE = 1250
HAUTEUR_FENETRE = 800
COULEUR_FOND = (34, 139, 200)  # Bleu ciel

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
GRIS = (200, 200, 200)
GRIS_CLAIR = (100, 100, 100)
GRIS_FONCE = (50, 50, 50)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)
ORANGE = (255, 165, 0)

# Polices
import pygame
pygame.init()
police = pygame.font.Font(None, 36)
police_hud = pygame.font.Font(None, 24)
police_titre = pygame.font.Font(None, 48)
police_petit = pygame.font.Font(None, 20)

# Écran
ecran = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
pygame.display.set_caption("Jeu RPG - Aventure Épique")
def afficher_carte_interactive(ecran, police):
    ecran.fill((80, 120, 160))
    titre = police.render("Carte interactive", True, (255,255,255))
    ecran.blit(titre, (LARGEUR_FENETRE//2 - titre.get_width()//2, 80))
    # Affichage simple, à compléter avec la vraie carte
    txt = police.render("(Carte à venir)", True, (255,255,255))
    ecran.blit(txt, (LARGEUR_FENETRE//2 - txt.get_width()//2, 200))
# ===== SYSTÈME DE SUCCÈS =====
succes = {
    "Premier combat": False,
    "100 or": False,
    "Quête terminée": False,
    "Bestiaire rempli": False
}

def verifier_succes(joueur, gestionnaire_quetes, compteur_bandits_vaincus, compteur_loups_vaincus):
    if not succes["Premier combat"] and (compteur_bandits_vaincus > 0 or compteur_loups_vaincus > 0):
        succes["Premier combat"] = True
        mettre_a_jour_notification("Succès débloqué : Premier combat!")
    if not succes["100 or"] and joueur.argent >= 100:
        succes["100 or"] = True
        mettre_a_jour_notification("Succès débloqué : 100 or!")
    if not succes["Quête terminée"] and gestionnaire_quetes.get_stats_quetes()["completees"] > 0:
        succes["Quête terminée"] = True
        mettre_a_jour_notification("Succès débloqué : Quête terminée!")
    # Bestiaire rempli : à compléter avec la logique bestiaire

# ===== IMPORTS =====
import pygame
import sys
import json
import os
from personnage import Personnage
from ennemi_classe import Ennemi
from combat_systeme import CombatSysteme
from systeme_sauvegarde import SystemeSauvegarde
from quete_systeme import Quete, GestionnaireQuetes
from interface_audio import InterfaceAudio

# ===== SYSTÈME SAUVEGARDE =====
sauvegarde_systeme = SystemeSauvegarde("sauvegardes")

# ===== BESTIAIRE =====
bestiaire = set()

def ajouter_monstre_bestiaire(nom):
    if nom not in bestiaire:
        bestiaire.add(nom)
        mettre_a_jour_notification(f"Nouveau monstre dans le bestiaire : {nom}")

def afficher_bestiaire(ecran, police):
    ecran.fill((60, 60, 80))
    titre = police.render("Bestiaire", True, (255,255,255))
    ecran.blit(titre, (LARGEUR_FENETRE//2 - titre.get_width()//2, 80))
    y = 160
    for nom in sorted(bestiaire):
        txt = police.render(nom, True, (200,200,255))
        ecran.blit(txt, (LARGEUR_FENETRE//2 - txt.get_width()//2, y))
        y += 40

# ===== FENÊTRE PARAMÈTRES AVANCÉE =====
def afficher_fenetre_parametres(ecran, police, police_titre, touches_config, volume_musique, volume_effets, langue, menu_ouvert):
    # Menu paramètres simplifié, sans modification des touches
    ecran.fill((40, 40, 60))
    titre = police_titre.render("Paramètres", True, (255,255,255))
    ecran.blit(titre, (LARGEUR_FENETRE//2 - titre.get_width()//2, 30))
    boutons = []
    y = 120
    x = LARGEUR_FENETRE//2 - 350
    ecart = 70

    # Volume musique
    txt = police.render(f"Volume Musique : {int(volume_musique*100)}%", True, (200,200,255))
    rect = pygame.Rect(x, y, 700, 55)
    pygame.draw.rect(ecran, (80,80,120), rect, border_radius=12)
    ecran.blit(txt, (x+40, y+15))
    boutons.append(("volume_musique", rect))
    y += ecart

    # Volume effets
    txt = police.render(f"Volume Effets : {int(volume_effets*100)}%", True, (200,255,200))
    rect = pygame.Rect(x, y, 700, 55)
    pygame.draw.rect(ecran, (80,120,80), rect, border_radius=12)
    ecran.blit(txt, (x+40, y+15))
    boutons.append(("volume_effets", rect))
    y += ecart

    # Langue
    txt = police.render(f"Langue : {langue}", True, (255,255,200))
    rect = pygame.Rect(x, y, 700, 55)
    pygame.draw.rect(ecran, (120,120,80), rect, border_radius=12)
    ecran.blit(txt, (x+40, y+15))
    boutons.append(("langue", rect))
    y += ecart

    # Mode Fenêtre/Plein écran
    txt = police.render("Mode : Fenêtre/Plein écran", True, (255,220,180))
    rect = pygame.Rect(x, y, 700, 55)
    pygame.draw.rect(ecran, (120,100,80), rect, border_radius=12)
    ecran.blit(txt, (x+40, y+15))
    boutons.append(("plein_ecran", rect))
    y += ecart

    # Réinitialiser options
    txt = police.render("Réinitialiser toutes les options", True, (255,180,180))
    rect = pygame.Rect(x, y, 700, 55)
    pygame.draw.rect(ecran, (180,100,100), rect, border_radius=12)
    ecran.blit(txt, (x+40, y+15))
    boutons.append(("reset_options", rect))
    y += ecart

    # Accessibilité
    txt = police.render("Accessibilité (taille police, contraste)", True, (180,255,180))
    rect = pygame.Rect(x, y, 700, 55)
    pygame.draw.rect(ecran, (100,180,100), rect, border_radius=12)
    ecran.blit(txt, (x+40, y+15))
    boutons.append(("accessibilite", rect))
    y += ecart

    # Crédits
    txt = police.render("Crédits", True, (255,255,255))
    rect = pygame.Rect(x, y, 340, 50)
    pygame.draw.rect(ecran, (100,100,100), rect, border_radius=10)
    ecran.blit(txt, (x+30, y+12))
    boutons.append(("credits", rect))

    # Aide
    txt = police.render("Aide", True, (255,255,255))
    rect2 = pygame.Rect(x+360, y, 340, 50)
    pygame.draw.rect(ecran, (100,100,100), rect2, border_radius=10)
    ecran.blit(txt, (x+30+360, y+12))
    boutons.append(("aide", rect2))
    y += 60

    # Retour
    txt = police.render("Retour", True, (255,255,255))
    rect = pygame.Rect(x, y, 700, 55)
    pygame.draw.rect(ecran, (150,80,80), rect, border_radius=12)
    ecran.blit(txt, (x+280, y+15))
    boutons.append(("retour", rect))

    return boutons
# ===== FONCTION AFFICHAGE MENU PRINCIPAL =====
def afficher_menu_principal(ecran, police_titre, sauvegarde_existe):
    ecran.fill((34, 139, 200))
    titre = police_titre.render("Aventure Épique", True, (255,255,255))
    ecran.blit(titre, (LARGEUR_FENETRE//2 - titre.get_width()//2, 100))

    boutons = []
    y = 250
    w, h = 350, 60
    x = LARGEUR_FENETRE//2 - w//2
    ecart = 20

    if sauvegarde_existe:
        txt = police.render("Continuer", True, (0,0,0))
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(ecran, (200,255,200), rect)
        ecran.blit(txt, (x + w//2 - txt.get_width()//2, y + h//2 - txt.get_height()//2))
        boutons.append(("continuer", rect))
        y += h + ecart

    txt = police.render("Nouvelle Partie", True, (0,0,0))
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(ecran, (200,200,255), rect)
    ecran.blit(txt, (x + w//2 - txt.get_width()//2, y + h//2 - txt.get_height()//2))
    boutons.append(("nouvelle", rect))
    y += h + ecart

    if sauvegarde_existe:
        txt = police.render("Reset (Supprimer Sauvegarde)", True, (0,0,0))
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(ecran, (255,200,200), rect)
        ecran.blit(txt, (x + w//2 - txt.get_width()//2, y + h//2 - txt.get_height()//2))
        boutons.append(("reset", rect))
        y += h + ecart

    # Icône écrou pour paramètres
    ecrou = pygame.image.load('Asset/ui/settings_gear.png') if os.path.exists('Asset/ui/settings_gear.png') else None
    if ecrou:
        ecrou = pygame.transform.scale(ecrou, (50,50))
        rect = pygame.Rect(x + w//2 - 25, y, 50, 50)
        ecran.blit(ecrou, (x + w//2 - 25, y))
        boutons.append(("parametres", rect))
        y += 50 + ecart
    else:
        txt = police.render("Paramètres", True, (0,0,0))
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(ecran, (220,220,220), rect)
        ecran.blit(txt, (x + w//2 - txt.get_width()//2, y + h//2 - txt.get_height()//2))
        boutons.append(("parametres", rect))
        y += h + ecart

    txt = police.render("Quitter", True, (0,0,0))
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(ecran, (180,180,180), rect)
    ecran.blit(txt, (x + w//2 - txt.get_width()//2, y + h//2 - txt.get_height()//2))
    boutons.append(("quitter", rect))

    return boutons
import pygame
import sys
import json
import os

from personnage import Personnage
from ennemi_classe import Ennemi
from combat_systeme import CombatSysteme
from systeme_sauvegarde import SystemeSauvegarde
from quete_systeme import Quete, GestionnaireQuetes
from interface_audio import InterfaceAudio
def afficher_defaite(ecran, police_titre):
    ecran.fill((30,0,0))
    txt = police_titre.render("Défaite !", True, (255,80,80))
    ecran.blit(txt, (LARGEUR_FENETRE//2 - txt.get_width()//2, 250))
    txt2 = police_titre.render("Vous avez perdu...", True, (255,255,255))
    ecran.blit(txt2, (LARGEUR_FENETRE//2 - txt2.get_width()//2, 350))
    txt3 = police_titre.render("Appuyez pour quitter", True, (255,255,255))
    ecran.blit(txt3, (LARGEUR_FENETRE//2 - txt3.get_width()//2, 450))

    # Rien d'autre à afficher ici, la fonction doit juste afficher l'écran de défaite.


    # ...existing code...

# ===== PERSONNAGE PRINCIPAL =====
# ===== VARIABLES PARAMÈTRES =====
volume_musique = 0.5
volume_effets = 0.5
langue = "FR"
menu_ouvert = None

donnees_chargees = sauvegarde_systeme.charger_partie()
if donnees_chargees:
    sauvegarde_existe = True
    # Charger une partie existante
    joueur = Personnage(donnees_chargees["nom_joueur"])
    joueur.niveau = donnees_chargees["niveau"]
    joueur.experience = donnees_chargees["experience"]
    joueur.vie = donnees_chargees["vie"]
    joueur.vie_max = donnees_chargees["vie_max"]
    joueur.argent = donnees_chargees["argent"]
    joueur.inventaire = donnees_chargees["inventaire"]
    joueur.tenue = donnees_chargees["tenue"]
    joueur.main = donnees_chargees["main"]
    pos_joueur_x = donnees_chargees.get("position_x", 100)
    pos_joueur_y = donnees_chargees.get("position_y", 400)
    print(f"[OK] Partie chargee: {joueur.nom} niveau {joueur.niveau}")
else:
    sauvegarde_existe = False
    # Créer un nouveau joueur
    joueur = Personnage("Arthur")
    joueur.inventaire = {
        "potion": {"quantité": 3},
        "épée_fer": {"quantité": 1},
        "bouclier": {"quantité": 1},
    }
    pos_joueur_x = 100
    pos_joueur_y = 400
    print("[OK] Nouveau joueur cree")

# Charger l'image du joueur
image_joueur = pygame.image.load('Asset/Cute_Fantasy_Free/Player/Player_Actions.png').convert_alpha()
image_joueur = pygame.transform.scale(image_joueur, (40, 50))
vitesse_joueur = 8
rect_joueur = image_joueur.get_rect()
rect_joueur.topleft = (pos_joueur_x, pos_joueur_y)

# Limite de déplacement haut (sous le HUD)
LIMITE_HAUT = 70
LIMITE_BAS = HAUTEUR_FENETRE - 50
LIMITE_GAUCHE = 0
LIMITE_DROITE = LARGEUR_FENETRE - 40

# ===== PNJ =====
image_pnj_1 = pygame.image.load('Asset/Cute_Fantasy_Free/Player/Player.png').convert_alpha()
image_pnj_1 = pygame.transform.scale(image_pnj_1, (50, 50))

pos_pnj_1_x = 200
pos_pnj_1_y = 150
rect_pnj_1 = image_pnj_1.get_rect()
rect_pnj_1.topleft = (pos_pnj_1_x, pos_pnj_1_y)

# PNJ Marchand
image_marchand = pygame.image.load('Asset/Cute_Fantasy_Free/Player/Player.png').convert_alpha()
image_marchand = pygame.transform.scale(image_marchand, (50, 50))
pos_marchand_x = 900
pos_marchand_y = 200
rect_marchand = image_marchand.get_rect()
rect_marchand.topleft = (pos_marchand_x, pos_marchand_y)

# Rayon d'interaction augmenté
RAYON_INTERACTION = 100

dialogues_pnj = {
    "pnj1": [
        {
            "texte": "Salut aventurier! Que puis-je faire pour toi?",
            "reponses": {
                "1": {"texte": "Parlez-moi de ce monde", "action": "discuter"},
                "2": {"texte": "Au revoir", "action": "quitter"}
            }
        },
        {
            "texte": "Ce régne est rempli de mystères et de dangers!",
            "reponses": None
        }
    ],
    "marchand": [
        {
            "texte": "Bienvenue! J'ai d'excellentes affaires pour toi!",
            "reponses": {
                "1": {"texte": "Potion de Vie (50 or)", "action": "acheter_potion"},
                "2": {"texte": "Épée Premium (100 or)", "action": "acheter_epee"},
                "3": {"texte": "M'en aller", "action": "quitter"}
            }
        },
        {
            "texte": "À bientôt, voyageur!",
            "reponses": None
        }
    ]
}

# Positions des PNJ
positions_pnj = {
    "pnj1": (pos_pnj_1_x, pos_pnj_1_y),
    "marchand": (pos_marchand_x, pos_marchand_y),
}

# ===== SYSTEME AUDIO =====
audio = InterfaceAudio()

# ===== COMPTEURS ENNEMIS POUR QUÊTES =====
compteur_bandits_vaincus = 0
compteur_loups_vaincus = 0
compteur_collectibles = 0

# ===== OBJETS =====
image_objet = pygame.image.load('Asset/Retro_Interior/canap.png').convert_alpha()
image_objet = pygame.transform.scale(image_objet, (50, 30))

pos_objet_x = 300
pos_objet_y = 500
rect_objet = image_objet.get_rect()
rect_objet.topleft = (pos_objet_x, pos_objet_y)

# ===== NOTIFICATIONS =====
texte_notification = ""
temps_notification = 0
duree_notification = 3
notification_active = False
notifications_differees = []

def afficher_notification():
    """Affiche les notifications temporaires"""
    global texte_notification, temps_notification, notification_active
    if notification_active:
        pygame.draw.rect(ecran, GRIS_CLAIR, (1000, 70, 240, 40))
        rendu_notification = police_petit.render(texte_notification, True, NOIR)
        ecran.blit(rendu_notification, (1010, 80))
        
        if pygame.time.get_ticks() - temps_notification > duree_notification * 1000:
            notification_active = False
            texte_notification = ""
    else:
        texte_notification = ""

def mettre_a_jour_notification(texte):
    """Crée une nouvelle notification"""
    global texte_notification, temps_notification, notification_active
    texte_notification = texte
    temps_notification = pygame.time.get_ticks()
    notification_active = True

def ajouter_notification_differee(texte):
    """Ajoute une notification à la file"""
    global notifications_differees
    notifications_differees = [texte]

def afficher_notifications_differees():
    """Affiche les notifications en attente"""
    global texte_notification, temps_notification, notification_active, notifications_differees
    if notifications_differees:
        texte_notification = " | ".join(notifications_differees)
        temps_notification = pygame.time.get_ticks()
        notification_active = True
        notifications_differees = []

# ===== QUÊTES =====
gestionnaire_quetes = GestionnaireQuetes()

# Ajouter des quêtes
q1 = Quete("Sauver le village", 
           "Éliminer 3 bandits qui terrorisent le village", 
           "Combat", 
           {"Bandits_vaincus"}, 
           200, 
           3)
gestionnaire_quetes.ajouter_quete(q1)

q2 = Quete("Chasser le loup", 
           "Tuer le loup qui terrorise les fermes", 
           "Combat", 
           {"Loups_vaincus"}, 
           100, 
           1)
gestionnaire_quetes.ajouter_quete(q2)

q3 = Quete("Collecte de ressources", 
           "Collecter 5 potions dans le monde", 
           "Collecte", 
           {"Ressources_collectees"}, 
           150, 
           5)
gestionnaire_quetes.ajouter_quete(q3)

quete_selectionnee = None

# ===== ENNEMIS =====
zone_ennemi_bandit = pygame.Rect(300, 300, 400, 150)
zone_ennemi_loup = pygame.Rect(600, 400, 100, 300)

ennemis = [
    Ennemi("Bandit", 20, 3, 10, 300, 300, zone_ennemi_bandit, 
           loot={"or": 50, "épée_fer": 1}),
    Ennemi("Loup", 15, 2, 5, 600, 400, zone_ennemi_loup,
           loot={"or": 30, "potion": 1})
]

ecran_combat = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
pygame.display.set_caption("Combat RPG")

# ===== FONCTIONS =====

# ===== PAGE CRÉDITS =====
def afficher_page_credits(ecran, police_titre, police):
    ecran.fill((30, 30, 60))
    titre = police_titre.render("Crédits", True, (255,255,255))
    ecran.blit(titre, (LARGEUR_FENETRE//2 - titre.get_width()//2, 80))
    y = 180
    credits = [
        "Développement : Votre Nom",
        "Graphismes : Asset sources",
        "Musique : Asset sources",
        "Remerciements : Communauté Python, Pygame",
        "Projet personnel 2024"
    ]
    for ligne in credits:
        txt = police.render(ligne, True, (200,200,255))
        ecran.blit(txt, (LARGEUR_FENETRE//2 - txt.get_width()//2, y))
        y += 50
    txt_retour = police.render("Appuyez sur une touche ou cliquez pour revenir", True, (255,180,180))
    ecran.blit(txt_retour, (LARGEUR_FENETRE//2 - txt_retour.get_width()//2, 650))

# ===== PAGE AIDE =====
def afficher_page_aide(ecran, police_titre, police):
    ecran.fill((60, 60, 30))
    titre = police_titre.render("Aide", True, (255,255,255))
    ecran.blit(titre, (LARGEUR_FENETRE//2 - titre.get_width()//2, 80))
    y = 180
    aide = [
        "Déplacements : ZQSD",
        "Inventaire : TAB",
        "Quêtes : P",
        "Interagir : E",
        "Pause/Menu : ESC",
        "Sauvegarde : Ctrl+S",
        "Collectez, combattez, explorez!"
    ]
    for ligne in aide:
        txt = police.render(ligne, True, (200,255,200))
        ecran.blit(txt, (LARGEUR_FENETRE//2 - txt.get_width()//2, y))
        y += 40
    txt_retour = police.render("Appuyez sur une touche ou cliquez pour revenir", True, (255,180,180))
    ecran.blit(txt_retour, (LARGEUR_FENETRE//2 - txt_retour.get_width()//2, 650))

def calcul_distance(pos1, pos2):
    """Calcule la distance entre deux points"""
    distance = ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5
    return distance

def joueur_proche_pnj(pos_pnj, pos_joueur, rayon=RAYON_INTERACTION):
    """Vérifie si le joueur est assez proche d'un PNJ"""
    distance = calcul_distance(pos_pnj, pos_joueur)
    return distance <= rayon

def afficher_dialogue(ecran, texte, reponses):
    """Affiche un dialogue avec le joueur"""
    police_dialogue = pygame.font.Font(None, 28)
    
    # Boîte de dialogue du PNJ
    pygame.draw.rect(ecran, GRIS_CLAIR, (50, 650, 600, 50), 0)
    pygame.draw.rect(ecran, BLANC, (50, 650, 600, 50), 2)
    
    # Texte du PNJ
    rendu_texte = police_dialogue.render(texte, True, BLANC)
    ecran.blit(rendu_texte, (65, 658))
    
    # Afficher les réponses
    if reponses:
        pos_y = HAUTEUR_FENETRE - 200
        for cle, reponse in reponses.items():
            # Boîte pour chaque réponse
            pygame.draw.rect(ecran, GRIS_CLAIR, (650, pos_y, 550, 40), 0)
            pygame.draw.rect(ecran, BLANC, (650, pos_y, 550, 40), 2)
            
            # Texte de la réponse
            rendu_reponse = police_dialogue.render(f"{cle}: {reponse['texte']}", True, BLANC)
            ecran.blit(rendu_reponse, (660, pos_y + 8))
            
            pos_y += 50

def traiter_action(action):
    """Traite les actions des dialogues"""
    if action == "acheter_epee":
        if joueur.argent >= 100:
            joueur.argent -= 100
            joueur.ajouter_objet("épée_premium", 1)
            ajouter_notification_differee("Épée achetée pour 100 or!")
            audio.jouer_son("achat")
        else:
            ajouter_notification_differee("Pas assez d'argent!")
            audio.jouer_son("erreur")
    
    elif action == "acheter_potion":
        if joueur.argent >= 50:
            joueur.argent -= 50
            joueur.ajouter_objet("potion", 1)
            ajouter_notification_differee("Potion achetée pour 50 or!")
            audio.jouer_son("achat")
        else:
            ajouter_notification_differee("Pas assez d'argent!")
            audio.jouer_son("erreur")
    
    elif action == "discuter":
        print("Vous discutez avec le PNJ.")
    elif action == "quitter":
        print("Vous partez.")

def afficher_hud():
    """Affiche le HUD avec les stats du joueur"""
    # Fond du HUD
    pygame.draw.rect(ecran, GRIS_FONCE, (0, 0, LARGEUR_FENETRE, 60))
    pygame.draw.line(ecran, BLANC, (0, 60), (LARGEUR_FENETRE, 60), 2)
    
    # Barre de vie
    barre_vie_max = 200
    pv_joueur_normalise = min((joueur.vie / 10) * barre_vie_max, barre_vie_max)
    pygame.draw.rect(ecran, GRIS_CLAIR, (10, 20, barre_vie_max, 20))
    couleur_vie = ROUGE if joueur.vie < 3 else VERT
    pygame.draw.rect(ecran, couleur_vie, (10, 20, pv_joueur_normalise, 20))
    pygame.draw.rect(ecran, BLANC, (10, 20, barre_vie_max, 20), 2)
    
    # Texte PV
    texte_pv = police_hud.render(f"PV: {joueur.vie:.1f}/10", True, BLANC)
    ecran.blit(texte_pv, (220, 20))
    
    # Niveau et XP
    texte_niveau = police_hud.render(f"Niveau: {joueur.niveau}", True, JAUNE)
    ecran.blit(texte_niveau, (400, 20))
    
    seuil_xp = joueur.niveau * 100
    texte_xp = police_hud.render(f"XP: {joueur.experience}/{seuil_xp}", True, BLEU)
    ecran.blit(texte_xp, (550, 20))
    
    # Argent
    texte_argent = police_hud.render(f"Or: {joueur.argent}", True, ORANGE)
    ecran.blit(texte_argent, (800, 20))
    
    # Nom du joueur
    texte_nom = police_hud.render(f"{joueur.nom}", True, BLANC)
    ecran.blit(texte_nom, (1050, 20))

def afficher_inventaire():
    """Affiche l'inventaire du joueur"""
    # Fond de l'inventaire
    pygame.draw.rect(ecran, GRIS_CLAIR, (50, 80, 500, 650))
    pygame.draw.rect(ecran, BLANC, (50, 80, 500, 650), 3)
    
    # Titre
    texte_titre = police.render("[INV] INVENTAIRE", True, NOIR)
    ecran.blit(texte_titre, (150, 100))
    
    # Items
    pos_y = 150
    for item, infos in joueur.inventaire.items():
        # Icône + texte
        texte_item = police_petit.render(f"• {item}: {infos['quantité']}", True, NOIR)
        ecran.blit(texte_item, (80, pos_y))
        
        # Séparateur
        pygame.draw.line(ecran, BLANC, (70, pos_y + 25), (530, pos_y + 25), 1)
        pos_y += 50
    
    # Instructions
    texte_info = police_petit.render("Appuie TAB pour fermer", True, ROUGE)
    ecran.blit(texte_info, (130, 700))

def afficher_menu_quetes():
    """Affiche le menu des quêtes"""
    toutes_quetes = gestionnaire_quetes.get_toutes_quetes()
    
    pygame.draw.rect(ecran, GRIS_CLAIR, (50, 80, 700, 650))
    pygame.draw.rect(ecran, BLANC, (50, 80, 700, 650), 3)
    
    # Titre
    texte_titre = police.render("[QUETES]", True, NOIR)
    ecran.blit(texte_titre, (200, 100))
    
    pos_y = 150
    
    # Quêtes non commencées
    if toutes_quetes["non_commencee"]:
        texte_cat = police_petit.render("Non commencées:", True, ORANGE)
        ecran.blit(texte_cat, (70, pos_y))
        pos_y += 30
        
        for quete in toutes_quetes["non_commencee"]:
            texte_quete = police_petit.render(f"• {quete.nom}", True, NOIR)
            ecran.blit(texte_quete, (90, pos_y))
            pos_y += 30
        pos_y += 20
    
    # Quêtes en cours
    if toutes_quetes["en_cours"]:
        texte_cat = police_petit.render("En cours:", True, VERT)
        ecran.blit(texte_cat, (70, pos_y))
        pos_y += 30
        
        for quete in toutes_quetes["en_cours"]:
            texte_quete = police_petit.render(f"• {quete.nom} ({quete.get_progression_totale():.0f}%)", True, NOIR)
            ecran.blit(texte_quete, (90, pos_y))
            pos_y += 30
        pos_y += 20
    
    # Quêtes complétées
    if toutes_quetes["completee"]:
        texte_cat = police_petit.render("Complétées:", True, VERT)
        ecran.blit(texte_cat, (70, pos_y))
        pos_y += 30
        
        for quete in toutes_quetes["completee"]:
            texte_quete = police_petit.render(f"[X] {quete.nom}", True, GRIS)
            ecran.blit(texte_quete, (90, pos_y))
            pos_y += 30
    
    # Instructions
    texte_info = police_petit.render("Appuie P pour fermer", True, ROUGE)
    ecran.blit(texte_info, (150, 700))

def verifier_collision_ennemis(rect_joueur, liste_ennemis):
    """Vérifie si le joueur collide avec un ennemi"""
    for ennemi in liste_ennemis:
        rect_ennemi = pygame.Rect(ennemi.rect.x, ennemi.rect.y, 50, 50)
        if rect_joueur.colliderect(rect_ennemi):
            return ennemi
    return None

def afficher_resume_quetes():
    """Affiche le résumé des quêtes en haut"""
    stats = gestionnaire_quetes.get_stats_quetes()
    texte_resume = f"Quêtes: {stats['completees']}/{stats['total']}"
    
    rendu = police_hud.render(texte_resume, True, NOIR)
    pygame.draw.rect(ecran, GRIS, (940, 20, 300, 40))
    ecran.blit(rendu, (960, 30))

# ===== DICTIONNAIRE TOUCHES =====
touches = {
    pygame.K_z: False,      # Haut
    pygame.K_s: False,      # Bas
    pygame.K_q: False,      # Gauche
    pygame.K_d: False,      # Droite
    pygame.K_TAB: False,    # Inventaire
    pygame.K_p: False,      # Quêtes
    pygame.K_ESCAPE: False, # Menu
    pygame.K_e: False       # Interagir
}

# ===== VARIABLES D'ÉTAT =====
en_cours = True
etat = "menu"  # Démarre sur le menu principal
horloge = pygame.time.Clock()

dialogue_actif = False
pnj_actuel = None
index_replique = 0

inventaire_affiche = False
menu_quetes_affiche = False
tab_presse_precedemment = False  # Pour toggle TAB

while en_cours:
    dt = horloge.tick(60) / 10
    
    # ===== GESTION ÉVÉNEMENTS =====
    events = pygame.event.get()
    for evenement in events:
        if evenement.type == pygame.QUIT:
            en_cours = False
        elif evenement.type == pygame.KEYDOWN:
            if evenement.key in touches:
                touches[evenement.key] = True
            # Fenêtre pause
            if evenement.key == pygame.K_ESCAPE and etat == "plateau":
                pause_active = True
                while pause_active:
                    ecran.fill((40,40,40))
                    txt = police_titre.render("Pause", True, (255,255,255))
                    ecran.blit(txt, (LARGEUR_FENETRE//2 - txt.get_width()//2, 200))
                    boutons_pause = []
                    y = 320
                    for label in ["Reprendre", "Menu principal", "Paramètres", "Bestiaire", "Carte interactive", "Quitter le jeu"]:
                        rect = pygame.Rect(LARGEUR_FENETRE//2 - 200, y, 400, 60)
                        pygame.draw.rect(ecran, (100,100,100), rect)
                        txt_btn = police.render(label, True, (255,255,255))
                        ecran.blit(txt_btn, (rect.x + rect.width//2 - txt_btn.get_width()//2, rect.y + rect.height//2 - txt_btn.get_height()//2))
                        boutons_pause.append((label, rect))
                        y += 80
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pause_active = False
                            en_cours = False
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            pause_active = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            pos = pygame.mouse.get_pos()
                            for label, rect in boutons_pause:
                                if rect.collidepoint(pos):
                                    if label == "Reprendre":
                                        pause_active = False
                                    elif label == "Menu principal":
                                        pause_active = False
                                        etat = "menu"
                                    elif label == "Paramètres":
                                        pause_active = False
                                        etat = "parametres"
                                    elif label == "Bestiaire":
                                        afficher_bestiaire(ecran, police)
                                        pygame.display.flip()
                                        attendre = True
                                        while attendre:
                                            for ev in pygame.event.get():
                                                if ev.type == pygame.KEYDOWN or ev.type == pygame.MOUSEBUTTONDOWN:
                                                    attendre = False
                                    elif label == "Carte interactive":
                                        afficher_carte_interactive(ecran, police)
                                        pygame.display.flip()
                                        attendre = True
                                        while attendre:
                                            for ev in pygame.event.get():
                                                if ev.type == pygame.KEYDOWN or ev.type == pygame.MOUSEBUTTONDOWN:
                                                    attendre = False
                                    elif label == "Quitter le jeu":
                                        pause_active = False
                                        en_cours = False
                                        pygame.quit()
                                        sys.exit()
            # Dialogue - passer à la suite
            if evenement.key == pygame.K_e and dialogue_actif:
                index_replique += 1
                if index_replique >= len(dialogues_pnj[pnj_actuel]):
                    dialogue_actif = False
                    pnj_actuel = None
            # Ctrl+S pour sauvegarder (à implémenter)
            if evenement.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                sauvegarde_systeme.sauvegarder_avec_position(joueur, pos_joueur_x, pos_joueur_y)
                ajouter_notification_differee("💾 Partie sauvegardée!")
                audio.jouer_son("achat")
        elif evenement.type == pygame.KEYUP:
            if evenement.key in touches:
                touches[evenement.key] = False
        # Clics souris pour dialogues
        elif evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:
            if dialogue_actif:
                pos_souris = pygame.mouse.get_pos()
                reponses = dialogues_pnj[pnj_actuel][index_replique].get("reponses")
                if reponses:
                    pos_y = HAUTEUR_FENETRE - 200
                    for cle, reponse in reponses.items():
                        rect_reponse = pygame.Rect(650, pos_y, 550, 40)
                        if rect_reponse.collidepoint(pos_souris):
                            traiter_action(reponse["action"])
                            index_replique += 1
                            if index_replique >= len(dialogues_pnj[pnj_actuel]):
                                dialogue_actif = False
                            break
                        pos_y += 50
    
    # ===== BASCULER ÉTATS =====
    if touches[pygame.K_p]:
        menu_quetes_affiche = True
        inventaire_affiche = False
    
    # TAB - Toggle inventaire
    if touches[pygame.K_TAB] and not tab_presse_precedemment:
        inventaire_affiche = not inventaire_affiche  # Toggle
        menu_quetes_affiche = False
        tab_presse_precedemment = True
    
    if not touches[pygame.K_TAB]:
        tab_presse_precedemment = False
    
    if touches[pygame.K_ESCAPE]:
        menu_quetes_affiche = False
        inventaire_affiche = False
        afficher_notifications_differees()
    
    # Interagir avec PNJ (touche E)
    if touches[pygame.K_e]:
        if not dialogue_actif:
            for pnj_id, pos in positions_pnj.items():
                if joueur_proche_pnj(pos, (pos_joueur_x, pos_joueur_y)):
                    dialogue_actif = True
                    pnj_actuel = pnj_id
                    index_replique = 0
                    audio.jouer_son("dialogue")
                    break
    
    # ===== MENU PRINCIPAL =====
    if etat == "menu":
        boutons_menu = afficher_menu_principal(ecran, police_titre, sauvegarde_existe)
        pygame.display.flip()
        for evenement in events:
            if evenement.type == pygame.QUIT:
                en_cours = False
            elif evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:
                pos = pygame.mouse.get_pos()
                for nom, rect in boutons_menu:
                    if rect.collidepoint(pos):
                        if nom == "continuer":
                            etat = "plateau"
                        elif nom == "nouvelle":
                            try:
                                os.remove(os.path.join("sauvegardes", "partie_principale.json"))
                            except Exception:
                                pass
                            etat = "plateau"
                        elif nom == "reset":
                            try:
                                os.remove(os.path.join("sauvegardes", "partie_principale.json"))
                            except Exception:
                                pass
                        elif nom == "parametres":
                            etat = "parametres"
                        elif nom == "quitter":
                            en_cours = False
                            pygame.quit()
                            sys.exit()
        continue

    # ===== FENÊTRE PARAMÈTRES =====
    if etat == "parametres":
        boutons_param = afficher_fenetre_parametres(ecran, police, police_titre, touches, volume_musique, volume_effets, langue, menu_ouvert)
        pygame.display.flip()
        event_param = pygame.event.wait()
        if event_param.type == pygame.QUIT:
            en_cours = False
        elif event_param.type == pygame.MOUSEBUTTONDOWN and event_param.button == 1:
            pos = pygame.mouse.get_pos()
            for nom, rect in boutons_param:
                if rect.collidepoint(pos):
                    # Volume musique : clic gauche = -, clic droit = +
                    if nom == "volume_musique":
                        milieu = rect.x + rect.width // 2
                        if pos[0] < milieu:
                            volume_musique = max(0.0, volume_musique - 0.1)
                        else:
                            volume_musique = min(1.0, volume_musique + 0.1)
                        mettre_a_jour_notification(f"Volume musique : {int(volume_musique*100)}%")
                        break
                    # Volume effets : clic gauche = -, clic droit = +
                    elif nom == "volume_effets":
                        milieu = rect.x + rect.width // 2
                        if pos[0] < milieu:
                            volume_effets = max(0.0, volume_effets - 0.1)
                        else:
                            volume_effets = min(1.0, volume_effets + 0.1)
                        mettre_a_jour_notification(f"Volume effets : {int(volume_effets*100)}%")
                        break
                    elif nom == "langue":
                        langue = "EN" if langue == "FR" else "FR"
                        mettre_a_jour_notification(f"Langue : {langue}")
                        break
                    elif nom == "plein_ecran":
                        if ecran.get_flags() & pygame.FULLSCREEN:
                            ecran = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
                        else:
                            ecran = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE), pygame.FULLSCREEN)
                        mettre_a_jour_notification("Mode plein écran changé")
                        break
                    elif nom == "reset_options":
                        volume_musique = 0.5
                        volume_effets = 0.5
                        langue = "FR"
                        mettre_a_jour_notification("Options réinitialisées")
                        break
                    elif nom == "accessibilite":
                        mettre_a_jour_notification("Fonction à venir")
                        break
                    elif nom == "credits":
                        # Affichage page crédits
                        afficher_page_credits(ecran, police_titre, police)
                        pygame.display.flip()
                        attendre = True
                        while attendre:
                            for ev in pygame.event.get():
                                if ev.type == pygame.KEYDOWN or ev.type == pygame.MOUSEBUTTONDOWN:
                                    attendre = False
                        break
                    elif nom == "aide":
                        # Affichage page aide
                        afficher_page_aide(ecran, police_titre, police)
                        pygame.display.flip()
                        attendre = True
                        while attendre:
                            for ev in pygame.event.get():
                                if ev.type == pygame.KEYDOWN or ev.type == pygame.MOUSEBUTTONDOWN:
                                    attendre = False
                        break
                    elif nom == "retour":
                        etat = "menu"
                        break
        elif event_param.type == pygame.KEYDOWN:
            if event_param.key == pygame.K_ESCAPE:
                etat = "menu"
        continue


    # ===== MOUVEMENTS DU JOUEUR =====
    if etat == "plateau":
        pos_x_init = pos_joueur_x
        pos_y_init = pos_joueur_y
        
        if touches[pygame.K_z]:  # Haut
            pos_joueur_y -= vitesse_joueur
        elif touches[pygame.K_s]:  # Bas
            pos_joueur_y += vitesse_joueur
        elif touches[pygame.K_d]:  # Droite
            pos_joueur_x += vitesse_joueur
        elif touches[pygame.K_q]:  # Gauche
            pos_joueur_x -= vitesse_joueur
        
        # Limites de déplacement
        pos_joueur_x = max(LIMITE_GAUCHE, min(pos_joueur_x, LIMITE_DROITE))
        pos_joueur_y = max(LIMITE_HAUT, min(pos_joueur_y, LIMITE_BAS))
        rect_joueur.topleft = (pos_joueur_x, pos_joueur_y)
        
        # Collisions avec objets
        if rect_joueur.colliderect(rect_objet):
            # Collecte de ressource
            compteur_collectibles += 1
            gestionnaire_quetes.augmenter_progression_quete("Ressources_collectees")
            mettre_a_jour_notification(f"Potion collectée! ({compteur_collectibles}/5)")
            
            # Réapparaître l'objet ailleurs
            import random
            pos_objet_x = random.randint(100, 1100)
            pos_objet_y = random.randint(100, 700)
            rect_objet.topleft = (pos_objet_x, pos_objet_y)
            
            # Ajouter à l'inventaire

            # ...existing code...
        elif rect_joueur.colliderect(rect_marchand):
            pos_joueur_x = pos_x_init
            pos_joueur_y = pos_y_init
            rect_joueur.topleft = (pos_joueur_x, pos_joueur_y)
        
        # Collision avec ennemis
        ennemi_collision = verifier_collision_ennemis(rect_joueur, ennemis)
        if ennemi_collision:
            combat = CombatSysteme(joueur, ennemi_collision, ecran_combat, audio)
            resultat = combat.afficher_combat()
            
            if resultat == "victoire":
                # Tracker les ennemis vaincus
                ajouter_monstre_bestiaire(ennemi_collision.nom)
                if ennemi_collision.nom.lower() == "bandit":
                    compteur_bandits_vaincus += 1
                    gestionnaire_quetes.augmenter_progression_quete("Bandits_vaincus")
                elif ennemi_collision.nom.lower() == "loup":
                    compteur_loups_vaincus += 1
                    gestionnaire_quetes.augmenter_progression_quete("Loups_vaincus")
                
                ennemis.remove(ennemi_collision)
                etat = "plateau"
                for cle in touches:
                    touches[cle] = False
                audio.jouer_son("victoire")
                verifier_succes(joueur, gestionnaire_quetes, compteur_bandits_vaincus, compteur_loups_vaincus)
            elif resultat == "defaite":
                afficher_defaite(ecran, police_titre)
                pygame.display.flip()
                attendre = True
                while attendre:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            attendre = False
                            en_cours = False
                        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                            attendre = False
                            en_cours = False
                            etat_jeu = "menu"
            elif resultat == "fuite":
                etat = "plateau"
                pos_joueur_x += 50
                rect_joueur.topleft = (pos_joueur_x, pos_joueur_y)
                for cle in touches:
                    touches[cle] = False
        
        # ===== AFFICHAGE PRINCIPAL =====
        ecran.fill(COULEUR_FOND)
        ecran.blit(image_objet, (pos_objet_x, pos_objet_y))
        ecran.blit(image_pnj_1, (pos_pnj_1_x, pos_pnj_1_y))
        ecran.blit(image_marchand, (pos_marchand_x, pos_marchand_y))
        ecran.blit(image_joueur, (pos_joueur_x, pos_joueur_y))
        
        afficher_hud()
        afficher_notification()
        afficher_resume_quetes()
        
        # Afficher les ennemis
        for ennemi in ennemis:
            ennemi.deplacer_aleatoirement(dt)
            pygame.draw.rect(ecran, ROUGE, (ennemi.rect.x, ennemi.rect.y, 50, 50))
        
        # Afficher dialogue
        if dialogue_actif:
            texte_actuel = dialogues_pnj[pnj_actuel][index_replique]["texte"]
            reponses_actuelles = dialogues_pnj[pnj_actuel][index_replique].get("reponses")
            afficher_dialogue(ecran, texte_actuel, reponses_actuelles)
    
    # Afficher inventaire
    if inventaire_affiche:
        afficher_inventaire()
    
    pygame.display.flip()
    horloge.tick(60)

pygame.quit()
sys.exit()
