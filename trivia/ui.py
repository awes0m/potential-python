from tkinter import *
THEME_COLOR = "#375362"
from  quiz_brain import QuizBrain
class QuizInterface:


    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quiz")
        self.window.config(padx=20,pady=40,bg=THEME_COLOR)

        self.score_l=Label(text="Score : 0",fg="white",bg=THEME_COLOR) #Score Label
        self.score_l.grid(column=1,row=0)
        self.Q_no=Label(text=f"{self.quiz.question_number}/10",fg="white",bg=THEME_COLOR)
        self.Q_no.grid(column=0,row=0)

        self.canvas=Canvas(width=300, height=250,bg="white")
        self.question_text=self.canvas.create_text(
            150,
            125,
            text="Question text",
            fill=THEME_COLOR,
            width=270,
            font=("Arial",13,"italic"))
        self.canvas.grid(column=0,row =1,columnspan=2,pady=50)

        #-------------------Buttons
        true_image=PhotoImage(file="images/true.png")
        false_image=PhotoImage(file="images/false.png")
        self.true_b=Button(image=true_image,highlightthickness=0,command=self.tru)
        self.true_b.grid(column=0,row=2)
        self.false_b=Button(image=false_image,highlightthickness=0,command=self.fals)
        self.false_b.grid(column=1,row=2)

        self.get_nxt_question()

        self.window.mainloop()



    def get_nxt_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_l.config(text=f"Score:{self.quiz.score}")
            self.Q_no.config(text=f"{self.quiz.question_number}/10")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.config(bg="white")
            self.Q_no.config(text="10/10")
            self.canvas.itemconfig(self.question_text,text=f"Game ends! Final score: {self.quiz.score}")
            self.true_b.config(state=DISABLED)
            self.false_b.config(state=DISABLED)

    def tru(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def fals(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000,self.get_nxt_question)
            print("right")
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_nxt_question)
            print("wrong")






