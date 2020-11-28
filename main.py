import tkinter as tk
from tkinter import ttk

def set_values():
    txt1 = int(e1.get())
    txt2 = int(e2.get())
    txt3 = int(e3.get())
    print(convert(txt1, txt2, txt3))

def graphic():
    window = tk.Tk()
    window.title("Лабораторная работа №1")
    window.geometry('400x200')
    window.resizable(width=False, height=False)
    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Программа')
    tab_control.add(tab2, text='Авторы')
    window["bg"] = "lightgray"
    lbl1 = tk.Label(tab1, text="Введите число", )
    lbl1.grid(column=0, row=0)
    global e1
    e1 = tk.Entry(tab1, text="")
    e1.grid(column=1, row=0)
    txt1 = e1.get()
    lbl2 = tk.Label(tab1, text="В какую СС:")
    lbl2.grid(column=0, row=1)
    global e2
    e2 = tk.Entry(tab1, text="")
    e2.grid(column=1, row=1)
    lbl3 = tk.Label(tab1, text="Из какой СС:")
    lbl3.grid(column=0, row=2)
    global e3
    e3 = tk.Entry(tab1, text="")
    e3.grid(column=1, row=2)
    btn = tk.Button(tab1, text="OK", command=set_values)
    btn.grid(column=1, row=4)
    lblgroup = tk.Label(tab2,
                        text="Работу выполнили студенты группы 0307: \n Брывкин Даниил \n Верещагин Роман \n Обрезков "
                             "Егор")
    lblgroup.grid(column=0, row=8)
    tab_control.pack(expand=1, fill='both')
    print(txt1)
    window.mainloop()


def convert(num, to_base=10, from_base=10):
    # конвертация в десятичное число
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # конвертация в СС с основанием to_base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert(n // to_base, to_base) + alphabet[n % to_base]


def output():
    number = int(input("Число:"))
    to_ = int(input("Основание новой СС:"))
    from_ = int(input("Основание старой СС:"))
    print(convert(number, to_, from_))


graphic()


#output()
