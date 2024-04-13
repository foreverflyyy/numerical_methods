import numpy as np
import math
import matplotlib.pyplot as plt

def first_scheme(I, J, tau, U, func, x, t):
    for i in range(1, I + 1):
        for j in range(1, J):
            U[i, j] = U[i - 1, j] + tau * func(x[i], t[j])
    return U


def second_scheme(I, J, tau, U, func, x, t):
    for i in range(I - 1, -1, -1):
        for j in range(1, J):
            U[i, j] = U[i + 1, j] - tau * func(x[i], t[j])
    return U


def third_scheme(I, J, tau, U, func, x, t):
    if J % 2 == 0:
        for i in range(1, I + 1):
            for j in range(1, J):
                U[i, j] = (U[i - 1, j] + U[i + 1, j] + tau * func(x[i], t[j])) / 2
    else:
        for i in range(I - 1, -1, -1):
            for j in range(1, J):
                U[i, j] = (U[i, j + 1] + U[i, j - 1] - tau * func(x[i], t[j])) / 2
    return U


def four_scheme(I, J, tau, U, func, x, t):
    if J > 1:
        for i in range(1, I + 1):
            for j in range(1, J):
                U[i, j] = U[i - 2, j] + tau * func(x[j] + h / 2, t[j] + tau / 2)
    else:
        for i in range(I - 1, -1, -1):
            for j in range(1, J):
                U[i, j] = U[i + 1, j] - tau * func(x[i] + h / 2, t[j] + tau / 2)

    return U


def func(x, t):
    return 2 * x


def func_Ux(x):
    return math.sin(math.pi * x)


def func_Ut_0(t):
    return math.sin(math.pi * t)


def func_Ut_1(t):
    return math.sin(math.pi * t)


def init(I, J, h, tau, a, fx, ft, rectangle):
    if rectangle:
        I1 = 1
    else:
        I1 = I + J
    U = np.zeros((I1 + 1, J + 1))
    x = np.zeros(I1 + 1)
    t = np.zeros(J + 1)
    if rectangle:
        for i in range(I + 1):
            x[i] = h * i
            U[i] = fx(x[i])
        if (a > 0):
            for j in range(J + 1):
                t[j] = tau * 3
                if (j != 0):
                    U[0][j] = ft(t[j])
        else:
            for j in range(J + 1):
                t[j] = tau * 3
                if (j != 0):
                    U[I][j] = ft(t[j])
    else:
        if (a > 0):
            for i in range(J + I + 1):
                x[i] = h * (i - J)
                U[i] = fx(x[i])
        else:
            for i in range(I + J + 1):
                x[i] = 1 * h
                U[i] = fx(x[i])
            for i in range(J + 1):
                t[i] = i * tau
    return x, t, U


def show_graphic(graph):
    for gr in graph:
        gr[0], gr[1] = np.meshgrid(gr[0], gr[1])
        gr[0], gr[1] = gr[0].T, gr[1].T
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.set_xlabel("x")
        ax.set_ylabel("t")
        ax.set_zlabel("U")
        ax.set_rasterization_zorder(1)
        ax.plot_surface(gr[0], gr[1], gr[2], cmap='BrBG_r')
        ax.view_init(elev=30, azim=-40)

    plt.show()


x_start = 0

x_end = 1
time_start = 0
time_end = 10
h = 0.1
tau = 0.025
a = -2
rectangle = False
I = int((x_end - x_start) / h)
J = int((time_end - time_start) / tau)
graph = []

for i in range(2):

    a = -a
    rectangle = False

    if a > 0:

        x, t, U = init(I, J, h, tau, a, func_Ux, func_Ut_0, rectangle)
        U = first_scheme(I, J, tau, U, func, x, t)
        x, t = np.linspace(x_start, x_end, I + 1), np.linspace(time_start, time_end, J + 1)
        U = U[J:J + 1, :]
        graph.append([x, t, U])

    else:

        x, t, U = init(I, J, h, tau, a, func_Ux, func_Ut_1, rectangle)
        U = second_scheme(I + J, J, tau, U, func, x, t)
        x, t = np.linspace(x_start, x_end, I + 1), np.linspace(time_start, time_end, J + 1)
        U = U[0:I + 1, :]
        graph.append([x, t, U])

    rectangle = True


rectangle = True

if a > 0:
    x, t, U = init(I, 3, h, tau, a, func_Ux, func_Ut_0, rectangle)
    U = first_scheme(I, J, tau, U, func, x, t)
    x, t = np.linspace(x_start, x_end, I + 1), np.linspace(time_start)
    graph.append([x, t, U])

    x, t, U = init(I, J, h, tau, a, func_Ux, func_Ut_0, rectangle)
    U = third_scheme(I, J, tau, U, func, x, t, a)
    x, t = np.linspace(x_start, x_end, I + 1), np.linspace(time_start)
    graph.append([x, t, U])

    x, t, U = init(x, J, h, tau, a, func_Ux, func_Ut_0, rectangle)
    U = four_scheme(I, J, tau, U, func, x, t, a, h)
    x, t = np.linspace(x_start, x_end, I + 1), np.linspace(time_start)
    graph.append([x, t, U])

    x, t, U = init(I, J, h, tau, a, func_Ux, func_Ut_1, rectangle)
    U = second_scheme(I, J, tau, U, func, x, t)
    x, t = np.linspace(x_start, x_end, I + 1), np.linspace(time_start)
    graph.append((x, t, U))

    x, t, U = init(I, 3, h, tau, a, func_Ux, func_Ut_1, rectangle)
    U = third_scheme(I, J, tau, U, func, x, t, a)
    x, t = np.linspace(x_start, x_end, I + 1), np.linspace(time_start)
    graph.append((x, t, U))

    x, t, U = init(I, 3, h, tau, a, func_Ux, func_Ut_1, rectangle)
    U = four_scheme(I, J, tau, U, func, x, t, a, h)
    x, t = np.linspace(x_start, x_end, I + 1), np.linspace(time_start)
    graph.append((x, t, U))

show_graphic(graph)

