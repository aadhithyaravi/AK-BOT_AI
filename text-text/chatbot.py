import json
import random

with open("intents.json", "r") as f:
    datas = json.load(f)

def talk():
    user_input = input("You: ").lower().strip().split()
    best_match = None
    best_score = 0

    for intent in datas["intents"]:
        for pattern in intent["patterns"]:
            pattern_words = pattern.lower().strip().split()
            common = set(user_input) & set(pattern_words)
            score = len(common)  

            if score > best_score:
                best_score = score
                best_match = intent

    if best_match and best_score > 0:
        response = random.choice(best_match["responses"])
        print(f"Bot: {response}")
        print("over ✅")
    else:
        print("😒 I didn’t understand that.")

while True:
    talk()
