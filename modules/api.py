# modules/api.py
import requests
import html

# Category map: name → Open Trivia DB category ID
CATEGORIES = {
    "Movies":       11,
    "Music":        12,
    "Science":      17,
    "History":      23,
    "Sports":       21,
    "Video Games":  15,
    "General":       9,
}

def choose_category():
    print("\nChoose a category:")
    for i, name in enumerate(CATEGORIES, 1):
        print(f"[{i}] {name}")

    choice = input("→ ").strip()
    keys = list(CATEGORIES.keys())

    if choice.isdigit() and 1 <= int(choice) <= len(keys):
        name = keys[int(choice) - 1]
    else:
        print("Invalid choice, defaulting to Movies.")
        name = "Movies"

    print(f"✅ Category: {name}")
    return CATEGORIES[name], name  # ← return both ID and name


def fetch_questions(amount, difficulty):
    category_id, category_name = choose_category()   

    url = "https://opentdb.com/api.php"
    params = {
        "amount":     amount,
        "difficulty": difficulty,
        "type":       "multiple",
        "category":   category_id,        # ← new line
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        questions = data.get("results", [])
        # Decode HTML entities like &quot; → "
        for q in questions:
            q["question"]         = html.unescape(q["question"])
            q["correct_answer"]   = html.unescape(q["correct_answer"])
            q["incorrect_answers"] = [html.unescape(a) for a in q["incorrect_answers"]]
        return questions, category_name
   
    except Exception as e:
        print(f"❌ API Error: {e}")
        return []