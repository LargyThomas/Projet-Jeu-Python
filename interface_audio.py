"""
Interface Audio - Musique et effets sonores
"""
import pygame
import os

pygame.mixer.init()

class InterfaceAudio:
    def __init__(self):
        self.volume_musique = 0.5
        self.volume_son = 0.7
        
        # Dossier des sons
        self.dossier_audio = "Asset/audio"
        
        # Sons disponibles
        self.sons_cache = {}
        
        # Charger les sons disponibles
        self.charger_sons()
    
    def charger_sons(self):
        """Charge tous les sons disponibles"""
        sons_a_charger = [
            "coup",
            "coup_ennemi",
            "victoire",
            "defaite",
            "fuite",
            "dialogue",
            "achat",
            "erreur",
            "defense",
            "potion"
        ]
        
        for nom_son in sons_a_charger:
            chemin = f"{self.dossier_audio}/{nom_son}.wav"
            if os.path.exists(chemin):
                try:
                    son = pygame.mixer.Sound(chemin)
                    son.set_volume(self.volume_son)
                    self.sons_cache[nom_son] = son
                except Exception as e:
                    print(f"Erreur chargement son {nom_son}: {e}")
            else:
                print(f"Son non trouvé: {chemin}")
    
    def jouer_son(self, nom_son):
        """Joue un son si disponible"""
        if nom_son in self.sons_cache:
            try:
                self.sons_cache[nom_son].play()
            except Exception as e:
                print(f"Erreur lecture son {nom_son}: {e}")
        else:
            print(f"Son '{nom_son}' non chargé")
    
    def arreter_tous_sons(self):
        """Arrête tous les sons"""
        pygame.mixer.stop()
    
    def definir_volume_musique(self, volume):
        """Définit le volume de la musique (0 à 1)"""
        self.volume_musique = max(0, min(1, volume))
    
    def definir_volume_son(self, volume):
        """Définit le volume des effets sonores (0 à 1)"""
        self.volume_son = max(0, min(1, volume))
        
        # Appliquer au cache
        for son in self.sons_cache.values():
            son.set_volume(self.volume_son)
    
    def jouer_musique(self, chemin_musique):
        """Joue une musique de fond"""
        try:
            pygame.mixer.music.load(chemin_musique)
            pygame.mixer.music.set_volume(self.volume_musique)
            pygame.mixer.music.play(-1)  # Boucle infinie
        except Exception as e:
            print(f"Erreur chargement musique: {e}")
    
    def arreter_musique(self):
        """Arrête la musique"""
        pygame.mixer.music.stop()
