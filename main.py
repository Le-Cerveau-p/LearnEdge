from tkinter import *
from tkinter import filedialog
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
French = "French"
English = "English"
Question = "Question"
A = 'Option A'
B = 'Option B'
C = 'Option C'
D = 'Option D'
C_Option = 'Correct Option'
new_card = None

# ---------------------------- CARD MANAGEMENT ------------------------------- #
# try:
#     data = pandas.read_csv("data/words_to_learn.csv")
# except FileNotFoundError:
#     data = pandas.read_csv("data/french_words.csv")
# finally:
#     to_learn = data.to_dict(orient="records")
data_file = filedialog.askopenfilename(title='select data file', filetypes=[('CSV files', '*.csv')])
data = pandas.read_csv(data_file)
questions = data.to_dict(orient="records")
no_of_questions = len(questions)
counter = 0
score = 0


def next_question():
    global  new_card, counter, score
    counter += 1
    if len(questions) > 0:
        new_card = choice(questions)
        canvas.itemconfig(canvas_img, image=card_front)
        canvas.itemconfig(title, text="Question", fill="black")
        canvas.itemconfig(text, text=new_card[Question], fill="black")
        canvas.itemconfig(option_1, text=f'a. {new_card[A]}', fill="black")
        canvas.itemconfig(option_2, text=f'b. {new_card[B]}', fill="black")
        canvas.itemconfig(option_3, text=f'c. {new_card[C]}', fill="black")
        canvas.itemconfig(option_4, text=f'd. {new_card[D]}', fill="black")
        canvas.itemconfig(correct_option, text='', fill="black")
        a_btn.config(state="active")
        b_btn.config(state="active")
        c_btn.config(state="active")
        d_btn.config(image=d_img, command=option_d)
    else:
        a_btn.config(state="disabled")
        b_btn.config(state="disabled")
        c_btn.config(state="disabled")
        d_btn.config(state="disabled")
        canvas.itemconfig(correct_option, text=f'Accuracy: {int(score * 100)}%', fill="black")


def flip_card():
    global new_card, score
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(title, text="Answer", fill="white")
    canvas.itemconfig(text, text=new_card[Question], fill="black")
    canvas.itemconfig(option_1, text=f'a. {new_card[A]}', fill="black")
    canvas.itemconfig(option_2, text=f'b. {new_card[B]}', fill="black")
    canvas.itemconfig(option_3, text=f'c. {new_card[C]}', fill="black")
    canvas.itemconfig(option_4, text=f'd. {new_card[D]}', fill="black")
    canvas.itemconfig(correct_option, text=f'correct option: {new_card[C_Option]}', fill="black")
    a_btn.config(state="disabled")
    b_btn.config(state="disabled")
    c_btn.config(state="disabled")
    d_btn.config(image=next_img, command=next_question)
    if counter == no_of_questions:
        print(counter)
        score = (no_of_questions - len(questions))/no_of_questions

def option_a():
    global new_card
    if new_card[C_Option] == 'A':
        update_known_question()
        flip_card()
    else:
        flip_card()

def option_b():
    global new_card
    if new_card[C_Option] == 'B':
        update_known_question()
        flip_card()
    else:
        flip_card()

def option_c():
    global new_card
    if new_card[C_Option] == 'C':
        update_known_question()
        flip_card()
    else:
        flip_card()

def option_d():
    global new_card
    if new_card[C_Option] == 'D':
        update_known_question()
        flip_card()
    else:
        flip_card()

# ---------------------------- KNOWN CARD MANAGEMENT ------------------------------- #

def update_known_question():
    global new_card
    questions.remove(new_card)


# ---------------------------- UI SETUP ------------------------------- #
# Window initialization
window = Tk()
window.title("Flash Card")
window.config(pady=20, padx=20, bg=BACKGROUND_COLOR)

# Card canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400,263, image=card_front)
title = canvas.create_text(400, 50, text="Title", font=(FONT_NAME, 15, "italic"))
text = canvas.create_text(60, 80, text="Text", font=(FONT_NAME, 25, "bold"), width=680, anchor=NW)
option_1 = canvas.create_text(60, 240, text="option_1", font=(FONT_NAME, 15, "bold"), anchor=NW)
option_2 = canvas.create_text(60, 280, text="option_2", font=(FONT_NAME, 15, "bold"), anchor=NW)
option_3 = canvas.create_text(60, 320, text="option_3", font=(FONT_NAME, 15, "bold"), anchor=NW)
option_4 = canvas.create_text(60, 360, text="option_4", font=(FONT_NAME, 15, "bold"), anchor=NW)
correct_option = canvas.create_text(120, 420, text="correct_option", font=(FONT_NAME, 20, "bold"), anchor=NW)
canvas.grid(row=0, column=0, columnspan=4)

# Buttons
a_img = PhotoImage(file="images/a.png")
a_btn = Button(image=a_img, highlightthickness=0, command=option_a)
a_btn.grid(row=1, column=0)

b_img = PhotoImage(file="images/b.png")
b_btn = Button(image=b_img, highlightthickness=0, command=option_b)
b_btn.grid(row=1, column=1)

c_img = PhotoImage(file="images/c.png")
c_btn = Button(image=c_img, highlightthickness=0, command=option_c)
c_btn.grid(row=1, column=2)

d_img = PhotoImage(file="images/d.png")
d_btn = Button(image=d_img, highlightthickness=0, command=option_d)
d_btn.grid(row=1, column=3)

next_img = PhotoImage(file="images/next.png")

next_question()

window.mainloop()