import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def artificial_viscosity(a, b, c, d, u_0, I, J):
    h = (b - a) / I
    tau = (d - c) / J
    u = np.zeros((J, I + 1))

    for i in range(I):
        u[0][i] = u_0(a + i * h)
    for j in range(1, J):
        for i in range(I):
            u[j][i] = (u[j-1][i] - (tau / h) * (u[j-1][i] - u[j-1][i-1]) - ((tau * eps**2) / (2*h**3))
                       * (u[j-1][i+1] - u[j-2][i-1]) * (u[j-1][i+1]-u[j-1][i] + u[j-1][i-1]))
        for i in range(I):
            if abs(u[j][i] - u[j][i-1]) > 0.5:
                u[j][i] = (u[j][i-1] + u[j][i+1]) / 2
    return u[:, :-1]


def conservative(a, b, c, d, u_0, I, J):
    h = (b - a) / I
    tau = (d - c) / J
    u = np.zeros((J, I + 1))
    for i in range(I):
        u[0][i] = u_0(a + i * h)
    for j in range(J - 1):
        for i in range(I):
            u[j + 1][i] = u[j][i] - tau / (2*h) * (u[j][i] * u[j][i] - u[j][i-1] * u[j][i-1])
        for i in range(I):
            if abs(u[j][i] - u[j][i-1]) > 0.5:
                u[j][i] = (u[j][i-1] + u[j][i+1]) / 2
    return u[:, :-1]


def show_graph_by_params(graph, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.title(title)
    ax.set_xlabel("t")
    ax.set_ylabel("x")
    ax.set_zlabel("u")
    ax.set_rasterization_zorder(1)
    t, x = np.meshgrid(np.linspace(c, d, 2000), np.linspace(a, b, 10))
    x, t = x.T, t.T
    ax.plot_surface(x, t, graph, cmap=cm.summer)
    ax.view_init(elev=20, azim=20)


a, b = 0, 1
c, d = 0, 1
eps = 0.01
I, J = 10, 2000
u_0 = lambda x: 0 if x >= 0.5 else 1

res_artificial = artificial_viscosity(a, b, c, d, u_0, I, J)
show_graph_by_params(res_artificial, "Grid method")

res_conservative = conservative(a, b, c, d, u_0, I, J)
show_graph_by_params(res_conservative, "Conservative method")

plt.show()
