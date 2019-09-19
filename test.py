from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Vi")
root.geometry('300x300')

def que_one():
    question = Label(root, text = "Question One" )
    answer = Entry()
    btn = Button(root, text = "Submit", command = lambda: game1(que_two))

    question.grid(row = 0)
    answer.grid(row = 1)
    btn.grid(row = 2)

    def game1 (que_two):
        if answer.get().lower() == "1":
            que_two()
        else:
            messagebox.showerror("Error!", "Try again.")

def que_two():
    question_2 = Label(root, text = "Question Two")
    answer_2 = Entry()
    btn_2 = Button(root, text = "Submit", command = lambda: game2(que_two))

    question_2.grid()
    answer_2.grid()
    btn_2.grid('')

    def game2 (que_two):
        if answer_2.get().lower() == "2":
            messagebox.showinfo("You win!", "Nice game!")
        else:
            messagebox.showerror("Error!", "Try again.")

# def que_three():
#     question_3 = Label(root, text = "Question Three")
#     answer_3 = Entry()
#     btn_3 = Button(root, text = "Submit")
#
#     question_3.grid(row = 0)
#     answer_3.grid(row = 1)
#     btn_3.grid(row = 2)

# def que_two():
#     question_2 = Label(root, text = "Question Two", command = lambda: game2(que_three))
#     answer_2 = Entry()
#     btn_2 = Button(root, text = "Submit")
#
#    question_2.grid(row = 0)
#    answer_2.grid(row = 1)
#    btn_2.grid(row = 2)
#
#    def game2 (que_three):
#        if answer_2 == "2":
#            que_three()
#      else:
#           messagebox.showerror("Error!", "Try again.")
#
# def que_three():
#    question_3 = Label(root, text = "Question Three")

que_one()

root.mainloop()
