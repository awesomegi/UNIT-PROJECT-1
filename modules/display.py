from rich.console import Console
from rich.table import Table

console = Console()

def show_leaderboard(scores):
    table = Table(title="🏆 CINEQUIZ LEADERBOARD 🏆", style="yellow")
    
    table.add_column("Rank", justify="center", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("Score", justify="right", style="green")
    table.add_column("Rank Title", style="blue")

    if not scores:
        console.print("[bold red]No scores yet. Be the first![/bold red]")
    else:
        for i, entry in enumerate(scores, 1):
            table.add_row(str(i), entry['name'], str(entry['score']), entry['rank'])
        
        console.print(table)