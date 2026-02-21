import time
import threading
import random

from entite import Entite

from nourriture import Nourriture
from niveau import Niveau
from shop import Shop
from ennemi import Ennemi


class Perso(Entite):
    def __init__(self, prenom):
        super().__init__(prenom, niveau=1)  # On initialise la super-classe (Entite)
        self.tenu = {'tete': 'casquette', 'haut': 'pull', 'bas': 'pantalon', 'pied': 'basket'}
        self.inventaire = {}
        self.argent = 1000
        self.main = {'gauche': 'rien', 'droite': 'hache'}
        self.vie = 10
        self.faim = 10
        self.experience = 0

        self.stop_event = threading.Event()  #Création de l'événement pour arrêter les threads

    def donner_nom(self):
        return self.nom

    def changer_argent(self, valeur):
        self.argent = valeur

    def gagner_experience(self, xp_gagnee):
        """Ajoute de l'XP et vérifie si level up"""
        self.experience += xp_gagnee
        seuil_levelup = self.niveau * 100
        
        if self.experience >= seuil_levelup:
            self.level_up()
    
    def level_up(self):
        """Augmente le niveau et augmente les stats"""
        self.niveau += 1
        self.experience = 0
        # Augmenter les stats
        self.vie += 2  # +2 PV par level
        print(f"{self.nom} a atteint le niveau {self.niveau}!")
        print(f"PV max augmenté à {self.vie}")
    
    def gagner_argent(self, montant):
        """Ajoute de l'argent"""
        self.argent += montant
        print(f"{self.nom} a gagné {montant} pièces d'or!")

    def gerer_faim(self):
     while not self.stop_event.is_set():  # Vérifie si l'événement est activé
         if self.faim <= 0:
             print(f"{self.nom} est mort de faim.")
             self.stop_event.set()  # Active l'événement pour arrêter le thread
             break
         self.faim -= 1  # Réduit la faim chaque seconde
         if self.points_de_vie <= 0:  # Si la vie est 0, la faim doit aussi arrêter
             print(f"{self.nom} est mort.")
             self.stop_event.set()  # Active l'événement pour arrêter le thread
             break
         time.sleep(600)  # Pause 10 minutes

    # Les threads = tâche en parallèle du prog.principale

    def gerer_faim_thread(self):
        """ Démarre un thread pour gérer la faim """
        thread_faim = threading.Thread(target=self.gerer_faim)
        thread_faim.start()
        return thread_faim

    def mourir(self):
        """ Méthode appelée quand le personnage meurt """
        self.stop_event.set()  # Active l'événement pour arrêter les threads
        print(f"{self.nom} est mort définitivement.")

    def manger(self, aliment):
        for item in self.inventaire:
            if isinstance(item, Nourriture) and item.nom == aliment:  # Vérification si c'est de la nourriture
                if item.nombre_unite() > 0:
                    points_restores = item.manger()  # Restaure des PV
                    self.restaurer_PV(points_restores)

                    if item.nombre_unite() == 0:
                        print(f"{aliment} est épuisé !")
                else:
                    print(f"{aliment} n'est plus disponible dans l' inventaire.")
                return
        print(f"{aliment} n'est pas trouvé dans l' inventaire.")

    def ajouter_objet(self, item, quantite=1):
        if item in self.inventaire:
            self.inventaire[item]["quantité"] += quantite  # Ajoute la quantité si l'item existe déjà
        else:
            self.inventaire[item] = {"quantité": quantite}  # Crée l'item avec sa quantité initiale
            print(f"{quantite} {item}(s) ajouté(s) à l'inventaire de {self.nom}.")

    def equiper_objet(self, item, main):
        if item in self.inventaire:
            if main == 'gauche':
                if self.main['gauche'] == 'rien':
                    self.main['gauche'] = item
                    self.inventaire[item]["quantité"] -= 1  # Décrémente la quantité de l'objet
                    if self.inventaire[item]["quantité"] == 0:  # Si la quantité atteint 0, on supprime l'objet
                        del self.inventaire[item]
                    print(f"{self.nom} a équipé {item} dans sa main {main}.")
                else:
                    print(f"{self.nom} ne peut pas équiper {item} dans sa main {main} car elle est déjà occupée.")

            elif main == 'droite':
                if self.main['droite'] == 'rien':
                    self.main['droite'] = item
                    self.inventaire[item]["quantité"] -= 1  # Décrémente la quantité de l'objet
                    if self.inventaire[item]["quantité"] == 0:  # Si la quantité atteint 0, on supprime l'objet
                        del self.inventaire[item]
                    print(f"{self.nom} a équipé {item} dans sa main {main}.")
                else:
                    print(f"{self.nom} ne peut pas équiper {item} dans sa main {main} car elle est déjà occupée.")
                    choix = input(f"Voulez-vous remplacer {self.main['droite']} par {item} ? (Oui/Non): ").strip().lower()
                    if choix == 'oui' or 'Oui':
                        ancien_item = self.main['droite']
                        self.main['droite'] = item
                        # Remet l'arme précédente dans l'inventaire
                        if ancien_item in self.inventaire:
                            self.inventaire[ancien_item]["quantité"] += 1
                        else:
                            self.inventaire[ancien_item] = {"quantité": 1}
                        self.inventaire[item]["quantité"] -= 1  # Décrémente la quantité de l'objet
                        if self.inventaire[item]["quantité"] == 0:  # Si la quantité atteint 0, on supprime l'objet
                            del self.inventaire[item]
                        print(f"{self.nom} a remplacé {ancien_item} par {item} dans sa main droite.")
                    else:
                        print(f"{self.nom} a décidé de ne pas remplacer {self.main['droite']}.")
        else:
            print(f"{self.nom} ne peut pas équiper {item} puisqu'il ne l'a pas dans son inventaire.")

    def utiliser_objet(self, item):
        if item in self.inventaire and self.inventaire[item]["quantité"] > 0:
            self.inventaire[item]["quantité"] -= 1
            # Ajouter des conditions selon le type d'item
        else:
            print(f"Pas de {item} dans l'inventaire.")

    def afficher_inventaire(self):
        for item, infos in self.inventaire.items():
            print(f"{item}: {infos['quantité']}")

    def equiper_tenu(self, item, tenu):
        if item in self.inventaire:
            if self.tenu[tenu] == 'rien':  # Vérifie si le slot de tenue est libre
                self.tenu[tenu] = item
                self.inventaire.remove(item)
                print(f"{self.nom} a équipé {item} sur lui.")
            else:
                ancien_item = self.tenu[tenu]
                self.inventaire.append(ancien_item)
                self.tenu[tenu] = item
                self.inventaire.remove(item)
                print(f"{self.nom} a équipé {item} sur lui.")
        else:
            print(f"{self.nom} ne peut pas équiper {item} puisqu'il ne l'a pas dans son inventaire.")

    def attaquer(self, arme, ennemi):
        # Associer l'arme à la main droite
        self.main['droite'] = arme

        # Définir les dégâts en fonction de l'arme
        if arme == 'hache':
            degats = 7
        elif arme == 'epee_fer':
            degats = 5
        elif arme == 'epee_or':
            degats = 10
        else:
            degats = 1  # Attaque à mains nues

        # Vérifier si l'ennemi est bien une instance de Ennemi (ou PNJ)
        if isinstance(ennemi, Ennemi):
            ennemi.point_de_vie -= degats
            print(f"{self.nom} attaque avec {arme} et inflige {degats} dégâts à {ennemi.nom} !")
            if ennemi.point_de_vie <= 0:
                print(f"{ennemi.nom} est mort.")
        else:
            print("L'ennemi n'est pas valide ou n'est pas de type Ennemi.")

    def fuir(self, ennemi):
        perte_or = random.randint(5, 15)  # Pénalité aléatoire en or
        self.inventaire["or"] = max(0, self.inventaire.get("or", 0) - perte_or)  # Empêche un solde négatif
        print(f"{self.nom} a fui le combat contre {ennemi.nom} !")
        print(f"Il perd {perte_or} pièces d'or en panique.")

    def acheter(self, item, Shop):
        if item in Shop.stock and Shop.stock[item][0] > 0:  # Vérifie si l'item est en stock
            prix = Shop.stock[item][1]
            if self.argent >= prix:  # Vérifie si le joueur a assez d'argent
                self.argent -= prix
                Shop.caisse += prix
                self.inventaire.append(item)
                Shop.stock[item][0] -= 1  # Enlève l'objet du stock
                print(f"{self.nom} a acheté {item} pour {prix} pièces.")
            else:
                print(f"{self.nom} n'a pas assez d'argent pour acheter {item}.")
        else:
            print(f"{item} n'est pas disponible dans le stock du magasin.")

    def gagner_experience(self, points):
        self.experience = points
        if self.experience >= self.niveau * 100:
            self.niveau_up()

    def niveau_up(self):
        self.niveau += 1
        self.experience = 0
        self.vie += 15