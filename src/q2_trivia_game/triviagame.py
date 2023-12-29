import json
import random
from question import Question


def play_trivia_game(questions):
    player1_score = 0
    player2_score = 0

    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion #{i} for Player 1:")
        question.display_question()
        player1_answer = int(input("Enter your answer as a number (e.g. 1, 2, 3, or 4): "))
        if question.is_correct(player1_answer):
            player1_score += 1

        print(f"\nQuestion {i} for Player 2:")
        question.display_question()
        player2_answer = int(input("Enter your answer as a number(e.g. 1, 2, 3, or 4): "))
        if question.is_correct(player2_answer):
            player2_score += 1

        if i == 10:
            break

    print("\nGame Over!")
    print(f"\nPlayer 1 Score: {player1_score}")
    print(f"Player 2 Score: {player2_score}")

    if player1_score > player2_score:
        print("Congratulations! Player 1 wins!")
    elif player2_score > player1_score:
        print("Congratulations! Player 2 wins!")
    else:
        print("It was a nice battle! It's a tie!")


def main():
    with open('questions.json', 'r') as file:
        json_data = json.load(file)

    questions_data_json = json_data['list_of_questions']
    questions_data_dictionary = [
        {
            "question": q["question"],
            "options": q["options"],
            "correct_answer": q["correct_answer"]
        }
        for q in questions_data_json
    ]

    random.shuffle(questions_data_dictionary)
    random_questions = questions_data_dictionary[:10]

    questions = [Question(q["question"], q["options"], q["correct_answer"]) for q in random_questions]

    play_trivia_game(questions)


if __name__ == "__main__":
    main()
