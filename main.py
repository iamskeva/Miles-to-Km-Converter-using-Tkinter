from tkinter import *
window = Tk()
window.title("Mile to KM Converter")
window.config(padx=30, pady=30)


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    result_label.config(text=f"{km}")


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Courier", 15, "normal"))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Courier", 15, "normal"))
is_equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km", font=("Courier", 15, "normal"))
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", font=("Courier", 15, "normal"), command=miles_to_km)
calculate_button.grid(column=1, row=2)
