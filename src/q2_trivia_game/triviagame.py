import json  # json library to parse json file with questions
import random  # random library to get random questions from the json file
from question import Question  # importing Question class


def play_trivia_game(questions):
    # initial scores of players
    player1_score = 0
    player2_score = 0

    for i, question in enumerate(questions, start=1):  # cycle to manipulate with questions
        print(f"\nQuestion #{i} for Player 1:")
        question.display_question()  # using Question class method to display question
        player1_answer = int(input("Enter your answer as a number (e.g. 1, 2, 3, or 4): "))
        if question.is_correct(player1_answer):  # using Question class method to check answer
            player1_score += 1  # counter

        print(f"\nQuestion {i} for Player 2:")
        question.display_question()
        player2_answer = int(input("Enter your answer as a number(e.g. 1, 2, 3, or 4): "))
        if question.is_correct(player2_answer):
            player2_score += 1

        if i == 10:  # to show only 10 questions
            break

    print("\nGame Over!")
    print(f"\nPlayer 1 Score: {player1_score}")
    print(f"Player 2 Score: {player2_score}")

    # check players score and print the winner
    if player1_score > player2_score:
        print("Congratulations! Player 1 wins!")
    elif player2_score > player1_score:
        print("Congratulations! Player 2 wins!")
    else:
        print("It was a nice battle! It's a tie!")


def main():
    with open('questions.json', 'r') as file:  # open json file with a questions
        json_data = json.load(file)  # load data from json file

    questions_data_json = json_data['list_of_questions']  # parse questions using list_of_questions key in json file

    # create a python dictionary with questions from parsed json data
    questions_data_dictionary = [
        {
            "question": q["question"],
            "options": q["options"],
            "correct_answer": q["correct_answer"]
        }
        for q in questions_data_json
    ]

    random.shuffle(questions_data_dictionary)  # shuffle dictionary to get random questions
    random_questions = questions_data_dictionary[:10]  # use only 10 random questions

    # create a class object
    questions = [Question(q["question"], q["options"], q["correct_answer"]) for q in random_questions]

    play_trivia_game(questions)


if __name__ == "__main__":
    main()
