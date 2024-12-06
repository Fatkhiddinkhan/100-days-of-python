from tkinter import *
def calculation():
    """takes number from input, returns calculated km"""
    num = float(input.get())
    km_result = num * 1.609344
    num_label.config(text=round(km_result, 0))

#window config
window = Tk()
window.title("Mile To Km")
window.minsize(width=300, height=170)
window.config(padx=30, pady=30)

##labels config
input = Entry(width=10)
input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

num_label = Label(text=0)
num_label.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=calculation)
calc_button.grid(column=1, row=2)














window.mainloop()