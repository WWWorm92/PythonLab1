import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk

destroy = []


def set_values(window):
    global res, destroy_objects
    flag = 0
    while flag == 0:
        try:
            n = int(e1.get())
            res = alg(n)
            graphic(window)
        except ValueError:
            msg = "Неверное значение"
            mb.showwarning("Информация", msg)
            graphic(window)
            flag = 0
        except RuntimeError:
            msg = "Непредвиденная ошибка"
            mb.showerror("Информация", msg)
            graphic(window)
            flag = 0
        else:
            flag = 1
        break


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
    btn = tk.Button(tab1, text="OK", command=lambda: set_values(window))
    destroy_objects.append(btn)
    btn.grid(column=2, row=0, columnspan=1)
    lbl4 = tk.Label(tab1, text="Результат:")
    destroy_objects.append(lbl4)
    lbl4.grid(column=0, row=3)
    text = tk.Text(tab1, width=30, height=10, bg="gray95", bd=0, wrap=tk.WORD)
    text.insert("3.1", res)
    text.configure(state='disabled')
    text.grid(column=1, row=3, columnspan=9998)
    lbl5 = tk.Label(tab1, text="(Вомзможна прокрутка)")
    lbl5.grid(column=1, row=4)
    lblgroup = tk.Label(tab2,
                        text="Работу выполнили студенты группы 0307: \n Брывкин Даниил \n Верещагин Роман \n Обрезков "
                             "Егор")
    lblgroup.grid(column=0, row=8)
    tab_control.pack(expand=1, fill='both')
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


def periodconvert(perstr):
    P = 6
    perLen = len(perstr)
    chisl = int(convert(perstr, 10, 6))
    perstr = chisl / (P ** perLen - 1)
    return str(perstr)


def fibo(x):
    FIB = [1, 2]
    temp = 1
    while FIB[temp - 1] + FIB[temp] <= x:
        FIB.append(FIB[temp - 1] + FIB[temp])
        temp += 1
    resstr = ''
    for i in FIB[::-1]:
        if x >= i:
            x -= i
            resstr += '1'
        else:
            resstr += '0'
    return resstr


def alg(n):
    List = [12, 16, 20, 10, 12, 10]
    for i in range(len(List)):
        List[i] = convert(List[i], 6, 10)
    part1 = ''.join(List[:3])
    part2 = ''.join(List[3:])
    part1 = int(part1)
    part1 = fibo(part1)
    part2 = periodconvert(part2)
    part2 = int(part2[2:])
    part2 = fibo(part2)
    respart = part2 + part1
    outputstr = ''
    for i in range(n):
        outputstr += respart[i % len(respart)]
    return outputstr


# Код,формирующий графическое окно
destroy_objects = []
res = ''
window = tk.Tk()
window.title("Лабораторная работа №1")
window.geometry('450x250')
window.resizable(width=False, height=False)
graphic(window)
