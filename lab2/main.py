# Численное решение систем линейных алгебраических уравнений

def format(number):
    return "{:.25f}".format(number)


def short_format(number):
    return "{:.5f}".format(number)


def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, map(short_format, row))))


class Program:
    def __init__(self, matrix, b, precision):
        self.matrix = matrix.copy()
        self.b = b
        self.precision = precision

    def gauss(self):
        matrix = [row[:] for row in self.matrix]
        size = len(matrix)

        i = 0
        for row in matrix:
            row.append(b[i])
            i += 1

        for row in range(size):
            for i in range(row, size):
                if abs(matrix[i][row]) <= abs(matrix[row][row]):
                    continue

            for j in range(row + 1, size):
                divisor = matrix[j][row] / matrix[row][row]
                for m in range(row, size + 1):
                    matrix[j][m] -= divisor * matrix[row][m]

        print("Треугольная матрица: ")
        display_matrix(matrix)
        x = [0] * size
        x[size - 1] = matrix[size - 1][size] / matrix[size - 1][size - 1]
        for i in range(size - 1, -1, -1):
            mod = 0
            for j in range(i + 1, size):
                mod = mod + matrix[i][j] * x[j]
            x[i] = (matrix[i][size] - mod) / matrix[i][i]
        return x

    def seidel(self, b, eps=1e-7, max_iteration=1000):
        matrix = [row[:] for row in self.matrix]
        n = len(matrix)
        x = [0] * n
        it_count = 0

        for _ in range(max_iteration):
            it_count += 1
            x_new = x[:]

            for i in range(n):
                s1 = sum(matrix[i][j] * x_new[j] for j in range(i))
                s2 = sum(matrix[i][j] * x[j] for j in range(i + 1, n))
                x_new[i] = (b[i] - s1 - s2) / matrix[i][i]

            if all(abs(x_new[i] - x[i]) < eps for i in range(n)):
                print(it_count)
                return x_new

            x = x_new
        print("Метод Зейделя не отработал")
        return None


matrix = [
    [5.9, 1.2, 2.1, 0.9],
    [1.2, 7.2, 1.5, 2.5],
    [2.1, 1.5, 9.8, 1.3],
    [0.9, 2.5, 1.3, 6.1]
]

b = [-2, 5.3, 10.3, 12.6]
right_answer = [-1, 0, 1, 2]

program = Program(matrix, b, right_answer)
sol_1 = program.gauss()

values = [format(abs(sol_1[index] - right_answer[index])) for index in range(len(sol_1))]
print("Метод Гаусса: ", sol_1)
print("Погрешность: ", max(values))

print()
sol_2 = program.seidel(b)
values = [format(abs(sol_2[index] - right_answer[index])) for index in range(len(sol_2))]
print("Метод Зейдель: ", sol_2)
print("Погрешность: ", max(values))


print()
print()
numbers = [-0.9999999999999999, 0.0000000000000004, 1.0, 1.9999999999999996]
num = max([float(format(abs(numbers[index] - right_answer[index]))) for index in range(len(numbers))])
print("Метод Гаусса: " + '\n'.join(["{:.16f}".format(number) for number in numbers]))
print("Погрешность: {:.25f}".format(num))
print()
print()
numbers = [-1.0000000000000018, 0.0000000000000004, 0.9999999999999983, 1.9999999999999997]
num = max([float(format(abs(numbers[index] - right_answer[index]))) for index in range(len(numbers))])
print("Метод Зейдель: " + '\n'.join(["{:.16f}".format(number) for number in numbers]))
print("Погрешность: {:.25f}".format(num))
