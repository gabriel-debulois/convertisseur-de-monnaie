from tkinter import *
from tkinter import ttk

convertor = Tk()
convertor.geometry("700x500")
convertor.resizable(width=False, height=False)
convertor.title("Currency converter")

expression = ""
display_history = []
input_text = StringVar()
display_result = StringVar()

EURto = {"USD": 1.09, "GBP": 0.88, "YEN": 141.03, "CNY": 7.37}
USDto = {"EUR": 0.92, "GBP": 0.81, "YEN": 129.37, "CNY": 6.74}
GBPto = {"EUR": 1.13, "USD": 1.23, "YEN": 159.56, "CNY": 8.32}
YENto = {"EUR": 0.0071, "USD": 0.0077, "GBP": 0.0063, "CNY": 0.052}
CNIto = {"EUR": 0.14, "USD": 15.27, "YEN": 19.18, "GBP": 0.12}

# List for Combobox
type_currency = ["EUR", "USD", "GBP", "YEN", "CNY"]


# Function to convert the currency to another
def convert():
    global expression
    try:
        if from_currency.get() == "EUR":
            expression = int(float(input_text.get())) * EURto[to_currency.get()]
            display_result.set("{0:.2f}".format(expression))

        elif from_currency.get() == "USD":
            expression = int(float(input_text.get())) * USDto[to_currency.get()]
            display_result.set("{0:.2f}".format(expression))

        elif  from_currency.get() == "GBP":
            expression = int(float(input_text.get())) * GBPto[to_currency.get()]
            display_result.set("{0:.2f}".format(expression))

        elif from_currency.get() == "YEN":
            expression = int(float(input_text.get())) * YENto[to_currency.get()]
            display_result.set("{0:.2f}".format(expression))

        elif from_currency.get() == "CNY":
            expression = int(float(input_text.get())) * CNIto[to_currency.get()]
            display_result.set("{0:.2f}".format(expression))

        # Retrieves information from the input and the result to display it
        history = input_text.get() + from_currency.get() + " = " + "{0:.2f}".format(expression) + to_currency.get()
        listbox_h.insert(0, history)

    except:
        display_result.set("Conversion impossible")


# Function to clear the content of listbox
def clear():
    listbox_h.delete(0, END)


amount_label = Label(convertor, text='AMOUNT:')
amount_label.place(x=100, y=40)

# Entry to declare the value to convert
entry_value = Entry(convertor, textvariable=input_text, width=15, font=1)
entry_value.place(x=180, y=40)

from_label = Label(convertor, text='FROM:')
from_label.place(x=117, y=130)

# List FROM the money to convert
from_currency = ttk.Combobox(convertor, values=type_currency, state="readonly")
from_currency.set("Pick a currency")
from_currency.place(x=180, y=130)

from_label = Label(convertor, text='TO:')
from_label.place(x=360, y=130)

# List which type of currency to convert to
to_currency = ttk.Combobox(convertor, values=type_currency, state="readonly")
to_currency.set("Pick a currency")
to_currency.place(x=400, y=130)

# First button for the conversion and second for clear the content from the listbox
Button(convertor, command=lambda: convert(), text="Convert", height=9, width=10).place(x=50, y=200)
Button(convertor, command=lambda: clear(), text="Clear", height=4, width=5).place(x=480, y=200)

# Display result from conversion
Label(convertor, textvariable=display_result, width=20, height=6, padx=10, bg="white", font=100).place(x=180, y=200)

# Listbox for historic
listbox_h = Listbox(convertor, listvariable=display_history, bg="white", width=25, height=18)
listbox_h.place(x=537, y=200)

convertor.mainloop()
