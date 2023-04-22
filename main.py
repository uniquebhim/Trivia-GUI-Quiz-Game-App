from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import Quizinterface

# create an empty list to hold the questions
question_bank = []

# loop through each question in the question data and create a Question object
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# create a new QuizBrain object with the list of questions
quiz = QuizBrain(question_bank)

# create a new Quizinterface object with the QuizBrain object
quiz_ui = Quizinterface(quiz)

# print the final score after the quiz game has ended
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
