import numpy as np

def f_xy(x, y):
    return np.cos(x**2-y**2) + 0.2 * y


def f_2(x, y):
    return 1 - np.sin(0.75 * x + y**2)


def format_value(value):
    return format(value, '.8f')


def print_two_values(first, second):
    print(f"{format_value(first)}\t\t{format_value(second)}")


def task_1_EC():
    a, b, n, eps, max = 0, 0.5, 2, 0.001, -1
    h = (a + b) / n
    current_iter = [[a, 0]]
    for i in range(1, n + 1):
        current_iter.append([a + i * h, current_iter[i - 1][1] + h * f_xy(a + i * h, current_iter[i - 1][1])])
        iter = 0
        while True:
            iter += 1
            max = -1
            h = (a + b) / n
            prev_iter = np.copy(current_iter)
            current_iter = [[a, 0]]
            for i in range(1, n +1):
                current_iter.append([a + i * h, current_iter[i - 1][1] + h / 2 *
                     (f_xy(a + (i - 1) * h, current_iter[i - 1][1])
                      + f_xy(a + i * h, current_iter[i - 1][1] + h * f_xy(a + (i - 1) * h, current_iter[i - 1][1])))])
            for i in range(1, len(prev_iter)):
                for j in range(1, len(current_iter)):
                    if (prev_iter[i][0] == current_iter[j][0]):
                        val = abs(prev_iter[i][1] - current_iter[j][1])
                        if (max < val):
                            max = val
                        break
            if max < eps and max >= 0:
                print('Euler Method', end = '\n\n')
                print('previous iteration')
                print('X\t\t\t\tY')
                print_two_values(prev_iter[0][0], prev_iter[0][1])
                for i in range(1, len(prev_iter) - 1):
                    print_two_values(prev_iter[i][0], prev_iter[i][1])
                print_two_values(prev_iter[len(prev_iter) - 1][0], prev_iter[len(prev_iter) - 1][1])
                print('last iteration')
                print('X\t\t\t\tY')
                print_two_values(current_iter[0][0], current_iter[0][1])
                for i in range(1, len(current_iter) - 1):
                    print_two_values(current_iter[i][0], current_iter[i][1])
                print_two_values(current_iter[len(current_iter) - 1][0], current_iter[len(current_iter) - 1][1])
                return
            n *= 2
            print(n)

task_1_EC()

def task_1_RK():
    a, b, n, eps, max = 0, 0.5, 2, 0.001, -1
    h = (a + b) / n
    current_iter = [[a, 0]]
    k1 = h * f_xy(a, current_iter[0][1])
    k2 = h * f_xy((a + b) / 2, current_iter[0][1] + k1 / 2)
    k3 = h * f_xy((a + b) / 2, current_iter[0][1] + k2 / 2)
    k4 = h * f_xy(b, current_iter[0][1] + k3)
    current_iter.append([b, current_iter[0][1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)])
    iter = 1
    while True:
        iter += 1
        max = -1
        h = (a + b) / n
        prev_iter = np.copy(current_iter)
        current_iter = [[a, 0]]
        for i in range(1, n + 1):
            k1 = h * f_xy(a + (i - 1) * h, current_iter[i - 1][1])
            k2 = h * f_xy(a + (i - 1) * h + h / 2, current_iter[i - 1][1] + k1 / 2)
            k3 = h * f_xy(a + (i - 1) * h + h / 2, current_iter[i - 1][1] + k2 / 2)
            k4 = h * f_xy(a + i * h, current_iter[i - 1][1] + k3)
        current_iter.append([a + i * h, current_iter[i - 1][1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)])
        for i in range(1, len(prev_iter)):
            for j in range(1, len(current_iter)):
                if prev_iter[i][0] == current_iter[j][0]:
                    val = abs(prev_iter[i][1] - current_iter[j][1])
                    if max < val:
                        max = val
                    break
        if max < eps and max >= 0:
            print('Runge-Kutta Method', end = '\n\n')
            print('previous iteration')
            print('X\t\t\tY')
            print_two_values(prev_iter[0][0], prev_iter[0][1])
            for i in range(1, len(prev_iter) - 1):
                print_two_values(prev_iter[i][0], prev_iter[i][1])
            print_two_values(prev_iter[len(prev_iter) - 1][0], prev_iter[len(prev_iter) - 1][1])
            print('last iteration')
            print('X\t\t\tY')
            print_two_values(current_iter[0][0], current_iter[0][1])
            for i in range(1, len(current_iter) - 1):
                print_two_values(current_iter[i][0], current_iter[i][1])
            print_two_values(current_iter[len(current_iter) - 1][0], current_iter[len(current_iter) - 1][1])
            return
        n *= 2
        print(n)

# task_1_RK()

