import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def init_rectangle(U, I, J, fx, ft, h, tau, a):
    i = np.arange(I + 1)
    x = h * i
    U[:, 0] = fx(x)
    j = np.arange(J + 1)
    t = tau * j
    startX = 0 if a > 0 else I
    U[startX, 1:] = ft(t[1:])
    return x, t, U


def init_half_plane(U, I, J, fx, ft, h, tau, a):
    i = np.arange(I + 1)
    x = h * (i - (J if a > 0 else 0))
    U[:, 0] = fx(x)
    j = np.arange(J + 1)
    t = tau * j
    return x, t, U


def init(I, J, h, tau, fx, ft, is_rect, a):
    if not is_rect:
        I = I + J
    U = np.zeros((I + 1, J + 1))
    if is_rect:
        return init_rectangle(U, I, J, fx, ft, h, tau, a)
    else:
        return init_half_plane(U, I, J, fx, ft, h, tau, a)


def bottom_right_corner(I, J, tau, U, fx, x, t, a, h):
    lmbd = a * tau / h
    for i in range(1, I):
        for j in range(0, J):
            U[i][j + 1] = lmbd * U[i - 1][j] + (1 - lmbd) * U[i][j] + tau * fx(x[i], t[j])
    return U


def bottom_left_corner(I, J, tau, U, fx, x, t, a, h):
    lmbd = a * tau / h
    for i in range(I - 2, -1, -1):
        for j in range(0, J):
            U[i][j + 1] = -lmbd * U[i + 1][j] + (1 + lmbd) * U[i][j] + tau * fx(x[i], t[j])
    return U


def upper_right_corner(I, J, tau, U, fx, x, t, a):
    if a > 0:
        for i in range(1, I + 1):
            for j in range(0, J):
                U[i][j + 1] = (U[i][j] + U[i - 1][j + 1] + tau * fx(x[i], t[j])) / 2
    else:
        for i in range(I - 1, -1, -1):
            for j in range(0, J):
                U[i][j + 1] = (U[i][j] + U[i + 1][j + 1] - tau * fx(x[i], t[j])) / 2
    return U


def rectangle(I, J, tau, U, fx, x, t, a, h):
    if a > 0:
        for i in range(1, I + 1):
            for j in range(0, J):
                U[i][j + 1] = U[i - 1][j] + tau * fx(x[i] + h / 2, t[j] + tau / 2)
    else:
        for i in range(I - 1, -1, -1):
            for j in range(0, J):
                U[i][j + 1] = U[i + 1][j] - tau * fx(x[i] + h / 2, t[j] + tau / 2)
    return U


# Функция отрисовки
def draw_graphic(x, t, U):
    x, t = np.meshgrid(x, t)
    x, t = x.T, t.T
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel("x")
    ax.set_ylabel("t")
    ax.set_zlabel("U")
    ax.plot_surface(x, t, U)
    ax.plot_surface(x, t, U, cmap=cm.summer)
    plt.show()
# dict_keys(['Blues', 'BrBG', 'BuGn', 'BuPu', 'CMRmap', 'GnBu', 'Greens', 'Greys', 'OrRd', 'Oranges', 'PRGn', 'PiYG', 'PuBu', 'PuBuGn', 'PuOr', 'PuRd', 'Purples', 'RdBu', 'RdGy', 'RdPu', 'RdYlBu', 'RdYlGn', 'Reds', 'Spectral', 'Wistia', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'binary', 'bone', 'brg', 'bwr', 'cool', 'coolwarm', 'copper', 'cubehelix', 'flag', 'gist_earth', 'gist_gray', 'gist_heat', 'gist_ncar', 'gist_rainbow', 'gist_stern', 'gist_yarg', 'gnuplot', 'gnuplot2', 'gray', 'hot', 'hsv', 'jet', 'nipy_spectral', 'ocean', 'pink', 'prism', 'rainbow', 'seismic', 'spring', 'summer', 'terrain', 'winter', 'Accent', 'Dark2', 'Paired', 'Pastel1', 'Pastel2', 'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c'])

# Начальные условия
Ux = lambda x: 5 * np.cos(2 * np.pi * x)
Ut0 = lambda t: 5 * np.cos(2 * np.pi * t)
Ut1 = lambda t: 5 * np.cos(2 * np.pi * t)
f = lambda x, t: 2 * x
f0 = lambda x, t: 0

tau = 0.05
h = 0.1
x_bounds = (0, 1)
t_bounds = (0, 10)
I = int((x_bounds[1] - x_bounds[0]) / h)
J = int((t_bounds[1] - t_bounds[0]) / tau)

# Вычисление и отрисовка
a = 2
is_rect = False
x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
U = bottom_right_corner(I + J + 1, J, tau, U, f0, x, t, a, h)
draw_graphic(x[x >= 0], t, U[-11:, :])

# a = -2
# is_rect = False
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = bottom_left_corner(I + J + 1, J, tau, U, f0, x, t, a, h)
# draw_graphic(x[x <= 1], t, U[:11, :])
#
# a = 2
# is_rect = True
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = bottom_right_corner(I + 1, J, tau, U, f0, x, t, a, h)
# draw_graphic(x, t, U)
#
# a = 2
# is_rect = True
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = upper_right_corner(I, J, tau, U, f0, x, t, a)
# draw_graphic(x, t, U)
#
# a = 2
# is_rect = True
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = rectangle(I, J, tau, U, f0, x, t, a, h)
# draw_graphic(x, t, U)
#
# a = -2
# is_rect = True
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = bottom_left_corner(I + 1, J, tau, U, f0, x, t, a, h)
# draw_graphic(x, t, U)
#
# a = -2
# is_rect = True
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = upper_right_corner(I, J, tau, U, f0, x, t, a)
# draw_graphic(x, t, U)
#
# a = -2
# is_rect = True
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = rectangle(I, J, tau, U, f0, x, t, a, h)
# draw_graphic(x, t, U)
#
# a = 2
# is_rect = False
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = bottom_right_corner(I + J + 1, J, tau, U, f, x, t, a, h)
# draw_graphic(x[x >= 0], t, U[-11:, :])
#
# a = -2
# is_rect = False
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = bottom_left_corner(I + J + 1, J, tau, U, f, x, t, a, h)
# draw_graphic(x[x <= 1], t, U[:11, :])
#
# a = 2
# is_rect = True
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = bottom_right_corner(I + 1, J, tau, U, f, x, t, a, h)
# draw_graphic(x, t, U)
#
# a = 2
# is_rect = True
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = upper_right_corner(I, J, tau, U, f, x, t, a)
# draw_graphic(x, t, U)
#
# a = 2
# is_rect = True
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = rectangle(I, J, tau, U, f, x, t, a, h)
# draw_graphic(x, t, U)
#
# a = -2
# is_rect = True
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = rectangle(I, J, tau, U, f, x, t, a, h)
# draw_graphic(x, t, U)
#
# a = -2
# is_rect = True
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = upper_right_corner(I, J, tau, U, f, x, t, a)
# draw_graphic(x, t, U)
#
# a = -2
# is_rect = True
# x, t, U = init(I, J, h, tau, Ux, Ut0, is_rect, a)
# U = bottom_left_corner(I + 1, J, tau, U, f, x, t, a, h)
# draw_graphic(x, t, U)
