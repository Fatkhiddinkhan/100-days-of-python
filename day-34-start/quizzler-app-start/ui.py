from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        ## next question
        self.quiz = quiz_brain
        # window config
        self.window = Tk()
        self.window.title("QuizQuiz")
        self.window.config(bg=THEME_COLOR)
        ## score check
        self.score = Label(text="Score: 0")
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 14, "bold"))
        self.score.grid(row=0, column=1, padx=20, pady=20)
        ## canvas config
        self.canvas = Canvas(bg="white")
        self.canvas.config(width=300, height=250, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)
        ### canvas text config
        self.text = self.canvas.create_text(150, 125, width=280, text="Here is new text", fill="black",font=("Arial", 20, "italic"))
        ## button config
        false = PhotoImage(file="images/false.png")
        true = PhotoImage(file="images/true.png")

        self.true_button = Button(image=true, highlightthickness=0, bd=0, command=self.true_answer)
        self.true_button.grid(row=2, column=1, pady=20, padx=20)
        self.false_button = Button(image=false, highlightthickness=0, bd=0, command=self.false_answer)
        self.false_button.grid(row=2, column=0, pady=20, padx=20)

        self.get_new_question()

        self.window.mainloop()

    def get_new_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)

        else:
            self.canvas.itemconfig(self.text, text="You have reached finish")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_new_question)






