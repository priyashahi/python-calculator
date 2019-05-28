import tkinter as tk
mainWindow = tk.Tk()
mainWindow.title("Calculator")


Label_1 = tk.Label(mainWindow, text="Enter First Number", pady=(10))
Label_1.pack()

first = tk.Entry(mainWindow)
first.pack()

Label_2 = tk.Label(mainWindow,text="Enter Second Number")
Label_2.pack()

second = tk.Entry(mainWindow)
second.pack()


def sum():
    var1 = int(first.get())
    var2 = int(second.get())
    addition = var1 +var2
    print(addition)
    result_label.config(text = "operations result is :" + str(addition))


button1 = tk.Button(mainWindow, text="+",
                   command=lambda: sum())
button1.pack()

def sub():
    var1 = int(first.get())
    var2 = int(second.get())
    subtraction = var1 -var2
    print(subtraction)
    result_label.config(text="operations result is :" + str(subtraction))


button2 = tk.Button(mainWindow, text="-",
                   command=lambda: sub())
button2.pack()

def division():
    var1 = int(first.get())
    var2 = int(second.get())
    division = var1/var2
    print(division)
    result_label.config(text="operations result is :" + str(division))


button3 = tk.Button(mainWindow, text="/",
                   command=lambda: division())
button3.pack()

def multiply():
    var1 = int(first.get())
    var2 = int(second.get())
    multiplication = var1 *var2
    print(multiplication)
    result_label.config(text="operations result is :" + str(multiplication))


button4 = tk.Button(mainWindow, text="*",
                   command=lambda: multiply())
button4.pack()

result_label = tk.Label(mainWindow, text="result")
result_label.pack()
mainWindow.mainloop()