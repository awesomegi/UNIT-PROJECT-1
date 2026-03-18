from modules.game import run_game
from modules.utils import get_leaderboard
from modules.display import show_leaderboard
import pyfiglet

import pyfiglet

if __name__ == "__main__":
    title = pyfiglet.figlet_format("CineQuiz", font="slant")
    print(title)
    print("🎬 Welcome to the Ultimate Movie Trivia!")
    
    # Keep showing the menu until the player quits
    while True:
        print("\n══════════════ MAIN MENU ══════════════")
        print("[1] Play")
        print("[2] View Leaderboard") 
        print("[3] Quit")
        print("═══════════════════════════════════════")
        
        choice = input("→ ").strip()
        
        if choice == "1": 
            run_game()
        elif choice == "2":
            scores = get_leaderboard()
            show_leaderboard(scores)

        elif choice == "3":
            print("\n🎬 Thanks for playing CineQuiz. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or 3.")
