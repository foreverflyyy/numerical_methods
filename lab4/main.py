import math


def sin_function(x):
    return math.sin(x)


def sin_half_arg_function(x):
    return math.sin(x / 2)


def function_derivative(x):
    return math.cos(x / 2) / 2


def function_second_derivative(x):
    return (-math.sin(x / 2)) / 4


def left_derivative(x, dx, func):
    return (func(x) - func(x - dx)) / dx


def right_derivative(x, dx, func):
    return (func(x + dx) - func(x)) / dx


def center_derivative(x, dx, func):
    return (func(x + dx) - func(x - dx)) / (2 * dx)


def second_derivative(x, dx, func):
    return (func(x + dx) + func(x - dx) - 2 * func(x)) / (dx ** 2)


def aitken_interpolation(xk, yk, x, a, b):
    if (b - a) <= 1:
        return (yk[a] * (xk[b] - x) - yk[b] * (xk[a] - x)) / (xk[b] - xk[a])
    else:
        return (aitken_interpolation(xk, yk, x, a, b - 1) * (xk[b] - x) - aitken_interpolation(xk, yk, x, a + 1, b) * (
                    xk[a] - x)) / (xk[b] - xk[a])


def solve_task_1_1(xk, yk, x):
    L = 0
    for i in range(4):
        p = 1
        for j in range(4):
            if j != i:
                p *= (x - xk[j]) / (xk[i] - xk[j])
        L += yk[i] * p
    res_f_x = sin_function(x)
    print('f(x): ', res_f_x)
    print('Многочлен Лагранжа: ', L)
    print('Погрешность: ', abs(L - res_f_x))
    print('Левая производная: ', left_derivative(x, 0.001, sin_function),
          'Погрешность: ', abs(left_derivative(x, 0.001, sin_function) - res_f_x))

    print('Правая производная: ', right_derivative(x, 0.001, sin_function),
          'Погрешность: ', abs(right_derivative(x, 0.001, sin_function) - res_f_x))

    print('Центральная производная: ', center_derivative(x, 0.001, sin_function),
          'Погрешность: ', abs(center_derivative(x, 0.001, sin_function) - res_f_x))

    print('Точное значение производной: ', res_f_x)
    print()


def solve_task_1_2(xk, yk, x, a, b, func):
    L = aitken_interpolation(xk, yk, x, a, b)
    exact_value = func(x)
    print('Интерполяция Эйткену: ', L)
    print('Точное значение: ', exact_value)
    print('Погрешность: ', abs(L - exact_value))
    print()


def solve_task_2(xk, n, m):
    print('Xk = ', xk[0])
    print('Правая производная: ', right_derivative(xk[0], 0.001, sin_half_arg_function),
          'Погрешность: ', abs(right_derivative(xk[0], 0.001, sin_half_arg_function) - function_derivative(xk[0])))
    print('Точное значение первой производной: ', function_derivative(xk[0]))
    print('Точное значение второй производной: ', function_second_derivative(xk[0]))
    print()

    for i in range(1, n - 1):
        print('Xk = ', xk[i])
        print('Левая производная: ', left_derivative(xk[i], 0.001, sin_half_arg_function),
              'Погрешность: ', abs(left_derivative(xk[i], 0.001, sin_half_arg_function) - function_derivative(xk[i])))

        print('Правая производная: ', right_derivative(xk[i], 0.001, sin_half_arg_function),
              'Погрешность: ', abs(right_derivative(xk[i], 0.001, sin_half_arg_function) - function_derivative(xk[i])))

        print('Центральная производная: ', center_derivative(xk[i], 0.001, sin_half_arg_function),
              'Погрешность: ', abs(center_derivative(xk[i], 0.001, sin_half_arg_function) - function_derivative(xk[i])))

        print('Вторая производная: ', second_derivative(xk[i], 0.001, sin_half_arg_function),
              'Погрешность: ', abs(second_derivative(xk[i], 0.001, sin_half_arg_function) - function_second_derivative(xk[i])))

        print('Точное значение первой производной: ', function_derivative(xk[i]))
        print('Точное значение второй производной: ', function_second_derivative(xk[i]))
        print()

    print('Xk = ', xk[n - 1])
    print('Левая производная: ', left_derivative(xk[n - 1], 0.001, sin_half_arg_function),
          'Погрешность: ', abs(left_derivative(xk[n - 1], 0.001, sin_half_arg_function) - function_derivative(xk[n - 1])))
    print('Точное значение первой производной: ', function_derivative(xk[n - 1]))
    print('Точное значение второй производной: ', function_second_derivative(xk[n - 1]))
    print()
    yk = [sin_half_arg_function(x) for x in xk]
    solve_task_1_2(xk, yk, m, 0, n - 1, sin_half_arg_function)


# 1.1
xk_task1_1 = [1.0, 1.05, 1.1, 1.15]
yk_task1_1 = [0.84147, 0.86742, 0.89121, 0.91276]
x_task1_1 = 1.04
solve_task_1_1(xk_task1_1, yk_task1_1, x_task1_1)

# 1.2
xk_task1_2 = [1.0, 1.08, 1.2, 1.27, 1.31, 1.38]
yk_task1_2 = [sin_function(x) for x in xk_task1_2]
x_task1_2 = 1.04
solve_task_1_2(xk_task1_2, yk_task1_2, x_task1_2, 0, 5, sin_function)

# 2
xk_task2 = []
a_task2, b_task2, m_task2 = 0, 1, 0.06
n_task2 = 5
for i in range(n_task2):
    xk_task2.append(a_task2 + i * (b_task2 - a_task2) / (n_task2 - 1))
xk_task2.append(m_task2)
xk_task2.sort()

solve_task_2(xk_task2, n_task2 + 1, m_task2)
