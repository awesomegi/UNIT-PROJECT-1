
# 🎬 CINEQUIZ: The Ultimate Trivia CLI

## Overview
A Python-based Command Line Interface (CLI) game that tests your knowledge across multiple categories using real-time data from the Open Trivia Database API.

## Features
- **Multi-Category Questions:** Choose from Movies, Music, Science, History, Sports, Video Games, and General.
- **Difficulty Selection:** Choose between Easy, Medium, and Hard.
- **Question Timer:** 15 seconds per question — run out of time and it counts as wrong.
- **Streak & Combo System:** Consecutive correct answers multiply your score (up to 2.5x).
- **Hint System:** Use up to 2 hints per game to eliminate a wrong answer.
- **Persistent Leaderboard:** Scores saved to JSON with date, accuracy, and best streak.
- **Category-Aware Ranks:** Your final rank title matches the category you played.
- **Rich CLI:** Colored output, panels, and live score updates powered by `rich`.

## How to Use
1. Run `python main.py`.
2. Select **[1]** to Play.
3. Enter your name, choose a difficulty, then choose a category.
4. Use **A, B, C, or D** to answer — or **H** to use a hint.
5. Select **[2]** from the main menu to see the Top 5 High Scores.

## Technical Skills Used
- **OOP:** `Player` class manages score, streak, accuracy, and ranking logic.
- **API Integration:** Uses `requests` to fetch questions by category and difficulty.
- **Threading:** `threading.Event` powers the per-question countdown timer.
- **File I/O:** Saves and reads scores using `json` in append mode.
- **Decorators:** Custom `@game_banner` for consistent UI framing.
- **Error Handling:** Try/Except blocks for API calls and file reading.
- **Rich Library:** Panels and colored text for a polished CLI experience.