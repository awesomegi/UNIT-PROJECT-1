from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def show_leaderboard(scores):
    if not scores:
        console.print(Panel("[bold red]No scores yet. Be the first![/bold red]", title="🏆 Leaderboard"))
        return

    table = Table(title="🏆 CINEQUIZ LEADERBOARD 🏆", style="yellow", border_style="dim")

    table.add_column("Rank",       justify="center", style="cyan",    no_wrap=True)
    table.add_column("Name",                         style="magenta")
    table.add_column("Score",      justify="right",  style="green")
    table.add_column("Accuracy",   justify="center", style="white")    # ← new
    table.add_column("Best Streak",justify="center", style="yellow")   # ← new
    table.add_column("Date",       justify="center", style="dim")      # ← new
    table.add_column("Rank Title",                   style="blue")

    for i, entry in enumerate(scores, 1):
        medal = ["🥇","🥈","🥉"].pop(0) if i <= 3 else str(i)
        table.add_row(
            medal,
            entry["name"],
            str(entry["score"]),
            entry.get("accuracy",   "N/A"),   # .get() handles old saves safely
            str(entry.get("max_streak", 0)),
            entry.get("date", "—"),
            entry["rank"],
        )

    console.print(table)