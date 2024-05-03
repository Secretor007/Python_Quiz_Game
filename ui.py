THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="some question text",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, borderwidth=0, highlightthickness=0,command=self.true_answer)
        self.true_btn.grid(row=2, column=0)
        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, borderwidth=0, highlightthickness=0,command=self.false_answer)
        self.false_btn.grid(row=2, column=1)
        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(tagOrId=self.question_text, text=q_text)
        else:
            self.canvas.itemconfigure(self.question_text,text="You have reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
    def true_answer(self):
        answer = "True"
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def false_answer(self):
        answer = "False"
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)