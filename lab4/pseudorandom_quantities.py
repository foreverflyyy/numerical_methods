# алгоритм Обратных функций
class LCG:
    def __init__(self, seed, a=1664525, c=1013904223, m=2 ** 32):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def random(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed / self.m


class DiscreteRandomVariable:
    def __init__(self, values, probabilities, seed):
        self.values = values
        self.probabilities = probabilities
        self.cumulative_probabilities = self.cumulative_probabilities()
        self.lcg = LCG(seed)

    def cumulative_probabilities(self):
        cumulative_probabilities = [self.probabilities[0]]
        for i in range(1, len(self.probabilities)):
            cumulative_probabilities.append(cumulative_probabilities[i - 1] + self.probabilities[i])
        return cumulative_probabilities

    def generate_random(self):
        rand_num = self.lcg.random()
        for i in range(len(self.cumulative_probabilities)):
            # print(rand_num, self.cumulative_probabilities[i])
            if rand_num <= self.cumulative_probabilities[i]:
                return self.values[i]


n = 1_000
seed_value = 12345
values = [1, 2, 30, 4000000]
probabilities = [0.3, 0.2, 0.35, 0.15]
numbers = [1, 2, 30, 4_000_000]

drv = DiscreteRandomVariable(values, probabilities, seed_value)
random_nums = [drv.generate_random() for _ in range(n)]

average_number = sum(random_nums) / n
print(f"Average number: {average_number}")

elems = []
for i in range(len(numbers)):
    elems.append(numbers[i] * probabilities[i])

math_expectation = sum(elems)
print(f"Math expectation: {average_number}")
