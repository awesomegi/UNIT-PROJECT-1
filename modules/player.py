import json
from datetime import date

class Player:
    def __init__(self, name, category="General"):
        self.name     = name
        self.category = category  # store it
        self.score    = 0
        self.correct_answer_count = 0
        self.wrong_answer_count   = 0
        self.streak     = 0
        self.max_streak = 0

    def add_score(self, base_points):
        # streak multiplier: 1x → 2.5x max
        multiplier = min(1.0 + self.streak * 0.5, 2.5)
        earned = int(base_points * multiplier)
        self.score += earned
        if self.streak >= 2:
            print(f"🔥 {self.streak}-streak! x{multiplier:.1f} → +{earned} pts")
        return earned

    def on_correct(self):
        self.correct_answer_count += 1
        self.streak += 1
        self.max_streak = max(self.max_streak, self.streak)
        self.add_score(100)

    def on_wrong(self, correct_answer):
        self.wrong_answer_count += 1
        self.streak = 0
        print(f"❌ Wrong! The answer was: {correct_answer}")

    @property
    def accuracy(self):
        total = self.correct_answer_count + self.wrong_answer_count
        return round((self.correct_answer_count / total) * 100) if total else 0

    def get_rank(self):
        # rank titles per category
        ranks = {
            "Movies":      ["🎟️ First Timer",    "🍿 Film Buff",     "⭐ Star Player",    "🎬 Movie Legend"],
            "Music":       ["🎵 Off Key",         "🎸 Music Fan",     "🎤 Chart Topper",   "🎼 Music Legend"],
            "Science":     ["🔬 Lab Rookie",      "⚗️ Researcher",    "🧪 Scientist",      "🏆 Nobel Tier"],
            "History":     ["📜 Apprentice",      "🏛️ Historian",     "⚔️ Scholar",        "👑 Time Lord"],
            "Sports":      ["🥉 Benchwarmer",     "🏅 Rookie",        "🏆 MVP",            "🐐 GOAT"],
           "Video Games": ["🕹️ Noob",           
                            "👾 Gamer",         "⚔️ Pro Player",     "🏆 Legend"],
           "General":     ["🌱 Beginner",        "📚 Quiz Fan",      "🧠 Brainiac",       "🏆 Genius"],
     }

       # fall back to General if category not in the dict
        titles = ranks.get(self.category, ranks["General"])
        if self.score >= 800: return titles[3]
        if self.score >= 500: return titles[2]
        if self.score >= 300: return titles[1]
        return titles[0]
    
    
    
    
    def save_score(self):
        entry = {
            "name":       self.name,
            "score":      self.score,
            "rank":       self.get_rank(),
            "accuracy":   f"{self.accuracy}%",
            "max_streak": self.max_streak,
            "date":       str(date.today()),
        }
        with open("data/scores.json", "a") as f:
            f.write(json.dumps(entry) + "\n")