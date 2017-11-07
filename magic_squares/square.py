import random
import math

class Square():
    __slots__ = ["dimension", "size", "max_rand", "square", "squared_square", "power"]

    def __init__(self, dimension, power=2, max_rand_digits=2):
        '''
        Represents a mundane square, which may or may not be magical.

        Args:
            - dimension (Integer) - The size of one side of the square
            - max_rand_digits (Integer) - The maximum number of digits in a random number (Default: 2)
        '''
        self.dimension = dimension
        self.size = dimension * dimension
        self.power = power

        self.max_rand = "9"
        while len(self.max_rand) < max_rand_digits:
            self.max_rand += "9"
        self.max_rand = int(self.max_rand)

        self.square = []

    def __str__(self):
        if len(self.square) == 0:
            return "Empty Square"

        string = ""
        for i in range(0, self.dimension):
            string = f"{string}\n{self.get_row(i, self.square)}"

        string += "\n\n"

        for i in range(0, self.dimension):
            string = f"{string}\n{self.get_row(i, self.squared_square)}"

        return string

    def get_row(self, i, square):
        return square[i*self.dimension:(i+1)*self.dimension]

    def get_column(self, i, square):
        return square[i::self.dimension]

    def get_diagonal_1(self, square):
        return square[0::self.dimension+1]

    def get_diagonal_2(self, square):
        return square[self.dimension-1::self.dimension-1][:self.dimension]

    def get_random_not_in_square(self):
        num = random.randint(0, self.max_rand)
        while num in self.square:
            num = random.randint(0, self.max_rand)
        return num

    def fill(self):
        # Seed the square with random numbers until we have dimension^2 unique
        for _ in range(self.size):
            self.square.append(self.get_random_not_in_square())

        self.squared_square = [math.pow(x, self.power) for x in self.square]

    def empty(self):
        self.square = []
        self.squared_square = []

    def is_magic(self):
        if not self.is_semi_magic():
            return False

        target_sum = sum(self.get_row(0, self.squared_square))

        if sum(self.get_diagonal_1(self.squared_square)) != target_sum:
            return False
        if sum(self.get_diagonal_2(self.squared_square)) != target_sum:
            return False

        return True

    def is_semi_magic(self):
        target_sum = sum(self.get_row(0, self.squared_square))

        # Check all rows and columns
        for i in range(0, self.dimension):
            if sum(self.get_row(i, self.squared_square)) != target_sum:
                return False
            if sum(self.get_column(i, self.squared_square)) != target_sum:
                return False

        return True

    def magic_string(self):
        print(f"Diagonal 1 Sum: {sum(self.get_diagonal_1(self.squared_square))}")
        print(f"Diagonal 2 Sum: {sum(self.get_diagonal_2(self.squared_square))}")
        # Check all rows and columns
        for i in range(0, self.dimension):
            print(f"Row {i} sum: {sum(self.get_row(i, self.squared_square))}")
            print(f"Col {i} sum: {sum(self.get_column(i, self.squared_square))}")
