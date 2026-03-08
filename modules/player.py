'''

This is your Player class. Before writing it, ask yourself:

What does a player have? → name, score, correct count, wrong count
What can a player do? → add score, get their rank, show their stats
How do I decide rank? → if/elif based on score or percentage correct
'''

class Player:
    def __init__(self, name: str):
        # your attributes here

    def add_score(self, points: int):
        # update score

    def get_rank(self) -> str:
        # return rank string based on score