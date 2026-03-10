import requests
import html


def fetch_questions(amount: int, difficulty: str) -> list: #Fetches movie trivia questions from OpenTDB API. Returns a list of question dictionaries."""
    url = f"https://opentdb.com/api.php?amount={amount}&category=11&difficulty={difficulty}&type=multiple"
    print(url)  # temporary, just to see it works
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # check for HTTP errors
        data = response.json()
        return [dict(q, question=html.unescape(q['question'])) for q in data['results']]
    
    except requests.RequestException as e:
        print(f"Error fetching questions: {e}")
        return []  # return an empty list on error