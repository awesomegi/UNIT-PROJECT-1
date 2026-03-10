import json

def get_leaderboard():
    leaderboard = []
    try:
        with open("data/scores.json", "r") as f:
            for line in f:
                if line.strip():
                    leaderboard.append(json.loads(line))
        
        # Sort by score (highest first)
        leaderboard.sort(key=lambda x: x['score'], reverse=True)
        return leaderboard[:5]  # Top 5 only
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def game_banner(func):
    def wrapper(*args, **kwargs):
        print("\n" + "="*30)
        print("🎬 CINEQUIZ LOADING...")
        print("="*30)
        return func(*args, **kwargs)
    return wrapper