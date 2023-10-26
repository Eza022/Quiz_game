# Sample Python Quiz Game
import random

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {   "question" : "What country has the highest life expectancy?",
        "options" : ["Nigeria", "Cuba", "Hong Kong", "China"],
        "answer" : "Hong Kong"
     },
     {  "question" : "How many elements are in the periodic table?",
        "options"  : ["114", "112", "118", "116"],
        "answer"   : "118"
         
     },
     {  "question" : "Which planet in the Milky Way is the hottest?",
         "options" : ["Pluto", "Mars", "Venus", "Saturn"],
         "answer"  : "Venus"
         
     },
     {  "question" : "Who discovered that the earth revolves around the sun?",
        "options"  : ["Nicolaus Copernicus", "Isaac Newton", "Marie Curie", "Galileo Galilei"],
        "answer"   : "Nicolaus Copernicus"
         
     }
    # Add more questions here
]

players = []
scores = {}

def add_player(player_name):
    players.append(player_name)
    scores[player_name] = 0

def ask_question(question_obj):
    random.shuffle(question_obj["options"])
    print(question_obj["question"])
    for i, option in enumerate(question_obj["options"], start=1):
        print(f"{i}. {option}")
    player_answer = input("Select an option: ")
    return question_obj["options"][int(player_answer) - 1]

def main():
    num_players = int(input("Enter the number of players: "))
    for _ in range(num_players):
        player_name = input("Enter player name: ")
        add_player(player_name)

    for question in questions:
        random.shuffle(players)
        for player in players:
            print(f"{player}'s turn:")
            answer = ask_question(question)
            if answer == question["answer"]:
                scores[player] += 1

    # Display final scores
    print("Final Scores:")
    for player, score in scores.items():
        print(f"{player}: {score} points")

if __name__ == "__main__":
    main()
