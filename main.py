from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in range(0, 12):
    question_bank.append(Question(question_data[i]['text'], question_data[i]['answer']))


user = QuizBrain(question_bank)

while user.still_has_questions():
    user.next_question()

print("You have completed the quiz")
print(f"Your final score was : {user.score} correct answer out of {len(user.question_list)} questions")
