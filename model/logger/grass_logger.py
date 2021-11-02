from model.agents.grass import Grass


class GrassLogger:
    def __init__(
            self,
    ):
        self.name = Grass.name
        self.number_generated = 0
        self.number_eaten = 0

    def add_generated(self, amount_generated):
        self.number_generated += amount_generated

    def add_eaten(self, amount_eaten):
        self.number_eaten += amount_eaten

    def log(self):
        print("#####")
        print(f'Specie: {self.name}')
        print(f'Number of grass generated: {self.number_generated}')
        print(f'Number of grass eaten: {self.number_eaten}')
        print("#####")
