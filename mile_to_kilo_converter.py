from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=550, height=300)
window.config(padx=50, pady=50)

miles_label = Label(text="Miles", font=("Arial", 28, "normal"))
miles_label.grid(column=2, row=0)
is_equal_to_label = Label(text="is equal to", font=("Arial", 28, "normal"))
is_equal_to_label.grid(column=0, row=1)
num_placeholder = 0
kilometers_result = Label(text=f"{num_placeholder}", font=("Arial", 28, "normal"))
kilometers_result.grid(column=1, row=1)
kilometers_label = Label(text="Km", font=("Arial", 28, "normal"))
kilometers_label.grid(column=2, row=1)

miles_entry = Entry(width=8, font=("Arial", 28, "normal"))
miles_entry.grid(column=1, row=0)
miles_entry.insert(END, string="0")


def calculate_miles_to_km():
    miles = miles_entry.get()
    conversion_factor = 0.62137119
    kilometers = int(miles) / conversion_factor
    kilometers_result.config(text=f"{round(kilometers, 2)}")


calculate_button = Button(text="Calculate", command=calculate_miles_to_km, font=("Arial", 28, "normal"))
calculate_button.grid(column=1, row=2)


window.mainloop()
