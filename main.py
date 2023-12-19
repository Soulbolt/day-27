from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label class
my_label = Label(text="I Am a Label", font=("Arial", 24, "normal"))
# need a label component to display this customer label text which is down below
my_label.pack()  # add side=left/bottom/top/right to the component to change position of the label
my_label["text"] = "New Text"
my_label.config(text="new text")

# Button class, same guideline as above


def button_clicked():
    new_text = text_input.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
text_input = Entry(width=10)
text_input.pack()
button_clicked()


window.mainloop()
