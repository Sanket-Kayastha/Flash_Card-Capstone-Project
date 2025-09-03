BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
current_card = {}
'''.........................................Pandas............................................................'''
data = pandas.read_csv("day31\data/french_words.csv")
data_dict = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card,flip_timmer
    window.after_cancel(flip_timmer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill = "black")
    canvas.itemconfig(card_word, text=current_card["French"], fill = "black")
    canvas.itemconfig(card_frontImage, image=front_photo)
    flip_timmer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text ="English", fill = "white")
    canvas.itemconfig(card_word, text=current_card["English"], fill = "white")
    canvas.itemconfig(card_frontImage, image = back_image)

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("day31\data\learn_word.csv")

    next_card()

'''........................................UI.................................................................'''
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

flip_timmer = window.after(3000, func=flip_card)

canvas = Canvas(width=800,height=526)
front_photo = PhotoImage(file="day31\images/card_back.png")
back_image = PhotoImage(file="day31\images\card_back.png")
card_frontImage=canvas.create_image(400,263,image=front_photo)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400,153,text="", font=("Arial",48,"italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 52, "bold"))
canvas.grid(column=0,row=0, columnspan=3)

cross_button = PhotoImage(file="day31\images\wrong.png")
unknown_button = Button(image=cross_button, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_button = PhotoImage(file="day31\images/right.png")
known_button = Button(image=check_button, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=2)


next_card()

window.mainloop()
