import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt


class Solver:

    def __init__(self, a, b, c, d, eps, h, tau, U0_x, der_U_t, Ut_0, Ut_1):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.eps = eps
        self.h = h
        self.tau = tau
        self.x_count = int((b - a) / h)
        self.t_count = int((d - c) / tau)
        self.l_ambda = (D * tau / h)
        self.A = self.l_ambda
        self.B = 2 * self.l_ambda + 1
        self.U0_x = U0_x
        self.der_U_t = der_U_t
        self.Ut_0 = Ut_0
        self.Ut_1 = Ut_1

    def explicit(self):
        u = np.zeros((self.t_count, self.x_count))
        for i in range(self.x_count):
            u[0][i] = self.U0_x(0, i * h)
            u[1][i] = u[0][i] + (-1) * tau
        for i in range(self.t_count):
            u[i][0] = self.Ut_0(i * tau, 0)
            u[i][self.x_count - 1] = self.Ut_1(i * tau, 1)
        for j in range(1, self.t_count - 1):
            for i in range(1, self.x_count - 1):
                u[j + 1][i] = 2 * (1 - self.l_ambda) * u[j][i] + self.l_ambda * (u[j][i + 1] + u[j][i - 1] - u[j - 1][i])
        return u

    def not_explicit_1(self):
        u = np.zeros((self.t_count, self.x_count))
        for i in range(self.x_count):
            u[0][i] = self.U0_x(0, i * h)
            u[1][i] = u[0][i] + (-1) * tau
        for i in range(self.t_count):
            u[i][0] = self.Ut_0(i * tau, 0)
            u[i][self.x_count - 1] = self.Ut_1(i * tau, 1)
        a, b, c = np.zeros(self.x_count), np.zeros(self.x_count), np.zeros(self.x_count)
        for j in range(1, self.t_count - 1):
            a[self.x_count - 1] = 0
            b[self.x_count - 1] = u[j + 1][self.x_count - 1]
            c[self.x_count - 1] = 1 / (self.B - self.A * a[self.x_count - 1])
            for i in range(self.x_count - 1, 0, -1):
                a[i - 1] = c[i] * self.A
                b[i - 1] = c[i] * (self.A * b[i] - (u[j - 1][i] - 2 * u[j][i]))
                c[i - 1] = 1 / (self.B - self.A * a[i - 1])
            for i in range(1, self.x_count - 1):
                u[j + 1][i + 1] = a[i] * u[j + 1][i] + b[i]
        return u

    def not_explicit_2(self):
        u = np.zeros((self.t_count, self.x_count))
        for i in range(self.x_count):
            u[0][i] = self.U0_x(0, i * h)
            u[1][i] = u[0][i] + (-1) * tau
        for i in range(self.t_count):
            u[i][0] = self.Ut_0(i * tau, 0)
            u[i][self.x_count - 1] = self.Ut_1(i * tau, 1)
        a, b, c = np.zeros(self.x_count), np.zeros(self.x_count), np.zeros(self.x_count)
        for j in range(1, self.t_count - 1):
            a[self.x_count - 1] = 0
            b[self.x_count - 1] = u[j + 1][self.x_count - 1]
            c[self.x_count - 1] = 1 / (self.B - self.A * a[self.x_count - 1])
            for i in range(self.x_count - 1, 0, -1):
                a[i - 1] = c[i] * self.A
                b[i - 1] = c[i] * (self.A * b[i] - (u[j - 1][i] - 2 * u[j][i]))
                c[i - 1] = 1 / (self.B - self.A * a[i - 1])
            for i in range(1, self.x_count - 1):
                u[j + 1][i + 1] = a[i] * u[j + 1][i] + b[i]
        return u

    def draw(self, u, method):
        x = np.arange(a, b, h)
        t = np.arange(c, d, tau)
        x, t = np.meshgrid(x, t)
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.set_title(method.title())
        ax.plot_surface(x, t, u, cmap=cm.summer, antialiased=False)
        plt.show()


D = 1
a, b = [0, 1]
c, d = [0, 10]
eps, h, tau = 0.01, 0.01, 0.01
U0_x = lambda t, x: x
der_U_t = lambda x: 2
Ut_0 = lambda t, x: 0
Ut_1 = lambda t, x: 1

solver = Solver(a, b, c, d, eps, h, tau, U0_x, der_U_t, Ut_0, Ut_1)
ul = solver.explicit()
u2 = solver.not_explicit_1()
u3 = solver.not_explicit_2()

solver.draw(ul, "Явный метод")
solver.draw(u2, "Неявный метод 1")
solver.draw(u3, "Неявный метод 2")