def task_2_3():
    a, b, n, eps, max = 0, 0.5, 4, 0.001, -1
    iter = 0
    y = [[a, 0]]
    while True:
        max = -1
        iter += 1
        h = (a + b) / n
        prev_iter = np.copy(y)
        g = [[a, 0]]
        y = [[a, 0]]
        k1 = h * f_2(a, g[0][1])
        k2 = h * f_2(a + h / 2, g[0][1] + k1 / 2)
        k3 = h * f_2(a + h / 2, g[0][1] + k2 / 2)
        k4 = h * f_2(a + h, g[0][1] + k3)
        g.append([a + h, g[0][1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)])
        y.append([a + h, y[0][1] + h * g[1][1]])
        k1 = h * f_2(a + h, g[1][1])
        k2 = h * f_2(a + 3 * h / 2, g[1][1] + k1 / 2)
        k3 = h * f_2(a + 3 * h / 2, g[1][1] + k2 / 2)
        k4 = h * f_2(a + 2 * h, g[1][1] + k3)
        g.append([a + 2 * h, g[1][1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)])
        y.append([a + 2 * h, y[1][1] + h * g[2][1]])
        for i in range(2, n):
            g.append([a + (i + 1) * h, g[i][1] + h / 12 * (
                        23 * f_2(a + i * h, y[i][1]) - 16 * f_2(a + (i - 1) * h, y[i - 1][1]) + 5 * f_2(a + (i - 2) * h,
                                                                                                        y[i - 2][1]))])
            y.append([a + (i + 1) * h, y[i][1] + h / 12 * (23 * g[i][1] - 16 * g[i - 1][1] + 5 * g[i - 2][1])])
        n *= 2
        print(n)
        for i in range(1, len(prev_iter)):
            for j in range(1, len(y)):
                if (prev_iter[i][0] == y[j][0]):
                    val = abs(prev_iter[i][1] - y[j][1])
                    if (max < val):
                        max = val
                    break
        if max < eps and max >= 0:
            print()
            print()
            print('Adam\'s Method(3rd order)', end='\n\n')
            print('last iteration')
            print('X\t\t\tY')
            print_two_values(y[0][0], y[0][1])
            for i in range(1, len(y) - 1):
                print_two_values(y[i][0], y[i][1])
            print_two_values(y[len(y) - 1][0], y[len(y) - 1][1])
            print(f"LENGTH {len(y) - 1}")
            return


def task_2_4():
    a, b, n, eps, max = 0, 0.5, 4, 0.001, -1
    iter = 0
    y = [[a, 0]]
    while True:
        max = -1
        iter += 1
        h = (a + b) / n
        prev_iter = np.copy(y)
        g = [[a, 0]]
        y = [[a, 0]]
        k1 = h * f_2(a, g[0][1])
        k2 = h * f_2(a + h / 2, g[0][1] + k1 / 2)
        k3 = h * f_2(a + h / 2, g[0][1] + k2 / 2)
        k4 = h * f_2(a + h, g[0][1] + k3)
        g.append([a + h, g[0][1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)])
        y.append([a + h, y[0][1] + h * g[1][1]])
        k1 = h * f_2(a + h, g[1][1])
        k2 = h * f_2(a + 3 * h / 2, g[1][1] + k1 / 2)
        k3 = h * f_2(a + 3 * h / 2, g[1][1] + k2 / 2)
        k4 = h * f_2(a + 2 * h, g[1][1] + k3)
        g.append([a + 2 * h, g[1][1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)])
        y.append([a + 2 * h, y[1][1] + h * g[2][1]])
        k1 = h * f_2(a + 2 * h, g[2][1])
        k2 = h * f_2(a + 5 * h / 2, g[2][1] + k1 / 2)
        k3 = h * f_2(a + 5 * h / 2, g[2][1] + k2 / 2)
        k4 = h * f_2(a + 3 * h, g[2][1] + k3)
        g.append([a + 3 * h, g[2][1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)])
        y.append([a + 3 * h, y[2][1] + h * g[3][1]])
        for i in range(3, n):
            g.append([a + (i + 1) * h, g[i][1] + h / 24 * (
                        55 * f_2(a + i * h, y[i][1]) - 59 * f_2(a + (i - 1) * h, y[i - 1][1]) + 37 * f_2(
                    a + (i - 2) * h, y[i - 2][1]) - 9 * f_2(a + (i - 3) * h, y[i - 3][1]))])
            y.append([a + (i + 1) * h,
                      y[i][1] + h / 24 * (55 * g[i][1] - 59 * g[i - 1][1] + 37 * g[i - 2][1] - 9 * g[i - 3][1])])
        n *= 2
        for i in range(1, len(prev_iter)):
            for j in range(1, len(y)):
                if prev_iter[i][0] == y[j][0]:
                    val = abs(prev_iter[i][1] - y[j][1])
                    if max < val:
                        max = val
                    break
        if max < eps and max >= 0:
            print()
            print()
            print('Adam\'s Method(4th order)')
            print('last iteration')
            print('X\t\t\tY')
            print_two_values(y[0][0], y[0][1])
            for i in range(0, len(y) - 1):
                print_two_values(y[i][0], y[i][1])
            print_two_values(y[len(y) - 1][0], y[len(y) - 1][1])
            print(f"LENGTH {len(y) - 1}")
            return


task_2_3()
task_2_4()
