import random


class ProbabilityService:
    @staticmethod
    def random_percentage(percentage):
        return random.randint(0, 100) < percentage

    @staticmethod
    def random_probability_1000(probability):
        return random.randint(0, 1000) < probability

    @staticmethod
    def random_number(maximum, minimum=0):
        return random.randint(minimum, maximum)
