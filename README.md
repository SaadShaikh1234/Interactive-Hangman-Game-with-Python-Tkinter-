# 🎮 Hangman Word Guessing Game with Tkinter

A fully interactive **Hangman game** built in **Python** using **Tkinter** for the graphical interface. Play solo with hints across multiple categories or challenge a friend in multiplayer mode. The game includes a **visual hangman progression**, **real-time feedback**, and a persistent **leaderboard** to track top scores.

---

## 🧩 Game Modes

- 🔹 **Single Player Mode**  
  Select a category and guess the word with the help of a hint.

- 🔸 **Multiplayer Mode**  
  One player sets the word and hint, the other tries to guess it.

---

## 💡 Features

- 🎨 GUI designed with Tkinter (custom colors, structured navigation)
- 🎯 Real-time gameplay feedback with ASCII-style hangman art
- 📚 Category-based words (Tech, Sports, Movies, Animals)
- 🏆 Leaderboard saved to `leaderboard.txt` with auto-updates
- ⚠️ Error handling for invalid or duplicate guesses
- 🎲 Randomized word selection for replayability

---

## 📁 Files Included

| File Name                          | Description                                 |
|-----------------------------------|---------------------------------------------|
| `Hangman-Word guessing game.py`   | Main Python script with complete game logic |
| `leaderboard.txt`                 | Stores player scores (auto-created)         |

---

## 🖼️ Screenshot Preview

```plaintext
   ------
   |    |
   |    O
   |   /|\
   |   / \
   |
-------
GAME OVER!
```
---

## 🧠 Example Categories & Hints
Category	Word	Hint
• **Tech**: `python` – Popular programming language  
• **Sports**: `cricket` – A game played with bat and ball  
• **Movies**: `joker` – A DC villain got his own movie  
• **Animals**: `penguin` – A bird that cannot fly  

---

## 🚀 How to Run
1. Ensure you have Python 3 installed.
2. Launch the game from terminal or IDE:

```bash

python "Hangman-Word guessing game.py"
```
3. Select a mode and start playing!

---

## 🧠 Learning Objectives
Master Tkinter layout and widget control

Practice file handling (read/write leaderboard)

Improve logic and error-checking using conditionals

Learn clean modular design using OOP principles in Python

---

## 🔧 Tech Stack
Language: Python 3

Libraries: Tkinter, os, random, messagebox

---

## 📈 Leaderboard Sample Format
```makefile

Alice: 30
Bob: 10
Scores are automatically saved and updated after each game session.
```
---
