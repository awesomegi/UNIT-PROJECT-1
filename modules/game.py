from modules.player import Player
from modules.api import fetch_questions
import random
import threading
from modules.utils import game_banner
from rich.console import Console
from rich.panel import Panel

console = Console()


def ask_with_timer(seconds=15):
    answered = threading.Event()
    answer = [None]

    def get_input():
        answer[0] = input("\n→ ").upper().strip()
        answered.set()

    t = threading.Thread(target=get_input, daemon=True)
    t.start()

    for remaining in range(seconds, 0, -1):
        if answered.is_set():
            break
        print(f"\r⏱️  {remaining}s remaining...  ", end="", flush=True)
        answered.wait(timeout=1)

    print()
    if not answered.is_set():
        print("⌛ Time's up!")
        return ""
    return answer[0]


@game_banner
def run_game():
    print("🎬 Welcome to CineQuiz!")
    name = input("Enter your name: ")
    player = Player(name)
    hints_remaining = 2

    # difficulty menu
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

    questions, category_name = fetch_questions(5, difficulty)  # ← unpack
    player = Player(name, category=category_name)   

    # abort if API fails
    if not questions:
        print("❌ Could not load questions. Check your internet and try again.")
        return

    for index, question in enumerate(questions):
        print(f"\n❓ Question {index + 1} of {len(questions)}")
        print(question['question'])

        # build + shuffle options
        options = question['incorrect_answers'] + [question['correct_answer']]
        random.shuffle(options)

        for i, option in enumerate(options):
            print(f"[{chr(65 + i)}] {option}")

        print(f"\n[H] Use a hint ({hints_remaining} left)  or enter A/B/C/D")

        # get answer
        valid_options = [chr(65 + i) for i in range(len(options))] + ["H"]
        answer = ask_with_timer(15)

        while answer not in valid_options:
            print(f"⚠️ Invalid input! Please enter {', '.join(valid_options)}")
            answer = ask_with_timer(15)

        # timeout → wrong
        if answer == "":
            player.on_wrong(question['correct_answer'])
            continue

        # hint
        if answer == "H":
            if hints_remaining > 0 and len(options) > 2:
                hints_remaining -= 1
                wrong = [o for o in options if o != question['correct_answer']]
                options.remove(wrong[0])
                print("\n💡 Hint used! One wrong answer removed:")
                for i, option in enumerate(options):
                    print(f"[{chr(65 + i)}] {option}")
                valid_options = [chr(65 + i) for i in range(len(options))]
                answer = ask_with_timer(15)
                while answer not in valid_options:
                    answer = ask_with_timer(15)
            else:
                print("❌ No hints left!" if hints_remaining == 0 else "⚠️ Not enough options!")
                answer = ask_with_timer(15)

        # check answer
        selected = options[ord(answer) - 65]
        if selected == question['correct_answer']:
            print("✅ Correct!")
            player.on_correct()
        else:
            player.on_wrong(question['correct_answer'])

        console.print(f"[dim]Score so far: [bold yellow]{player.score}[/bold yellow] pts[/dim]")

    # save + show results
    player.save_score()
    print("📁 Score saved to leaderboard!")
   

    console.print(Panel(
        f"[bold green]✅ Correct: {player.correct_answer_count}[/bold green]\n"
        f"[bold red]❌ Wrong:   {player.wrong_answer_count}[/bold red]\n"
        f"[bold yellow]🔥 Best streak: {player.max_streak}[/bold yellow]\n"
        f"[bold cyan]🎯 Accuracy: {player.accuracy}%[/bold cyan]",
        title=f"[bold]🏆 Game Over, {player.name}![/bold]",
        subtitle=f"Final score: [bold green]{player.score}[/bold green] pts — {player.get_rank()}"
    ))