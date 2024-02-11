import math


def format(number):
    return "{:.8f}".format(number)


class Program:
    def __init__(self, function, x, diff1, diff2, eps, a, b, n):
        self.function = function
        self.x = x
        self.diff1 = diff1
        self.diff2 = diff2
        self.eps = eps
        self.a = a
        self.b = b
        self.n = n

    def newton_method(self):
        print("Метод Ньютона (метод касательных):")
        x = self.a
        i = 0
        if self.function(x) * self.diff2(x) <= 0:
            x = self.b

        while True:
            i += 1
            x_new = x - self.function(x) / self.diff1(x)

            if abs(x_new - x) < self.eps:
                print(f"Число операций: {(i - 1)}")
                return format(x_new)

            x = x_new
            print(format(x))

    def chord_method(self):
        print("Метод хорд:")
        i = 0
        x = self.a
        cur_b = self.b
        if self.function(self.a) * self.function(cur_b) >= 0:
            x, cur_b = cur_b, self.a

        while True:
            i += 1
            x_new = (x - (self.function(x) * (cur_b - x)) / (self.function(cur_b) - self.function(x)))

            if abs(x_new - x) < self.eps:
                print(f"Число операций: {(i - 1)}")
                return format(x_new)

            x = x_new
            print(format(x))

    def secant_method(self):
        print("Метод секущих:")
        i = 0
        x_k = self.b
        x_k_1 = self.a
        while True:
            i += 1
            x_new = x_k - (self.function(x_k) * (x_k - x_k_1)) / (
                    self.function(x_k) - self.function(x_k_1))

            if abs(x_new - x_k) < self.eps:
                print(f"Число операций: {(i - 1)}")
                return format(x_new)

            print(format(x_k))
            x_k_1, x_k = x_k, x_new

    def finite_difference(self):
        print("Конечно-разностный метод Ньютона:")
        i = 0
        x = self.a
        h = (self.b - self.a) / self.n

        while True:
            i += 1
            x_new = (x - (h * self.function(x)) / (self.function(x + h) - (self.function(x))))

            print(format(x))
            if abs(x_new - x) < self.eps:
                print(f"Число операций: {i}")
                return format(x_new)
            x = x_new

    def stef_method(self):
        print("Метод Стеффенсена:")
        i = 0
        x = self.a

        while True:
            i += 1
            x_new = x - self.function(x)**2 / (self.function(x + self.function(x)) - self.function(x))
            if abs(x_new - x) < self.eps:
                print(f"Число операций: {(i - 1)}")
                return format(x_new)

            x = x_new
            print(format(x))

    def simple_iteration(self):
        print("Метод простых итераций:")
        i = 0
        t = 0.1
        x = self.a
        while True:
            i += 1
            x_new = x - t * self.function(x)

            print(format(x))
            if abs(x_new - x) < self.eps:
                print(f"Число операций: {(i - 1)}")
                return format(x_new)

            x = x_new


my_func = lambda x: math.exp(1 - x) + x ** 2 - 5
diff1 = lambda x: -math.exp(1 - x) + 2 * x
diff2 = lambda x: math.exp(1 - x) + 2
eps = 10**(-7)

start = 0.6
end = 2.5
count_steps = 10
step = (end - start) / 10

program = Program(my_func, 1, diff1, diff2, eps, start, end, count_steps)

res_1 = program.newton_method()
print(f"Метод Ньютона result: {res_1}")
print()

res_2 = program.chord_method()
print(f"Метод хорд result: {res_2}")
print()

res_3 = program.secant_method()
print(f"Метод секущих result: {res_3}")
print()

res_4 = program.finite_difference()
print(f"Конечно-разностный метод Ньютона: {res_4}")
print()

res_5 = program.stef_method()
print(f"Метод Стеффенсена result: {res_5}")
print()

res_6 = program.simple_iteration()
print(f"Метод простых итераций result: {res_6}")
print()

# while start <= end:
#     print(f"x: {format(start)}, f(x): {format(my_func(start))}")
#     start += step
