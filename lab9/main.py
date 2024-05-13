import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

a, b, h = 0, 1, 0.1
c, d, tau = 0, 10, 0.005
I, J = int((b - a) / h), int((d - c) / tau)
lambd = tau / (h ** 2)


def U_0x(x):
    return 1 + x - x * (1 - x)


def U_t0(t):
    return 1


def U_t1(t):
    return 2


def conditions():
    u = np.zeros((J, I))
    for i in range(I):
        u[0][i] = U_0x(i * h)
    for i in range(J):
        u[i][0] = U_t0(i * tau)
        u[i][I - 1] = U_t1(i * tau)
    return u


def explicit_scheme():
    u = conditions()
    for j in range(J - 1):
        for i in range(1, I - 1):
            u[j + 1][i] = lambd * u[j][i + 1] + (1 - 2 * lambd) * u[j][i] + lambd * u[j][i - 1]
    return u


def not_explicit_scheme():
    u = conditions()
    alpha, beta, gamma, A, B, C = np.zeros(I), np.zeros(I), np.zeros(I), lambd, 2 * lambd + 1, lambd
    for j in range(J - 1):
        alpha[I - 1] = 0
        beta[I - 1] = u[j + 1][I - 1]
        gamma[I - 1] = 1 / (B - C * alpha[I - 1])
        for i in range(I - 1, 0, -1):
            alpha[i - 1] = gamma[i] * A
            beta[i - 1] = gamma[i] * (C * beta[i] + u[j][i])
            gamma[i - 1] = 1 / (B - C * alpha[i - 1])
        for i in range(I - 1):
            u[j + 1][i + 1] = alpha[i] * u[j + 1][i] + beta[i]
    return u


data = [(explicit_scheme(), 'Явная схема'), (not_explicit_scheme(), 'Неявная схема')]
for (graph, title) in data:
    x, t = np.meshgrid(np.arange(a, b, h), np.arange(c, d, tau))
    fig = plt.figure(title)
    ax = fig.add_subplot(projection='3d')
    ax.view_init(30, -120)
    ax.plot_surface(x, t, graph, cmap=cm.summer, antialiased=False)

plt.show()
