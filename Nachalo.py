import math
import sympy
import sympy as sym
from sympy import *

# T = input("Введите значение температуры воды: ")
# t = input("Введите значение температуры окружающей среды: ")

tau1 = 0
T = Symbol("T")
tau = Symbol("tau")
k = Symbol("k")
c = Symbol("c")

expr1 = 1 / (T - 20)  # Левая часть уравнения
expr2 = k  # Правая часть уравнения

print("Изначальное диф.уравнение:", expr1, "=", expr2)

int1 = integrate(expr1)  # Интеграл левой части
int2 = integrate(expr2, tau)  # Интеграл правой части

print(int1, "=", int2, "+ c")

print("После преобразований, получим:", T - 20, "=", "({}^{})".format(exp, k * tau), "*", c)

tau2 = int(input("Введите время охладждения воды: "))
temp1 = int(input("Введите начальное значение тепмпературы воды: "))
temp2 = int(input("Введите конченое занчение температуры воды: "))
temp_room = int(input("Введите значение темпертуры в комнате: "))

print(f"При {tau1} минут и температуре {temp1} градусов, получаем: ")
print(f"{temp1} - {temp_room} =", "{}^{}*{}".format(exp, k * tau1, c))
print(f"c = {temp1} - {temp_room} = ", temp1 - temp_room)
c = temp1 - temp_room

print(f"При {tau2} минут и температуре {temp2} градусов, получаем: ")
print(f"{temp2} - {temp_room} =", "{}*{}^({})".format(c, exp, k * tau2))
answer = temp2 - temp_room  # Вычисления
print("{}^{}".format(exp, k), "=", (answer / c) ** (1 / tau2))
exp_ = (answer / c) ** (1 / tau2)
print("Подставляем полученное значение в уравнение 2: ")
print(T - temp_room, "=", c, "*", exp_, "^", tau)

temp_final = int(input("Введите конченое значение тепературы для ответа на ворпрос задачи: "))
print(f"При температуре в {temp_final} градусов, имеем: ")
print(temp_final - temp_room, "=", c, "*", exp_, "^", tau)
answer1 = temp_final - temp_room
print(exp_, "^", tau, "=", answer1 / c)
left = tau * log((answer / c) ** (1 / tau2))
right = log(answer1 / c)
print(left, "=", right)

total = right // log((answer / c) ** (1 / tau2))
print("Приблизительный ответ на вопрос задачи: ", total, "-", total + 1, "минут.")



