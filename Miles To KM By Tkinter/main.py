from tkinter import *


def miles_to_km():
    miles_local = float(miles.get())
    km = miles_local * 1.609
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles To KM Convertor")
window.config(padx=20, pady=20)

miles = Entry(width=6)
miles.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=2, pady=2)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=2, pady=2)

km_result_label = Label(text='0')
km_result_label.grid(column=1, row=1)
km_result_label.config(padx=2, pady=2)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)
km_label.config(padx=2, pady=2)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=2, pady=2)

window.mainloop()
