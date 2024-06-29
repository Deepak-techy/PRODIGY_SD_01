from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Temperature Converter")
root.geometry("720x480")

def Celcius_to_temp(temp_C):
    temp_F = ((9/5 * temp_C) + 32)
    temp_K = (temp_C + 273.15)
    Label(f4, text="You have entered the temperature in Celcius.", font = "comicsans 12").grid(row=4, column=0, pady=10)
    Label(f4, text=f"The temperature in Fahrenheit is : {temp_F:.2F} °F", font = "comicsans 12").grid(row=5, column=0, pady=10)
    Label(f4, text=f"The temperature in Kelvin is : {temp_K:.2F} K", font = "comicsans 12").grid(row=6, column=0, pady=10)
   

def Fahrenheit_to_temp(temp_F):
    temp_C = (5/9 * (temp_F - 32))
    temp_K = (((temp_F - 32) * 5/9) + 273.15)
    Label(f4, text="You have entered the temperature in Fahrenheit.", font = "comicsans 12").grid(row=4, column=0, pady=10)
    Label(f4, text=f"The temperature in Celcius is : {temp_C:.2F} °C", font = "comicsans 12").grid(row=5, column=0, pady=10)
    Label(f4, text=f"The temperature in Kelvin is : {temp_K:.2F} K", font = "comicsans 12").grid(row=6, column=0, pady=10)

def Kelvin_to_temp(temp_K):
    temp_C = (temp_K - 273.15)
    temp_F = (((temp_K - 273.15) * 9/5) + 32)
    Label(f4, text="You have entered the temperature in Kelvin.", font = "comicsans 12").grid(row=4, column=0, pady=10)
    Label(f4, text=f"The temperature in Celcius is : {temp_C:.2F} °C", font = "comicsans 12").grid(row=5, column=0, pady=10)
    Label(f4, text=f"The temperature in Fahrenheit is : {temp_F:.2F} °F", font = "comicsans 12").grid(row=6, column=0, pady=10)

def clear_frame():
    for widget in f4.winfo_children():
        widget.destroy()

def convert_temp():
    try:
        unit = clicked.get()
        tempvalue = float(entrybox_temp.get())
        clear_frame()
        if unit == "Celsius":
            Celcius_to_temp(tempvalue)
        elif unit == "Fahrenheit":
            Fahrenheit_to_temp(tempvalue)
        elif unit == "Kelvin":
            Kelvin_to_temp(tempvalue)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the temperature.")

f1 = Frame(root)
f1.pack(padx=20, pady=20)

f2 = Frame(root)
f2.pack(padx=20, pady=20)

f3 = Frame(root)
f3.pack()

f4 = Frame(root)
f4.pack(padx=20, pady=20)

heading = Label(f1, text="Temperature Converter", font="comicsans 14 bold",)
heading.grid()

entry_unit = Label(f2, text="Select the unit of the temperature : ", font="comicsans 12 ")
entry_unit.grid(row = 1, column=0, pady=20)

options = [
    "Celsius",
    "Fahrenheit",
    "Kelvin"
]
clicked = StringVar()
drop_unit = OptionMenu(f2, clicked, *options)
drop_unit.grid(row = 1, column=1)

entry_temp = Label(f2, text = "Enter the temperature : ", font="comicsans 12")
entry_temp.grid(row=2, column=0, pady=20)

tempvalue = DoubleVar()

entrybox_temp = Entry(f2, textvariable=tempvalue)
entrybox_temp.grid(row=2, column=1, pady=20)

btn = Button(f3, text="Convert", font="comicsans 12", command=convert_temp)
btn.grid(row=3, column=0)

root.mainloop()
