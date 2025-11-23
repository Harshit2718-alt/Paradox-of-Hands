# 🎮 Rock–Paper–Scissors (Tkinter GUI Version)

This is a simple and fun **Rock–Paper–Scissors game** built using Python's **Tkinter** library.
The player competes against the computer, and the first to reach **5 wins** is declared the champion!

---

## ✨ Features

* ✔️ User-friendly graphical interface (GUI)
* ✔️ ASCII art for Rock, Paper, and Scissors
* ✔️ Real-time score updates
* ✔️ CPU “thinking” animation with delays
* ✔️ Automatic round tracking
* ✔️ Final winner popup when game ends
* ✔️ Threading for smooth UI updates (no freezing!)

---

## 🛠️ How the Game Works

### 1️⃣ Player chooses Rock, Paper, or Scissors

Click one of the three buttons:

* **Rock**
* **Paper**
* **Scissors**

### 2️⃣ CPU makes its choice

The game shows a small “thinking” animation to feel more realistic.

### 3️⃣ Result & score update

The program checks:

* If you win
* If the CPU wins
* If it's a draw

The score displayed is updated accordingly.

### 4️⃣ Game History

ASCII pictures of both player and CPU choices appear in the text box.

### 5️⃣ Winning Condition

The first to reach **5 points** wins the match.

A popup window appears showing:

* Final result (You Won / CPU Won)
* Final Score
* OK button to exit the game

---

## 📁 Project Structure

All logic is handled in a single Python file:

* **GameRPS class**

  * Handles score, rules, ASCII art, and choices.
* **Tkinter UI**

  * Labels, buttons, text area, and result window.
* **Threading**

  * Used to avoid UI freezing during CPU animations.

---

## ▶️ How to Run

1. Make sure Python is installed.
2. Save the code in a file, for example:

```
rps_game.py
```

3. Install required modules (all are built-in):

```
tkinter, random, time, threading
```

4. Run the game:

```
python rps_game.py
```

Enjoy playing! 🎉

---

## 💡 Customization Ideas

You can improve the game by:

* Adding background colors or fonts
* Adding sound effects
* Adding a match restart button
* Displaying match history in a separate window

---
