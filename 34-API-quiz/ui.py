from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    """User Interface class"""

    # quiz_brain must be of data type QuizBrain
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        # window
        self.window = Tk()
        self.window.title("Quiz Quiz")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # score label
        self.score_lbl = Label(text="Score:", background=THEME_COLOR, foreground="white")

        # canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,  # width of the text, then it wraps and go to the next line
            text="QUIZ QUIZ",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )

        # true button
        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.button_true)

        # false button
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.button_false)

        # grid layout
        self.score_lbl.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        # gets the first question
        self.get_next_question()

        # window main loop
        self.window.mainloop()

    def get_next_question(self):

        # reset the bg color
        self.canvas.config(bg="white")

        # if still has questions
        if self.quiz.still_has_questions():
            # update score
            self.score_lbl.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # end of the quiz
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def button_true(self):
        # check if the user answered correct
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def button_false(self):
        # check if the user answered correct
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        # changes color according to right or wrong answer
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # delay of 1 second and then call the function
        self.window.after(1000, self.get_next_question)

