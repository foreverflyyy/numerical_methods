import math as m

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

eps = 0.01
a, b = c, d = 0, 10


def f(x, y):
    return 2 * x * y


def simple_iteration_method(x, N, h):
    X = np.copy(x)
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            X[i][j] = 1 / 4 * (x[i][j - 1] + x[i][j + 1] + x[i - 1][j] + x[i + 1][j] + f(i * h, j * h) * (h ** 2))
    return X


def simple_diff(x, y):
    result = 0
    lenght = len(x)
    for i in range(lenght):
        for j in range(len(x[i])):
            result += (x[i][j] - y[i][j]) ** 2
        return m.sqrt(result)


def seidel_method(x, N, h):
    X = np.copy(x)
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            X[i][j] = 1 / 4 * (X[i][j - 1] + x[i][j + 1] + x[i - 1][j] + x[i + 1][j] + f(i * h, j * h) * (h ** 2))
    return X


def seidel_diff(x, y):
    result = 0
    lenght = len(x)
    for i in range(lenght):
        for j in range(len(x[i])):
            result = max(abs(x[i][j] - y[i][j]), result)
    return result


def draw(a, b, c, d, h, u, method):
    x = np.arange(a, b, h)
    t = np.arange(c, d, h)
    x, t = np.meshgrid(x, t)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(x, t, u, cmap=cm.summer)
    ax.set_title(method.title())
    plt.show()


def get_method(a, b, c, d, h, method):
    count_x = int((b - a) / h)
    count_t = int((d - c) / h)
    u = np.zeros((count_t, count_x))
    for i in range(count_t):
        u[i][0] = i * h + a
        u[i][count_x - 1] = i * h + b
    for i in range(count_x):
        u[0][i] = i * h + c
        u[count_t - 1][i] = i * h + d

    for j in range(1, count_x - 1):
        for i in range(1, count_t - 1):
            u[i][j] = 0
    prev = next = u
    while True:
        prev = next
        if method.title() == 'SeidelMethod':
            next = seidel_method(prev, count_x, h)
            if seidel_diff(prev, next) * h < eps:
                break
        else:
            next = simple_iteration_method(prev, count_x, h)
            if simple_diff(prev, next) * h < eps:
                break
    return next


data = [
    {"a": 0, "b": 10, "c": 0, "d": 10, "h": 1, "method": 'Зейдель, 10 * 10'},
    {"a": 0, "b": 5, "c": 0, "d": 5, "h": 1, "method": 'Зейдель, 5 * 5'},
    {"a": 0, "b": 10, "c": 0, "d": 10, "h": 1, "method": 'Простые итерации, 10 * 10'},
    {"a": 0, "b": 5, "c": 0, "d": 5, "h": 1, "method": 'Простые итерации, 5 * 5'}
]

for cell in data:
    a, b, c, d, h, method = cell["a"], cell["b"], cell["c"], cell["d"], cell["h"], cell["method"]
    u = get_method(a, b, c, d, h, method)
    draw(a, b, c, d, h, u, method)
