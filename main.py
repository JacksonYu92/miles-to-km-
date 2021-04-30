from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def calculate():
    km = float(miles_entry.get()) * 1.609
    km_data_label.config(text=f"{km}")

miles_entry = Entry(width=7)
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

km_data_label = Label(text="0")
km_data_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)


calculate_button= Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)






window.mainloop()