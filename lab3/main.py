import math
from scipy import integrate


def long_format(number):
    return "{:.15f}".format(number)


def short_format(number):
    return "{:.6f}".format(number)


def f(x):
    return 2 * x * math.exp(x ** 2)


a = 0
b = 2
n = 2
eps = 10**(-4)


def left_rectangle(n):
    prev_sum = 0
    while True:
        h = ((b - a) / n)
        sum = 0
        for i in range(n):
            sum += f(a + h * i)
        sum *= h
        if abs(sum - prev_sum) < eps:
            print(f"Последний: {short_format(h)}, точек разбиения = {n}")
            return sum
        prev_sum = sum
        n *= 2


def right_rectangle(n):
    prev_sum = 1
    while True:
        h = ((b - a) / n)
        sum = 0
        for i in range(n):
            sum += f(a + h * i)
        sum *= h
        if abs(sum - prev_sum) < eps:
            print(f"Последний: {short_format(h)}, точек разбиения = {n}")
            return sum
        prev_sum = sum
        n *= 2


def middle_rectangle(n):
    prev_sum = 0
    while True:
        h = ((b - a) / n)
        sum = f(a + (h / 2))
        for i in range(1, n + 1):
            sum += f(a + (h / 2) + (h * i))
        sum *= h
        if abs(sum - prev_sum) < eps:
            print(f"Последний: {short_format(h)}, точек разбиения = {n}")
            return sum
        prev_sum = sum
        n *= 2


def trapezoid_method(n):
    prev_sum = 0
    while True:
        h = ((b - a) / n)
        sub_sum = 0
        for i in range(1, n + 1):
            sub_sum += f(a + h * i)
        sum = (h * (f(a) + f(b)) / 2) + h * sub_sum
        if abs(sum - prev_sum) < eps:
            print(f"Последний: {short_format(h)}, точек разбиения = {n}")
            return sum
        prev_sum = sum
        n *= 2


def simpson_method(n):
    prev_sum = 0
    while True:
        h = ((b - a) / n)
        sub_sum_even, sub_sum_odd = 0, 0
        if n != 2:
            for i in range(2, n, 2):
                sub_sum_even += f(a + h * i)
        for i in range(1, n + 1, 2):
            sub_sum_odd += f(a + h * i)
        sum = (h * (f(a) + f(b) + 2 * sub_sum_even + 4 * sub_sum_odd) / 3)
        if abs(sum - prev_sum) < eps:
            print(f"Последний шаг = {short_format(h)}, кол-во точек разбиения = {n}")
            return sum
        prev_sum = sum
        n *= 2


result, error = integrate.quad(f, a, b)
print(f"Точное решение: {result}")
print()

res_1 = left_rectangle(n)
error_rate_1 = (abs(result - res_1) / result) * 100
print(f"Приближенное решение метода левых прямоугольников: {res_1}")
print(f"Относительная погрешность: {short_format(error_rate_1)}")
print()

res_2 = right_rectangle(n)
error_rate_2 = (abs(result - res_2) / result) * 100
print(f"Приближенное решение метода правых прямоугольников: {res_2}")
print(f"Относительная погрешность: {short_format(error_rate_2)}")
print()

res_3 = middle_rectangle(n)
error_rate_3 = (abs(result - res_3) / result) * 100
print(f"Приближенное решение метода средних прямоугольников: {res_3}")
print(f"Относительная погрешность: {short_format(error_rate_3)}")
print()

res_4 = trapezoid_method(n)
error_rate_4 = (abs(result - res_4) / result) * 100
print(f"Приближенное решение метода трапеций: {res_4}")
print(f"Относительная погрешность: {short_format(error_rate_4)}")
print()

res_5 = simpson_method(n)
error_rate_5 = (abs(result - res_5) / result) * 100
print(f"Приближенное решение метода Симсона: {res_5}")
print(f"Относительная погрешность: {short_format(error_rate_5)}")
print()
