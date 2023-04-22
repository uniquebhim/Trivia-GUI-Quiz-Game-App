import html

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0     # current question number
        self.score = 0               # current score
        self.question_list = question_list   # list of question objects
        self.current_question = None         # current question object

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]  # get next question from list
        self.question_number += 1    # increment question number
        q_text = html.unescape(self.current_question.text)  # decode HTML entities in question text
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():   # compare answer with correct answer, ignoring case
            self.score += 1    # increment score if answer is correct
            # print("You got it right!")
            return True
        else:
            # print("That's wrong.")
            return False

    def get_score(self):
        return f"Your final score is: {self.score}/{self.question_number}"
