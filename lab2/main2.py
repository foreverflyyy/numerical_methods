import numpy as np


def format(number):
    return "{:.25f}".format(float(number))


def need_round(num):
    return round(float(num), 15)


A = [[5.9, 1.2, 2.1, 0.9],
    [1.2, 7.2, 1.5, 2.5],
    [2.1, 1.5, 9.8, 1.3],
    [0.9, 2.5, 1.3, 6.1]]
B = [-2, 5.3, 10.3, 12.6]

A_origin = [row.copy() for row in A]
B_origin = B.copy()


def gauss_elimination(A, B):
    n = len(A)
    p = list(range(n))
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_index][i]):
                max_index = j
        if max_index != i:
            A[i], A[max_index] = A[max_index], A[i]
            B[i], B[max_index] = B[max_index], B[i]
            p[i], p[max_index] = p[max_index], p[i]
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i]
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = need_round(A[i][j])
    for i in range(len(B)):
        B[i] = need_round(B[i])
    return A, B, p


def back_substitution(U, b):
    n = len(b)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        summation = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - summation) / U[i][i]
    return x


print("Метод Гаусса")
U, c, p = gauss_elimination(A, B)

print("Треугольная матрица:")
for row in U:
    print(row)

x = back_substitution(U, c)
print("Решение СЛАУ: ", x)

diff = [sum(A_origin[i][j] * x[j] for j in range(len(x))) - B_origin[i] for i in range(len(x))]
error = max(abs(val) for val in diff)
print("Погрешность: ", format(error))


def check_convergence(A):
    n = len(A)
    for i in range(n):
        summ = 0
        for j in range(n):
            if i != j:
                summ += np.abs(A[i][j])
        if not (np.abs(A[i][i]) > summ):
            print('Расходится')
            return False
    print('Сходится')
    return True


def prepare_matrix(A, b):
    n = len(b)
    for i in range(n):
        if A[i, i] == 0:
            A[i, i] = 1e-10
        for j in range(n):
            if i != j:
                multiplier = A[j, i] / A[i, i]
                for k in range(n):
                    A[j, k] -= multiplier * A[i, k]
                b[j] -= multiplier * b[i]
    return A, b


def seidel_iteration(A, b, x):
    n = len(b)
    for i in range(n):
        x_new = b[i]
        for j in range(n):
            if j != i:
                x_new -= A[i, j] * x[j]
        x_new /= A[i, i]
        x = x.astype(np.float64)
        x[i] = x_new
    return x


def seidel(A, b, x, tol=1e-10, max_iter=100):
    if not check_convergence(A):
        return False, False

    iter = 0
    for i in range(max_iter):
        x_new = np.copy(x)
        tmp = []
        for j in range(4):
            tmp.append(need_round(x[j]))
        print("Итерация: ", i)
        print("Решение: ", tmp)
        x = seidel_iteration(A, b, x)
        print()
        if (np.linalg.norm(x - x_new) < tol).all():
            iter = i
            break
    return x, iter


print("\nМетод Зейделя")
x = np.zeros_like(B)
diagonalized_A, diagonalized_b = prepare_matrix(np.array(A), np.array(B))
solution, iterations = seidel(diagonalized_A, diagonalized_b, x)

if not solution.all() and not iterations:
    print("Решение расходится")
else:
    tmp = []
    for i in range(4):
        tmp.append(round(float(solution[i]), 20))
    print("Количество итераций:", iterations + 1)
    print("Решение:", end="")
    print(tmp)

    error = max(abs(sum(A_origin[i][j] * solution[j] for j in range(len(solution))) - B_origin[i]) for i in range(len(B)))
    print("Погрешность:", format(error))
