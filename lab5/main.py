import numpy as np

def Euler(f, interval, n):
    a = interval[0]
    b = interval[1]
    h = (b - a) / n
    X = np.linspace(a, b, n + 1)
    Y = [0]
    for i in range(0, n):
        Y.append(Y[i - 1] + h * f(X[i - 1] + h / 2, Y[i - 1] + h * f(X[i - 1], Y[i - 1]) / 2))

    return X, Y

def Runge_Kutt(f, interval, n):
    a = interval[0]
    b = interval[1]
    h = (b - a) / n
    X = np.linspace(a, b, n + 1)
    Y = [0]

    for i in range(0, n):
        k_0 = h * f(X[i], Y[i])
        k_1 = h * f(X[i] + h / 2, Y[i] + k_0 / 2)
        k_2 = h * f(X[i] + h / 2, Y[i] + k_1 / 2)
        k_3 = h * f(X[i] + h / 2, Y[i] + k_2 / 2)
        k_4 = h * f(X[i] + h, Y[i] + k_3)
        Y.append(Y[i] + (1 / 6 * (k_1 + 2 * k_2 + 2 * k_3 + k_4)))

    return X, Y

def Runge_Kutt_2(f, interval, n):
    a = interval[0]
    b = interval[1]
    h = (b - a) / n
    X = np.linspace(a, b, n + 1)
    Y = [0]
    Z = [1]

    for i in range(0, n):
        l_0 = h * f(X[i], Y[i])
        k_0 = h * Z[i]

        l_1 = h * f(X[i] + 1 / 2 * h, Y[i] + 1 / 2 * k_0)
        k_1 = h * (Z[i] + 1 / 2 * l_0)

        l_2 = h * f(X[i] + 1 / 2 * h, Y[i] + 1 / 2 * k_1)
        k_2 = h * (Z[i] + 1 / 2 * l_1)

        l_3 = h * f(X[i] + 1 / 2 * h, Y[i] + 1 / 2 * k_2)
        k_3 = h * (Z[i] + 1 / 2 * l_2)

        Y.append(Y[i] + (k_0 + 2 * k_1 + 2 * k_2 + k_3) / 6)
        Z.append(Z[i] + (l_0 + 2 * l_1 + 2 * l_1 + l_3) / 6)

    return X, Y, Z


def Adams_3(f, interval, n):
    a = interval[0]
    b = interval[1]
    h = (b - a) / n
    X = np.linspace(a, b, n + 1)
    X_t, Y, Z = Runge_Kutt_2(f, interval, n)
    for i in range(0, n + 1):
        Z.append(Z[i] + h * (23 * f(X[i], Y[i]) - 16 * f(X[i - 1], Y[i - 1]) + 5 * f(X[i - 2], Y[i - 2])) / 12)
        Y.append(Y[i] + h * (23 * Z[i] - 16 * Z[i - 1] + 5 * Z[i - 2]) / 12)
    return X, Y


def Adams_4(f, interval, n):
    a = interval[0]
    b = interval[1]
    h = (b - a) / n
    X = np.linspace(a, b, n + 1)
    X_t, Y, Z = Runge_Kutt_2(f, interval, n)
    for i in range(0, n + 1):
        Z.append(Z[i] + h * (55 * f(X[i], Y[i]) - 59 * f(X[i - 1], Y[i - 1]) + 37 * f(X[i - 2], Y[i - 2]) - 9 * f(X[i - 3], Y[i - 3])) / 24)
        Y.append(Y[i] + h * (55 * Z[i] - 59 * Z[i - 1] + 37 * Z[i - 2] - 9 * Z[i - 3]) / 24)
    return X, Y


# Данные
def f_1(x, y):
    return np.cos(x**2-y**2) + 0.2 * y


def f_2(x, y):
    return 1 - np.sin(0.75 * x + y**2)


def format_value(value):
    return format(value, '.8f')


def print_two_values(first, second):
    print(f"{format_value(first)}\t\t{format_value(second)}")


interval = [0, 0.5]
n = 5
m = n

# Первая задача
x, y = Euler(f_1, interval, n)
print("Euler: ")
for i in range(0, n + 1):
    print_two_values(x[i], y[i])
X, Y = Runge_Kutt(f_1, interval, n)
print("Runge_Kutt:")
for i in range(0, m + 1):
    print_two_values(X[i], Y[i])

# Вторая задача
X, Y = Adams_3(f_2, interval, n)
print("Adams_3: ")
for i in range(0, n + 1):
    print_two_values(X[i], Y[i])
x, y = Adams_4(f_2, interval, n)
print("Adams_4:")
for i in range(0, n + 1):
    print_two_values(x[i], y[i])