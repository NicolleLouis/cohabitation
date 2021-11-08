from model.agents.animal import Animal
from model.agents.grass import Grass


class Herbivore(Animal):
    def eat(self):
        grass = list(
            filter(
                lambda agent: isinstance(agent, Grass),
                self.grid.get_grid_content(
                    positions=self.pos
                )
            )
        )[0]
        food_needed = self.stomach_size - self.food
        food_eaten = min(grass.food, food_needed)
        self.food = self.food + food_eaten
        self.specie_logger.add_food(grass.name, food_eaten)
        grass.eaten(food_eaten)
