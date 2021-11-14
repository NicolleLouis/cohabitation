from mesa import Agent


class Grass(Agent):
    name = "Herbe"

    def __init__(
            self,
            unique_id,
            model,
            grass_logger,
    ):
        super(Grass, self).__init__(unique_id=unique_id, model=model)
        self.food = 0
        self.food_growth = 2
        self.grass_logger = grass_logger

    def step(self):
        self.food += self.food_growth
        self.grass_logger.add_generated(self.food_growth)

    def eaten(self, food_eaten):
        if food_eaten < 0:
            raise Exception("Food consumption must be > 0")
        self.food = self.food - food_eaten
        self.grass_logger.add_eaten(food_eaten)

    def display(self):
        return {}
