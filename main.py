import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label class
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "normal"))
# need a label component to display this customer label text which is down below
my_label.pack(side="left")  # add side=left/bottom/top/right to the component to change position of the label


window.mainloop()
