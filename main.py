from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for info in question_data:
    obj = Question(info["text"],info["answer"])
    question_bank.append(obj)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the Quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")