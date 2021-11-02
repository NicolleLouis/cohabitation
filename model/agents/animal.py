from mesa import Agent

from model.agents.grass import Grass
from service.movement import MovementService
from service.probability import ProbabilityService


class Animal(Agent):
    name = "Basic Animal"

    def __init__(
            self,
            unique_id,
            model,
            stomach_size,
            life_expectancy,
            reproduction_probability,
            maximum_children_number,
            sexual_maturity,
            specie_logger,
    ):
        super().__init__(unique_id, model)
        self.grid = self.model.grid
        self.age = 0
        self.is_alive = True
        self.has_reproduced = False

        self.stomach_size = stomach_size
        self.food = self.stomach_size
        self.life_expectancy = life_expectancy
        self.reproduction_probability = reproduction_probability
        self.maximum_children_number = maximum_children_number
        self.sexual_maturity = sexual_maturity
        self.specie_logger = specie_logger

    def step(self):
        self.move()
        self.nutrition()
        self.reproduction()
        self.ageing()

    def move(self):
        if not self.is_alive:
            return

        new_position = self.next_position()
        self.modify_position(new_position)

    def next_position(self):
        new_position = MovementService.random_neighbour(agent=self)
        return new_position

    def modify_position(self, position):
        self.grid.move_agent(self, position)

    def nutrition(self):
        if not self.is_alive:
            return

        self.food = self.food - 1
        if self.food <= 0:
            self.death("Food")
            return
        self.eat()

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
        grass.eaten(food_eaten)

    def get_neighbors(self):
        neighbors = self.grid.get_grid_content(
            positions=self.grid.get_agent_neighbour_position(
                agent=self
            )
        )
        neighbors.remove(self)
        neighbors = list(
            filter(
                lambda neighbor: isinstance(neighbor, Animal),
                neighbors
            )
        )
        return neighbors

    def has_reproduce(self):
        self.has_reproduced = True

    def reset_reproduction(self):
        self.has_reproduced = False

    def can_reproduce(self):
        return not self.has_reproduced

    def reproduction(self):
        if self.has_reproduced:
            return

        if not self.is_alive:
            return

        if self.age < self.sexual_maturity:
            return

        neighbors = self.get_neighbors()
        reproducible_neighbors = list(
            filter(
                lambda neighbor: neighbor.can_reproduce(),
                neighbors
            )
        )
        for neighbor in reproducible_neighbors:
            if ProbabilityService.random_percentage(self.reproduction_probability):
                neighbor.has_reproduce()
                number_of_children = ProbabilityService.random_number(
                    maximum=self.maximum_children_number,
                    minimum=1,
                )
                self.specie_logger.add_children(number_of_children)
                for _children in range(number_of_children):
                    self.create_child()

    def create_child(self):
        self.model.agent_generator.add_agents(
            agents_number=1,
            agent_parameters={
                "life_expectancy": self.life_expectancy,
                "reproduction_probability": self.reproduction_probability,
                "maximum_children_number": self.maximum_children_number,
                "sexual_maturity": self.sexual_maturity,
                "stomach_size": self.stomach_size,
                "specie_logger": self.specie_logger,
            },
            agent_class=type(self),
            position=self.pos
        )

    def ageing(self):
        if not self.is_alive:
            return

        self.age += 1
        if self.age >= self.life_expectancy:
            self.death("Old age")

    def death(self, reason):
        self.is_alive = False
        self.specie_logger.add_death(reason)
        self.model.schedule.remove(self)
        self.grid.remove_agent(self)

    @staticmethod
    def display():
        """
        Documentation is in the class: CanvasGrid(VisualizationElement)
        file: CanvasGridVisualization from mesa.visualization.modules
        """
        data = {
            "Shape": "circle",
            "Color": "green",
            "Filled": "false",
            "Layer": 0,
            "r": 0.5,
            "w": 0.5,
            "h": 0.5,
            "text_color": "white"
        }
        return data
