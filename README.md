# The Perfect Guess 

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Beginner Friendly](https://img.shields.io/badge/Level-Beginner-green)](https://github.com/)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red)](https://opensource.org/)

A simple number guessing game built in Python. The program picks a random number between 1 and 100, and you try to guess it with hints along the way.

---

## Project Overview

This is one of my early Python projects. I built it to get more comfortable with loops, conditionals, functions, and input handling. The game is straightforward — guess a number, get a hint, repeat until you nail it. I also added input validation and a replay option to make it feel more complete.

---

## Features

- Random number generated between 1 and 100 each round
- Hints after every wrong guess (too high / too low)
- Handles invalid inputs without crashing
- Tracks and displays your total attempts
- Option to play again without restarting the script
- Clean terminal output that's easy to read

---

## How It Works

1. Program picks a random number between 1 and 100
2. You enter a guess
3. It tells you if your guess is too high or too low
4. Keep guessing until you get it right
5. Your total attempts are shown at the end
6. Choose to play again or exit

---

## Technologies Used

- **Python 3.x**
- `random` module (standard library — no external packages needed)

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/the-perfect-guess.git

# Navigate into the folder
cd the-perfect-guess
```

No additional packages required.

---

## Usage

```bash
python main.py
```

Make sure you have Python 3 installed. You can check with:

```bash
python --version
```

---

## Example Output

```
  Welcome to The Perfect Guess!
  I'm thinking of a number between 1 and 100.
  Let's see how many attempts it takes you.

Guess the number (1-100): 50
  Too high! Try a lower number.
Guess the number (1-100): 25
  Too low! Try a higher number.
Guess the number (1-100): 35
  Too high! Try a lower number.
Guess the number (1-100): 30

  Correct! The number was 30.
  You got it in 4 attempts. Well played!

  Play again? (y/n): n

  Thanks for playing. See you next time!
```

---

## Learning Outcomes

Working on this project helped me understand:

- How to use `while` loops effectively
- Writing reusable functions with `def`
- Handling exceptions using `try/except`
- Using f-strings for clean output
- Structuring a small script with a `main()` entry point
- The `if __name__ == "__main__"` pattern

---

## Future Improvements

A few things I want to add later:

- Difficulty levels (Easy / Medium / Hard with different ranges)
- A scoring system based on attempts
- Leaderboard stored in a file
- Option to set a custom range
- A GUI version using Tkinter

---

## Project Structure

```
the-perfect-guess/
│
├── main.py              # Main game logic
├── README.md            # Project documentation
├── LICENSE              # MIT License
├── .gitignore           # Files to ignore
├── requirements.txt     # Dependencies (none for now)
├── CONTRIBUTING.md      # How to contribute
├── CHANGELOG.md         # Version history
└── PROJECT_DESCRIPTION.md  # Extended project write-up
```

---

## Author

Kashish Arya
B.Tech (AI & ML)

- GitHub: kashish7714(https://github.com/your-username)
- LinkedIn: www.linkedin.com/in/kashish-arya-062249383
- Email : kashish7714ar@gmail.com


