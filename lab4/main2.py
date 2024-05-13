import math


def f(x):
    return math.log10(x)


def df(x):
    return 1 / (math.log(10) * x)


def f2(x):
    return 3 ** (x / 2)


def df2(x):
    return (math.log(3) * 3 ** (x / 2)) / 2


def d2f2(x):
    return ((math.log(3) ** 2) * 3 ** (x / 2)) / 4


def leftD(x, dx, func):
    return (func(x) - func(x - dx)) / dx


def rightD(x, dx, func):
    return (func(x + dx) - func(x)) / dx


def centerD(x, dx, func):
    return (func(x + dx) - func(x - dx)) / (2 * dx)


def secondD(x, dx, func):
    return (func(x + dx) + func(x - dx) - 2 * func(x)) / (dx ** 2)


def task1_1(xk, yk, x):
    L = 0
    for i in range(4):
        p = 1
        for j in range(4):
            if j != i:
                p *= (x - xk[j])
                p /= (xk[i] - xk[j])
        L += yk[i] * p
    print('f(x): ', f(x))
    print('L(x): ', L)
    print('Error: ', abs(L - f(x)))
    print('Left derivative: ', leftD(x, 0.001, f), 'Error: ', abs(leftD(x, 0.001, f) - df(x)))
    print('Right derivative: ', rightD(x, 0.001, f), 'Error: ', abs(rightD(x, 0.001, f) - df(x)))
    print('Center derivative: ', centerD(x, 0.001, f), 'Error: ', abs(centerD(x, 0.001, f) - df(x)))
    print('Exact derivative: ', df(x))
    print()


def Aitken(xk, yk, x, a, b):
    if (b - a) <= 1:
        return (yk[a] * (xk[b] - x) - yk[b] * (xk[a] - x)) / (xk[b] - xk[a])
    else:
        return (Aitken(xk, yk, x, a, b - 1) * (xk[b] - x) - Aitken(xk, yk, x, a + 1, b) * (xk[a] - x)) / (xk[b] - xk[a])


def task1_2(xk, yk, x, a, b, func):
    L = Aitken(xk, yk, x, a, b)
    print('Aitken: ', L)
    print('Exact: ', func(x))
    print('Error: ', abs(L - func(x)))
    print()


def task2(xk, n, m):
    print('Xk = ', xk[0])
    print('Right derivative: ', rightD(xk[0], 0.001, f2), 'Error: ', abs(rightD(xk[0], 0.001, f2) - df2(xk[0])))
    print('Exact first derivative: ', df2(xk[0]), 'Exact second derivative: ', d2f2(xk[0]))
    print()

    for i in range(1, n - 1):
        print('Xk = ', xk[i])
        print('Left derivative: ', leftD(xk[i], 0.001, f2), 'Error: ', abs(leftD(xk[i], 0.001, f2) - df2(xk[i])))
        print('Right derivative: ', rightD(xk[i], 0.001, f2), 'Error: ', abs(rightD(xk[i], 0.001, f2) - df2(xk[i])))
        print('Center derivative: ', centerD(xk[i], 0.001, f2), 'Error: ', abs(centerD(xk[i], 0.001, f2) - df2(xk[i])))
        print('Second derivative: ', secondD(xk[i], 0.001, f2), 'Error: ', abs(secondD(xk[i], 0.001, f2) - d2f2(xk[i])))
        print('Exact first derivative: ', df2(xk[i]), 'Exact second derivative: ', d2f2(xk[i]))
        print()

    print('Xk = ', xk[n - 1])
    print('Left derivative: ', leftD(xk[i], 0.001, f2), 'Error: ', abs(leftD(xk[i], 0.001, f2) - df2(xk[i])))
    print('Exact first derivative: ', df2(xk[i]), 'Exact second derivative: ', d2f2(xk[i]))
    print()

    yk = [f2(x) for x in xk]
    task1_2(xk, yk, m, 0, n - 1, f2)


if __name__ == "__main__":
    print("Task 1_1")
    xk = [8.1, 8.5, 8.9, 9.3]
    yk = [0.908, 0.929, 0.949, 0.968]
    x = 8.4
    task1_1(xk, yk, x)

    print("Task 1_2")
    xk = [1.0, 1.08, 1.2, 1.27, 1.31, 1.38]
    yk = [f(x) for x in xk]
    x = 1.032
    task1_2(xk, yk, x, 0, 5, f)

    print("Task 2")
    xk = []
    a, b, m = 5.4, 6, 5.6
    n = 5
    for i in range(n):
        xk.append(a + i * (b - a) / (n - 1))
    xk.append(m)
    xk.sort()
    task2(xk, n + 1, m)
