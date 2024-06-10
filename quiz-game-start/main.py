from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
	question_text = question["text"]
	question_answer = question["answer"]
	model_question = Question(question_text, question_answer)
	question_bank.append(model_question)

quiz = QuizBrain(question_bank)

print("Welcome to the quiz!")

while quiz.still_has_question():
	quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.question_number}/{len(question_bank)}")