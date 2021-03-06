import random

from mesa import Agent

from constants.gender import Gender
from service.movement import MovementService
from service.probability import ProbabilityService


class Animal(Agent):
    name = "Basic Animal"

    def __init__(
            self,
            unique_id,
            model,
            stomach_size: int,
            life_expectancy: int,
            reproduction_probability: int,
            maximum_children_number: int,
            sexual_maturity: int,
            specie_logger,
            weight: int,
            energy_cost: int,
            sight_size: int,
            gender: str = None,
            color: str = "green"
    ):
        super().__init__(unique_id, model)
        self.grid = self.model.grid
        self.age = 0
        self.is_alive = True
        self.has_reproduced = False

        self.stomach_size = stomach_size
        self.food = self.stomach_size
        self.weight = weight
        self.life_expectancy = life_expectancy
        self.reproduction_probability = reproduction_probability
        self.maximum_children_number = maximum_children_number
        self.sexual_maturity = sexual_maturity
        self.energy_cost = energy_cost
        self.sight_size = sight_size

        if gender is None:
            self.gender = random.choice([Gender.MALE, Gender.FEMALE])
        else:
            self.gender = gender

        self.color = color
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
        potential_positions = MovementService.get_neighbours(agent=self, radius=self.sight_size)
        best_position = random.choice(potential_positions)
        best_food = 0
        for position in potential_positions:
            potential_food = self.food_on_position(position)
            if potential_food > best_food:
                best_food = potential_food
                best_position = position
        return best_position

    def modify_position(self, position):
        self.grid.move_agent(self, position)

    def nutrition(self):
        if not self.is_alive:
            return

        self.food = self.food - self.energy_cost
        if self.food <= 0:
            self.death("Food")
            return
        self.eat()

    def eat(self):
        raise NotImplementedError("Each animal must have a 'eat' function")

    def food_on_position(self, position):
        raise NotImplementedError("Each animal must have a 'food_on_position' function")

    def get_neighbors(self):
        neighbors = self.grid.get_grid_content(
            positions=self.grid.get_agent_neighbour_position(
                agent=self
            )
        )
        neighbors.remove(self)
        neighbors = list(
            filter(
                lambda neighbor: isinstance(neighbor, type(self)),
                neighbors
            )
        )
        return neighbors

    def reproduction(self):
        if not self.is_alive:
            return

        if self.age < self.sexual_maturity:
            return

        if self.gender != Gender.FEMALE:
            return

        neighbors = self.get_neighbors()
        male_neighbors = list(
            filter(
                lambda neighbor: neighbor.gender == Gender.MALE,
                neighbors
            )
        )
        if len(male_neighbors) == 0:
            return

        if ProbabilityService.random_percentage(self.reproduction_probability):
            number_of_children_without_food_consideration = ProbabilityService.random_number(
                maximum=self.maximum_children_number,
                minimum=1,
            )
            real_number_of_children = min(
                number_of_children_without_food_consideration,
                int(self.food / self.energy_cost)
            )
            self.food = self.food - real_number_of_children * self.energy_cost
            self.specie_logger.add_children(real_number_of_children)
            for _children in range(real_number_of_children):
                self.create_child()

    def create_child(self):
        self.model.agent_generator.add_agents(
            agents_number=1,
            agent_parameters={
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

    def __str__(self):
        return f"{self.name}, age: {self.age}, stomach: {self.food}"

    def display(self):
        """
        Documentation is in the class: CanvasGrid(VisualizationElement)
        file: CanvasGridVisualization from mesa.visualization.modules
        """
        data = {
            "Shape": "circle",
            "Color": self.color,
            "Filled": "false",
            "Layer": 0,
            "r": 0.5,
            "w": 0.5,
            "h": 0.5,
            "text_color": "white"
        }
        return data
