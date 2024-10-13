from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html
from ui import QuizInterface

question_bank = []

# for each question from the data from the API
for question in question_data:
    # UNESCAPE: to decode the html entities like "&pound", "&amp;" or "&nbsp;"
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    # populate question bank
    question_bank.append(new_question)

# new quiz with the question bank
quiz = QuizBrain(question_bank)

# new user interface for the quiz
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
