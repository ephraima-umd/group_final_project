# CelebrityWordJab

## Project Overview

CelebrityWordJab is a text-based celebrity naming game written in Python.

Players take turns entering celebrity names. The first letter of the next celebrity’s first name must match the first letter of the previous celebrity’s last name.

Example:

Tom Hanks → next celebrity must start with H

The game supports both:
- Player vs Bot mode
- Player vs Player mode

The game uses a database of celebrity names stored in a text file and includes validation systems to prevent duplicate or invalid answers.

---

# Files Included

## main.py
Runs the game and contains the main menu, game loops, and user interaction.

## problem3.py
Contains utility functions for:
- filtering valid names
- parsing celebrity names
- ranking players
- generating summaries

## problem4.py
Contains the bot-selection algorithm used for choosing valid celebrity names.

## celebrities.txt
Contains the celebrity database used during gameplay.

---

# How to Run the Program

Have all the files open in VSCode then type this in the terminal:
python3 main.py
