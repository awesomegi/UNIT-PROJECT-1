# 🎬 CINEQUIZ: The Ultimate Movie Trivia CLI

## Overview
A Python-based Command Line Interface (CLI) game that tests your movie knowledge using real-time data from the Open Trivia Database API.

## Features
- **Dynamic Questions:** Fetches 10 fresh movie questions every round.
- **Difficulty Selection:** Choose between Easy, Medium, and Hard.
- **Persistent Leaderboard:** Scores are saved to a JSON file and can be viewed from the main menu.
- **Smart Formatting:** Handles HTML characters (like quotes) for clean reading.

## How to Use
1. Run `python main.py`.
2. Select **[1]** to Play.
3. Enter your name and choose a difficulty.
4. Use **A, B, C, or D** to answer.
5. Select **[2]** from the main menu to see the Top 5 High Scores.

## Technical Skills Used
- **OOP:** Player class manages state and ranking logic.
- **API Integration:** Uses `requests` to fetch external data.
- **File I/O:** Saves and reads data using `json` and file `append` mode.
- **Decorators:** Custom `@game_banner` for UI consistency.
- **Error Handling:** Try/Except blocks for API calls and file reading.
