import json



class Player: #Represents a player in the CineQuiz game.
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.correct_answer_count = 0
        self.wrong_answer_count = 0

    def add_score(self, points: int):
        self.score += points

    def get_rank(self) -> str:
        if self.score >= 500:
            return "🏆 Cinema Legend"
        elif self.score >= 300:
            return "🎬 Film Buff"
        elif self.score >= 100:
            return "🍿 Movie Lover"
        else:
            return "🎥 Casual Viewer"

    def show_stats(self):
        total_questions = self.correct_answer_count + self.wrong_answer_count
        if total_questions > 0:
            percentage_correct = (self.correct_answer_count / total_questions) * 100
        else:
            percentage_correct = 0
        return f"{self.name} - Score: {self.score}, Correct: {self.correct_answer_count}, Wrong: {self.wrong_answer_count}, Accuracy: {percentage_correct:.2f}%"  


    def save_score(self):
        score_data = {
            "name": self.name,
            "score": self.score,
            "rank": self.get_rank()
        }
        
        try:
            # We open the file to append the new score
            with open("data/scores.json", "a") as f:
                f.write(json.dumps(score_data) + "\n")
        except FileNotFoundError:
            print("Error: scores.json not found.")  