# 🎮 GUIDE RAPIDE - DÉMARRAGE DU JEU

## Lancer le jeu

```bash
cd "d:\Projet Jeu Python"
python principal.py
```

---

## 🎮 Commandes en jeu

| Clavier | Action |
|---------|--------|
| **Z/Q/S/D** | Déplacer le joueur |
| **TAB** | Ouvrir/fermer l'inventaire |
| **P** | Afficher les quêtes |
| **E** | Parler aux PNJ / Répondre dialogues |
| **CTRL+S** | Sauvegarder la partie (position + stats) |
| **ALT+F4** ou **X** | Quitter le jeu |

---

## 📊 Système de Progression

### Niveaux
- Gagnez de l'XP en tuant des ennemis
- À 100 XP → **LEVEL UP** (atk +1, santé +2)
- Continuez à progresser indéfiniment

### Argent
- Loot des ennemis: **30-50 or**
- Achetable chez le marchand (en bas à droite)
- Dépensable pour:
  - Potions: **50 or** chaque
  - Épées: **100 or** chaque

### Inventaire (TAB)
- Max 99 de chaque objet
- Affiche: nom + quantité
- Items principaux:
  - Potions (restaur 5 PV)
  - Épées (augment atk)
  - Boucliers (augment défense)

---

## ⚔️ Combat

### Comment combattre
1. Marchez sur un ennemi → Combat automatique
2. 4 boutons disponibles:

| Bouton | Effet | Coût |
|--------|--------|------|
| **Attaquer** | Dégât normal | Aucun |
| **Défendre** | Réduit dégat 50% | Aucun |
| **Potion** | Restaur 5 PV | -1 potion |
| **Fuir** | Quitter le combat | Échec 30% |

### Ennemis

**Bandit** (Zone centrale)
- Niveau: 1
- Atk: 3
- Loot: 50 or + épée_fer
- Quête: "Sauver le village" (3x)

**Loup** (Zone inférieure droite)
- Niveau: 1
- Atk: 2
- Loot: 30 or + potion
- Quête: "Chasser le loup" (1x)

### Ennemis spéciaux? 
Oui! Les ennemis peuvent:
- **Parer** (30% chance) → Réduit dégat
- **Esquiver** (30% chance) → Évite l'attaque

---

## 📜 Quêtes (Appui P)

### Quest 1: Sauver le village ⚔️
- Éliminer **3 bandits**
- Récompense: **200 or** (non implémentée auto)
- Progression: `0/3` → `100%`

### Quest 2: Chasser le loup ⚔️
- Éliminer **1 loup**
- Récompense: **100 or** (non implémentée auto)
- Progression: `0/1` → `100%`

### Quest 3: Collecte de ressources 🎒
- Collecter **5 potions**
- Récompense: **150 or** (non implémentée auto)
- Progression: `0/5` → `100%`
- **Comment**: Touchez les objets qui apparaissent sur la map

---

## 💾 Sauvegarde

### Auto-sauvegarde au démarrage
Au lancement, le jeu charge automatiquement:
- Position du joueur (X, Y)
- Niveau, XP, PV, Argent
- Inventaire complet
- État de la défense

### Fonction CTRL+S
Appuyez **CTRL+S** en jeu pour sauvegarder l'état actuel.

Les données sont stockées dans: `sauvegardes/partie_principale.json`

### Format (JSON)
```json
{
  "nom_joueur": "Arthur",
  "niveau": 5,
  "position_x": 450,
  "position_y": 350,
  "argent": 1500,
  "inventaire": {"potion": {"quantité": 15}},
  "date_sauvegarde": "2024-01-15 14:30:45"
}
```

---

## 🌍 Zones de la Map

| Zone | Contenu | Ennemis |
|------|---------|---------|
| **Haut gauche** | Point de spawn | Aucun |
| **Centre** | Zone principale | Bandits (3) |
| **Bas droite** | Région sauvage | Loup (1) |
| **Bas gauche** | Marchand | Aucun |
| **Haut droit** | PNJ 1 | Aucun |

---

## 🏪 Marchand

### Localisation
En bas à droite de la map

### Inventaire
- Potion de Vie: **50 or**
- Épée Premium: **100 or**

### Comment acheter
1. Allez près du marchand
2. Appuyez **E** → Dialogue automatique
3. Sélectionnez l'item avec les chiffres

---

## 🐛 Troubleshooting

### "Aucune sauvegarde trouvée"
Normal! Première partie = nouveau joueur.

### "Son non trouvé: Asset/audio/..."
Normal! Les sons sont optionnels.
- Voir [GUIDE_AUDIO.md](GUIDE_AUDIO.md) pour installer les sons

### Inventaire bugué?
- Appuyez **TAB** UNE fois = ouvre
- Appuyez **TAB** UNE fois = ferme
- (Pas de multi-toggle)

### Dialogue pas visible?
- Assez proche du PNJ (~150px)
- Appuyez **E** pour interagir

### Jeu crash?
- Vérifiez Python 3.10+
- Vérifiez Pygame: `pip install pygame==2.6.1`

---

## 📝 Notes importantes

- **Quêtes** se complètent auto (voir progression en temps réel)
- **Recompenses** ne sont pas distribuées auto (à implémenter)
- **Stats** sont sauvegardées en temps réel avec CTRL+S
- **Limite map** = joueur ne peut pas aller derrière le HUD
- **Rayon d'interaction** = 150px (large pour faciliter dialogue)

---

## 🎯 Objectifs recommandés

**Session 1**: Exploration
- [ ] Trouver tous les PNJ
- [ ] Comprendre le combat
- [ ] Gagner quelques niveaux

**Session 2**: Quêtes
- [ ] Terminer "Sauver le village"
- [ ] Terminer "Chasser le loup"
- [ ] Commencer "Collecte"

**Session 3**: Optimisation
- [ ] Farming or pour items premium
- [ ] Maximiser inventaire
- [ ] Tester défense combats

---

## 📚 Fichiers de référence

| Fichier | Contenu |
|---------|---------|
| [GUIDE_AUDIO.md](GUIDE_AUDIO.md) | Comment ajouter des sons |
| [RESUME_AMELIORATIONS_RECENTES.md](RESUME_AMELIORATIONS_RECENTES.md) | Changelog complet |
| [principal.py](principal.py) | Code principal du jeu |
| [systeme_sauvegarde.py](systeme_sauvegarde.py) | Système de save/load |
| [quete_systeme.py](quete_systeme.py) | Gestion des quêtes |
| [combat_systeme.py](combat_systeme.py) | Interface combat |

---

**Bon jeu! 🎮✨**
