import math
import sympy
import sympy as sym
from sympy import *
from tkinter import *
from tkinter import scrolledtext, ttk


def main1():
    tau1 = 0
    T = Symbol("T")
    tau = Symbol("tau")
    k = Symbol("k")
    c = Symbol("c")
    expr1 = 1 / (T - 20)  # Левая часть уравнения
    expr2 = k  # Правая часть уравнения

    tau2 = int(txt1.get())
    temp1 = int(txt2.get())
    temp2 = int(txt3.get())
    temp_room = int(txt4.get())

    # print("Изначальное диф.уравнение:", expr1, "=", expr2)

    int1 = integrate(expr1)  # Интеграл левой части
    int2 = integrate(expr2, tau)  # Интеграл правой части

    # print(int1, "=", int2, "+ c")

    # print("После преобразований, получим:", T - 20, "=", "({}^{})".format(exp, k * tau), "*", c)

    # tau2 = int(input("Введите время охладждения воды: "))
    # temp1 = int(input("Введите начальное значение тепмпературы воды: "))
    # temp2 = int(input("Введите конченое занчение температуры воды: "))
    # temp_room = int(input("Введите значение темпертуры в комнате: "))

    # print(f"При {tau1} минут и температуре {temp1} градусов, получаем: ")
    # print(f"{temp1} - {temp_room} =", "{}^{}*{}".format(exp, k * tau1, c))
    # print(f"c = {temp1} - {temp_room} = ", temp1 - temp_room)
    c = temp1 - temp_room

    # print(f"При {tau2} минут и температуре {temp2} градусов, получаем: ")
    # print(f"{temp2} - {temp_room} =", "{}*{}^({})".format(c, exp, k * tau2))
    answer = temp2 - temp_room  # Вычисления
    # print("{}^{}".format(exp, k), "=", (answer / c) ** (1 / tau2))
    exp_ = (answer / c) ** (1 / tau2)
    # print("Подставляем полученное значение в уравнение 2: ")
    # print(T - temp_room, "=", c, "*", exp_, "^", tau)

    # temp_final = int(input("Введите конченое значение тепературы для ответа на ворпрос задачи: "))
    temp_final = int(txt6.get())
    # print(f"При температуре в {temp_final} градусов, имеем: ")
    # print(temp_final - temp_room, "=", c, "*", exp_, "^", tau)
    answer1 = temp_final - temp_room
    # print(exp_, "^", tau, "=", answer1 / c)
    left = tau * log((answer / c) ** (1 / tau2))
    right = log(answer1 / c)
    # print(left, "=", right)

    total = right // log((answer / c) ** (1 / tau2))
    # print("Приблизительный ответ на вопрос задачи: ", total, "-", total + 1, "минут.")
    console.insert(1.0, "+-1")
    console.insert(1.0, total, total + 1)


def delete():
    console.delete(1.0, END)


window = Tk()
window.title("Решение задачи")
window.geometry('500x300')
window.resizable(width=False, height=False)
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2.5
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 3.5
window.wm_geometry("+%d+%d" % (x, y))
lbl = Label(window, text="Начальные условия:", font=("Arial Bold", 20))
lbl.grid(column=1, row=0)
lbl1 = Label(window, text="Время охлаждения воды")
lbl1.grid(column=1, row=1)
txt1 = Entry(window, width=20)
txt1.grid(column=2, row=1)

lbl2 = Label(window, text="Начальное значение температуры воды")
lbl2.grid(column=1, row=2)
txt2 = Entry(window, width=20)
txt2.grid(column=2, row=2)

lbl3 = Label(window, text="Конечное значение температуры воды")
lbl3.grid(column=1, row=3)
txt3 = Entry(window, width=20)
txt3.grid(column=2, row=3)

lbl4 = Label(window, text="Введите значение температуры в комнате")
lbl4.grid(column=1, row=4)
txt4 = Entry(window, width=20)
txt4.grid(column=2, row=4)

lbl5 = Label(window, text="Данные для вопроса:", font=("Arial Bold", 20))
lbl5.grid(column=1, row=5)

lbl6 = Label(window, text="Введите значение температуры:")
lbl6.grid(column=1, row=6)
txt6 = Entry(window, width=20)
txt6.grid(column=2, row=6)

btn8 = Button(window, text="Вывести результаты!", command=main1)
btn8.grid(column=2, row=9)

lbl6 = Label(window, text="ПЕРЕД ПОВТОРНЫМ ЗАПУСКОМ, ОЧИСТИТЬ ПОЛЕ ВЫВОДА!", bg="red")
lbl6.grid(column=1, row=11)

btn9 = Button(window, text="Очистить поле вывода!", command=delete)
btn9.grid(column=2, row=12)

console = Text(width=5, height=1)
console.grid(column=2, row=10)

window.mainloop()
