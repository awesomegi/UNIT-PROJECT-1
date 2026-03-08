from modules.player import Player
from modules.api import fetch_questions


def run_game():
    print("🎬 Welcome to CineQuiz!")
    name = input("Enter your name: ")
    player = Player(name)
        
    print("\nChoose difficulty:")
    print("[1] Easy")
    print("[2] Medium")
    print("[3] Hard")
        
        
    choice = input("→ ")
        
    if choice == "1":
        difficulty = "easy"
    elif choice == "2":
        difficulty = "medium"
    elif choice == "3":
        difficulty = "hard"
    else:
        print("Invalid choice, defaulting to medium.")
        difficulty = "medium"