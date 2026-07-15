# 🗼 Tower of Eternal Eclipse

*A terminal-based roguelite RPG built in Python.*

Enter the mysterious **Tower of Eternal Eclipse**, where every defeat becomes a lesson and every new life brings another chance to climb higher. Battle dangerous enemies, conquer legendary bosses, level up your hero, and uncover the secrets hidden within the ever-changing tower.

> **"The Tower remembers your previous lives... They weren't worthy enough."**

---

# ✨ Features

### ⚔️ Three Unique Playable Classes

Choose your playstyle:

* 🛡️ **Knight** – High durability with self-healing abilities.
* 🔥 **Mage** – High-risk, high-reward spellcaster capable of sacrificing vitality for overwhelming power.
* 🏹 **Archer** – Agile ranged fighter specializing in critical hits and devastating burst damage.

---

### 👾 Procedurally Generated Battles

* Random environments
* Random enemy encounters
* Scaling enemy difficulty
* Endless replayability

---

### 👑 Boss Encounters

Face increasingly powerful bosses throughout your climb.

* Boss battle every 5 floors
* Unique regional bosses
* Shadow Form encounter
* Final battle against **The Forgotten One**

---

### 📈 RPG Progression

* EXP-based leveling
* Class-specific stat growth
* Increasing EXP requirements
* Difficulty scaling

---

### 💾 Persistent Save System

Your progress is stored using JSON saves.

Saved information includes:

* Player Class
* Current Level
* EXP
* Current Floor
* Reset Count

Continue your climb whenever you return.

---

### ☠️ Roguelite Progression

Death isn't failure.

Every defeat increases your **Reset Count**, allowing another attempt with accumulated experience and knowledge while the Tower grows even more determined to stop you.

---

### 🤖 Automated Balance Testing

The project includes a dedicated **Autobot Simulator** used during development.

It can automatically play **thousands of complete game runs** without player input, allowing balancing decisions to be based on real gameplay data rather than guesswork.

The simulator records statistics such as:

* 📊 Average resets
* 🏆 Highest floor reached
* ⭐ Highest player level
* ⚔️ Attack usage percentages
* 💥 Critical hit rate
* 🎯 Miss rate
* 📈 EXP progression

---

# 🛠 Built With

* Python 3
* JSON
* Object-Oriented Programming (OOP)

---

# 📁 Project Structure

```text
Tower_of_Eternal_Eclipse/
│
├── main.py
├── battle.py
├── player.py
├── enemy.py
├── level_up.py
├── world.py
├── gamestate.py
├── save_system.py
├── autobot.py
├── statistics.py
├── reports.py
├── data/
├── save.json
└── README.md
```

---

# 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/NeilNNP45-dev/tower-of-eternal-eclipse-roguelite-game.git
```

Navigate into the project:

```bash
cd Tower-of-Eternal-Eclipse
```

Run the game:

```bash
python main.py
```

---

# 🎮 Current Version

## Alpha v0.1

Implemented features include:

* ✅ Turn-based combat
* ✅ Three playable classes
* ✅ Multiple boss encounters
* ✅ Procedural enemy generation
* ✅ Save & Load system
* ✅ EXP & Level progression
* ✅ Roguelite reset mechanics
* ✅ Automated balance testing suite
* ✅ Detailed simulation reports

---

# 🔮 Planned Features

* 🎒 Inventory System
* 🛡️ Equipment & Weapons
* ✨ Additional Skills & Class Abilities
* 🧪 Status Effects
* 🌎 More Environments
* 👹 More Bosses
* 📜 Story & Lore Expansion
* 🏆 Achievements
* 🎵 Music & Sound Effects
* 🎨 Pygame GUI Version

---

# 📸 Screenshots

*Coming Soon*

---

# 👨‍💻 Developer

Created by **Neil**

Tower of Eternal Eclipse is a personal passion project created while learning Python, Object-Oriented Programming, game development, software architecture, balancing, and software testing.

Every major gameplay mechanic—from combat to progression and class balance—has been built from scratch as part of the learning journey.

---

# 📜 License

This project is open for learning and educational purposes.
