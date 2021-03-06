from model.agents.animal import Animal
from service.probability import ProbabilityService


class Carnivore(Animal):
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
            weight,
            prey_list,
            energy_cost,
            sight_size,
            color="green",
    ):
        """
        :param unique_id:
        :param model:
        :param stomach_size: int
        :param life_expectancy: int
        :param reproduction_probability: int
        :param maximum_children_number: int
        :param sexual_maturity: int
        :param weight: int
        :param energy_cost: int
        :param sight_size: int
        :param specie_logger: logger
        :param prey_list: {prey_class: hunt_probability}
        :param color: string
        """
        super(Carnivore, self).__init__(
            unique_id=unique_id,
            model=model,
            stomach_size=stomach_size,
            life_expectancy=life_expectancy,
            reproduction_probability=reproduction_probability,
            maximum_children_number=maximum_children_number,
            sexual_maturity=sexual_maturity,
            specie_logger=specie_logger,
            weight=weight,
            energy_cost=energy_cost,
            color=color,
            sight_size=sight_size,
        )
        self.prey_list = prey_list

    def eat(self):
        potential_preys = list(
            filter(
                lambda agent: type(agent) in self.prey_list,
                self.grid.get_grid_content(
                    positions=self.pos
                )
            )
        )
        for prey in potential_preys:
            food_needed = self.stomach_size - self.food
            if food_needed * 2 < prey.weight:
                continue
            hunt_probability = self.prey_list[type(prey)]
            if ProbabilityService.random_percentage(hunt_probability):
                self.food = min(self.food + prey.weight, self.stomach_size)
                prey.death(f'Eaten by {self.name}')
                self.specie_logger.add_food(prey.name)

    def food_on_position(self, position):
        potential_preys = list(
            filter(
                lambda agent: type(agent) in self.prey_list,
                self.grid.get_grid_content(
                    positions=position
                )
            )
        )
        food = 0
        for prey in potential_preys:
            food += prey.weight
        return food
