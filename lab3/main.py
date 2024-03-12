import math

import scipy.integrate as spi


def long_format(number):
    return "{:.15f}".format(number)


def f(x):
    return x * (x ** 2 - 1) ** 3 / 2


def f(x):
    return 2 * x * math.exp(x ** 2)


def F(x):
    return math.exp(x ** 2)

a = 0
b = 2
eps = 10**(-4)


def left_endpoint_rule():
    n, prev_sum = 5, 0
    while True:
        h = ((b - a) / n)
        sum = 0
        for i in range(n):
            sum += f(a + h * i)
        sum *= h
        if abs(sum - prev_sum) < eps:
            print(f'Последний шаг = {long_format(h)}, количество точек = {n}')
            return sum
        prev_sum = sum
        n *= 2


def right_endpoint_rule():
    n, prev_sum = 5, 0
    while True:
        h = ((b - a) / n)
        sum = 0
        for i in range(1, n + 1):
            sum += f(a + h * i)
        sum *= h
        if abs(sum - prev_sum) < eps:
            print(f'Последний шаг = {long_format(h)}, количество точек = {n}')
            return sum
        prev_sum = sum
        n *= 2


def middle_endpoint_rule():
    n, prev_sum = 5, 0
    while True:
        h = ((b - a) / n)
        sum = f(a + (h / 2))
        for i in range(1, n):
            sum += f(a + (h / 2) + (h * i))
        sum *= h
        if abs(sum - prev_sum) < eps:
            print(f'Последний шаг = {long_format(h)}, количество точек = {n}')
            return sum
        prev_sum = sum
        n *= 2


def trapezoidal_rule():
    n, prev_sum = 5, 0
    while True:
        h = ((b - a) / n)
        sub_sum = 0
        for i in range(n):
            sub_sum += f(a + h * i)
        sum = (h * (f(a) + f(b)) / 2) + h * sub_sum
        if abs(sum - prev_sum) < eps:
            print(f'Последний шаг = {long_format(h)}, количество точек = {n}')
            return sum
        prev_sum = sum
        n *= 2


def simpsons_rule():
    n, prev_sum = 5, 0
    while True:
        h = ((b - a) / n)
        sub_sum_even, sub_sum_odd = 0, 0
        if n != 2:
            for i in range(2, n, 2):
                sub_sum_even += f(a + h * i)
        for i in range(1, n + 1, 2):
            sub_sum_odd += f(a + h * i)
        sum = h * (f(a) + f(b) + 2 * sub_sum_even + 4 * sub_sum_odd) / 3
        if abs(sum - prev_sum) < eps:
            print(f'Последний шаг = {long_format(h)}, количество точек = {n}')
            return sum
        prev_sum = sum
        n *= 2


def error_rate(res, exact):
    return abs(1 - res / exact) * 100


result, er = spi.quad(f, a, b)

res_1 = left_endpoint_rule()
err_1 = error_rate(res_1, result)
print(f'Приближенное решение методом левых прямоугольников: {long_format(res_1)}')
print(f'Относительная погрешность: {long_format(err_1)}')
print()

res_2 = right_endpoint_rule()
err_2 = error_rate(res_2, result)
print(f'Приближенное решение методом правых прямоугольников: {long_format(res_2)}')
print(f'Относительная погрешность: {long_format(err_2)}')
print()

res_3 = middle_endpoint_rule()
err_3 = error_rate(res_3, result)
print(f'Приближенное решение методом средних прямоугольников: {long_format(res_3)}')
print(f'Относительная погрешность: {long_format(err_3)}')
print()

res_4 = trapezoidal_rule()
err_4 = error_rate(res_4, result)
print(f'Приближенное решение методом трапеций: {long_format(res_4)}')
print(f'Относительная погрешность: {long_format(err_4)}')
print()

res_5 = simpsons_rule()
err_5 = error_rate(res_5, result)
print(f'Приближенное решение методом Симпсона: {long_format(res_5)}')
print(f'Относительная погрешность: {long_format(err_5)}')