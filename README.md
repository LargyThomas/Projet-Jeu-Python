# Python RPG Game 🎮

A 2D top-down RPG built with Python and Pygame, featuring a combat system, quest tracking, inventory management, and persistent save/load functionality.

---

## 🛠️ Built With

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.6.1-green?style=flat-square)

---

## 🎯 Features

- **Turn-based combat** — Attack, Defend (50% damage reduction), use Potions, or Flee
- **Enemy AI** — Enemies can parry (30%) and dodge (30%) your attacks
- **Quest system** — 3 quests with real-time progress tracking
- **Inventory** — Collect and manage items (potions, swords, shields)
- **Save & Load** — Persistent JSON save file, auto-loaded on startup
- **NPC & Merchant** — Talk to NPCs and buy items
- **Resource collection** — Pick up items scattered across the map

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install pygame==2.6.1
```

### Run the game

```bash
python principal.py
```

> Audio files are optional — the game runs fine without them.

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| Z / Q / S / D | Move |
| TAB | Open / Close inventory |
| P | Show quests |
| E | Interact with NPC |
| CTRL+S | Save game |

---

## 📜 Quests

| Quest | Objective | Reward |
|-------|-----------|--------|
| Save the Village | Defeat 3 bandits | 200 gold |
| Hunt the Wolf | Defeat 1 wolf | 100 gold |
| Resource Collection | Collect 5 potions | 150 gold |

---

## 💾 Save System

The game automatically loads your last save on startup. Press **CTRL+S** anytime to save your current position and stats.

Save file location: `sauvegardes/partie_principale.json`

---

## 📂 Project Structure

```
├── principal.py           ← Main game loop
├── systeme_sauvegarde.py  ← Save / Load system
├── quete_systeme.py       ← Quest management
├── combat_systeme.py      ← Combat UI
├── interface_audio.py     ← Audio system
├── Asset/
│   └── audio/             ← Sound files (.wav) — optional
└── sauvegardes/
    └── partie_principale.json
```

---

## 🔮 Planned Features

- [ ] Quest rewards auto-distribution
- [ ] Level-up stat bonuses
- [ ] Boss fights
- [ ] Mini-map
- [ ] More enemy types and zones# Python RPG Game 🎮
