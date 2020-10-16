from tkinter import * 
from tkinter import messagebox
from random import choice

dutch = {}
english_keys = []
# {key is english: value is dutch}

words = open("A2 Vocab.txt")

for line in words:
    x = line.rstrip().split(";")
    key = x[0]
    value = x[1]
    dutch[key] = value
    english_keys.append(key)

# forming the interface
window = Tk()
window.title("Dutch Vocab Practice")
window.geometry("400x350+470+50")

# the question label
label_text = StringVar()
label = Label(window, textvariable = label_text, fg = "#738cbf", font = ("Verdana", 16))
label.place(x = 80, y = 50)

english_key = ""

def display(label):
    global english_key
    english_key = choice(english_keys)
    label_text.set("Translate: " + english_key)

# the answer text field
text_variable = StringVar()
text = Entry(window, textvariable = text_variable)
text.place(x = 80, y = 100)

def submit():
    global english_key
    answer = text.get()
    dutch_value = dutch[english_key]
    if answer == dutch_value:
        messagebox.showinfo("", "Goed antwoord!")
    else:
        messagebox.showinfo("", "Sorry! The correct answer is: " + dutch_value + ".")

    display(label)
    text_variable.set("")

# the submit button
button = Button(window, text = "Antwoord", fg = "black", font = ("Verdana", 14), command = submit)
button.place(x = 80, y = 150)

display(label)

window.mainloop()