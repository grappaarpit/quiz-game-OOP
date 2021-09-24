class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number >= len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_choice = input(f"Q.{self.question_number+1} {current_question.text} : (True/False) ")
        self.question_number += 1
        self.check_answer(user_choice, current_question)

    def check_answer(self, user_choice, current_question):
        if user_choice == current_question.answer:
            print("You are correct")
            self.score += 1
        else:
            print("That is wrong, bitch")
        print(f"The correct answer is {current_question.answer}")
        print(f"The current score is {self.score}/{self.question_number}")
        print("\n")




