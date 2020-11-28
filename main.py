import tkinter as tk
from tkinter import ttk

destroy = []


def set_values(window):
    global res
    txt1 = int(e1.get())
    txt2 = int(e2.get())
    txt3 = int(e3.get())
    res = convert(txt1, txt2, txt3)
    graphic(window)


def graphic(window):
    global res, destroy_objects
    for i in destroy_objects:
        i.destroy()
    destroy_objects = []
    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    destroy_objects.append(tab1)
    tab2 = ttk.Frame(tab_control)
    destroy_objects.append(tab2)
    tab_control.add(tab1, text='Программа')
    destroy_objects.append(tab_control)
    tab_control.add(tab2, text='Авторы')
    destroy_objects.append(tab_control)
    window["bg"] = "lightgray"
    lbl1 = tk.Label(tab1, text="Введите число", )
    destroy_objects.append(lbl1)
    lbl1.grid(column=0, row=0)
    global e1
    e1 = tk.Entry(tab1, text="")
    destroy_objects.append(e1)
    e1.grid(column=1, row=0)
    # txt1 = e1.get()
    lbl2 = tk.Label(tab1, text="В какую СС:")
    destroy_objects.append(lbl2)
    lbl2.grid(column=0, row=1)
    global e2
    e2 = tk.Entry(tab1, text="")
    destroy_objects.append(e2)
    e2.grid(column=1, row=1)
    lbl3 = tk.Label(tab1, text="Из какой СС:")
    destroy_objects.append(lbl3)
    lbl3.grid(column=0, row=2)
    global e3
    e3 = tk.Entry(tab1, text="")
    destroy_objects.append(e3)
    e3.grid(column=1, row=2)
    btn = tk.Button(tab1, text="OK", command=lambda: set_values(window))
    destroy_objects.append(btn)
    btn.grid(column=1, row=4)
    lbl4 = tk.Label(tab1, text="Результат:")
    destroy_objects.append(lbl4)
    lbl4.grid(column=0, row=3)
    lbl5 = tk.Label(tab1, text=res)
    destroy_objects.append(lbl5)
    lbl5.grid(column=1, row=3)
    lblgroup = tk.Label(tab2,
                        text="Работу выполнили студенты группы 0307: \n Брывкин Даниил \n Верещагин Роман \n Обрезков "
                             "Егор")
    lblgroup.grid(column=0, row=8)
    tab_control.pack(expand=1, fill='both')
    # print(txt1)
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


destroy_objects = []
res = ''
window = tk.Tk()
window.title("Лабораторная работа №1")
window.geometry('400x200')
window.resizable(width=False, height=False)
graphic(window)

# output()
