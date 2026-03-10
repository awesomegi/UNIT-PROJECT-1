from modules.player import Player
from modules.api import fetch_questions
import random
from modules.utils import game_banner

@game_banner
def run_game():
    print("🎬 Welcome to CineQuiz!")
    name = input("Enter your name: ")
    player = Player(name)

    # Let the player choose their challenge level    
    print("\nChoose difficulty:")
    print("[1] Easy")
    print("[2] Medium")
    print("[3] Hard")
        
        
    choice = input("→ ")
    
    # Match the player's choice to a difficulty level    
    if choice == "1":
        difficulty = "easy"
    elif choice == "2":
        difficulty = "medium"
    elif choice == "3":
        difficulty = "hard"
    else:
        print("Invalid choice, defaulting to medium.")
        difficulty = "medium"

    questions = fetch_questions(10, difficulty)

    
    # Stop the game if no questions were fetched
    if not questions:
        print("❌ Could not load questions. Check your internet and try again.")
        return
    
    # Loop through each question one by one
    for index, question in enumerate(questions):
        print(f"\n❓ Question {index + 1} of {len(questions)}")
        print(question['question'])
        
        # Build the options list (correct + incorrect combined)
        options = question['incorrect_answers'] + [question['correct_answer']]
        random.shuffle(options)
        
        # Show each option with a letter
        for i, option in enumerate(options):
            print(f"[{chr(65 + i)}] {option}")

       # Get the player's answer and validate it
        valid_options = [chr(65 + i) for i in range(len(options))]
        answer = input("\n→ ").upper().strip()
        
        while answer not in valid_options:
            print(f"⚠️ Invalid input! Please enter {', '.join(valid_options)}")
            answer = input("→ ").upper().strip()
        
        # Check if the answer is correct
        selected = options[ord(answer) - 65]
        if selected == question['correct_answer']:
            print("✅ Correct! +100 pts")
            player.add_score(100)
            player.correct_answer_count += 1
        else:
            print(f"❌ Wrong! The answer was: {question['correct_answer']}")
            player.wrong_answer_count += 1


    # Show final results            
    print(f"\n🏆 Game Over, {player.name}!")
    print(f"📊 Final Score: {player.score}")
    print(f"✅ Correct Answers: {player.correct_answer_count}")
    print(f"❌ Wrong Answers: {player.wrong_answer_count}")

    player.save_score()
    print("📁 Score saved to leaderboard!")