class Question:

    # class method for object initialization
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    # method which handles displaying questions
    def display_question(self):
        print(self.question)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    # method to check correct answers
    def is_correct(self, player_answer):
        return player_answer == self.correct_answer
