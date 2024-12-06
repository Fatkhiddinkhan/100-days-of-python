from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

## label
my_label = Label(text="This Is Label")
## treating object like dictionary index
my_label["text"] = "Dict Version Label"
## config method
my_label.config(text="Config Version Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

## button
def click():
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click", command=click)
button.grid(column=2, row=0)

button1 = Button(text="Click", command=click)
button1.grid(column=1, row=1)

## entry

input = Entry(width=10)
input.grid(column=3, row=2)



window.mainloop()