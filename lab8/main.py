import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

np.set_printoptions(linewidth=100, precision=3, suppress=True, floatmode='fixed')

h = 0.1
a, b = 0, 1
c, d, tau = 0, 10, 0.01
I, J = int((b - a) / h), int((d - c) / tau)


def conditions():
    u = np.zeros((J, I))
    for i in range(I):
        u[0][i] = 1 - i * h
        u[1][i] = u[0][i] + (-1) * tau
    for j in range(J):
        u[j][0] = 1
        u[j][I - 1] = 0
    return u


def init(lamb):
    return np.zeros(I), np.zeros(I), np.zeros(I), lamb, (2 * lamb + 1), lamb


def method_1():
    u = conditions()
    lamb = (tau ** 2) / (h ** 2)
    for j in range(1, J - 1):
        for i in range(1, I - 1):
            calc = 2 * (1 - lamb) * u[j][i] + lamb * (u[j][i + 1] + u[j][i - 1]) - u[j - 1][i]
            u[j + 1][i] = calc
    return u, "Схема 1: явный метод"


def method_2():
    u = conditions()
    lamb = tau ** 2 / (2 * h ** 2)
    alpha, beta, gamma, A, B, C = init(lamb)
    for j in range(1, J - 1):
        alpha[I - 1] = 0
        beta[I - 1] = u[j + 1][I - 1]
        gamma[I - 1] = 1 / (B - C * alpha[I - 1])
        for i in range(I - 1, 0, -1):
            alpha[i - 1] = gamma[i] * A
            beta[i - 1] = gamma[i] * (C * beta[i] - (u[j - 1][i] - 2 * u[j][i]))
            gamma[i - 1] = 1 / (B - C * alpha[i - 1])
        for i in range(I - 1):
            u[j + 1][i + 1] = alpha[i] * u[j + 1][i] + beta[i]
    return u, "Cxema 2: неявный метод"


def method3():
    u = conditions()
    lamb = (tau ** 2) / (2 * h ** 2)
    a, b, c = np.zeros(I), np.zeros(I), np.zeros(I)

    for j in range(1, J - 1):
        a[I - 1] = 0
        b[I - 1] = u[j + 1][I - 1]
        c[I - 1] = 1 / (1 + 2 * lamb - lamb * a[I - 1])

        for i in range(I - 2, 0, -1):
            a[i - 1] = c[i] * lamb
            b[i - 1] = c[i] * (lamb * b[i] - (u[j - 1][i] - 2 * u[j][i]))
            c[i - 1] = 1 / (1 + 2 * lamb - lamb * a[i - 1])

        for i in range(1, I - 1):
            u[j + 1][i + 1] = a[i] * u[j + 1][i] + b[i]
    return u, "Схема 3: Неявный метод"


for (graph, title) in [method_1(), method_2(), method3()]:
    print(title, "U =", graph)
    X, T = np.meshgrid(np.arange(a, b, h), np.arange(c, d, tau))
    fig = plt.figure(title)
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, T, graph, cmap=cm.summer, linewidth=0, antialiased=False)

plt.show()
