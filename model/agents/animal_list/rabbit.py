from model.agents.herbivore import Herbivore


class Rabbit(Herbivore):
    name = "Lapin"

    def __init__(
            self,
            model,
            unique_id,
            specie_logger,
    ):
        stomach_size = 3
        life_expectancy = 10
        reproduction_probability = 4
        maximum_children_number = 8
        sexual_maturity = 5
        weight = 3
        energy_cost = 1
        sight_size = 1
        color = "green"
        super(Rabbit, self).__init__(
            unique_id=unique_id,
            model=model,
            stomach_size=stomach_size,
            life_expectancy=life_expectancy,
            reproduction_probability=reproduction_probability,
            maximum_children_number=maximum_children_number,
            sexual_maturity=sexual_maturity,
            weight=weight,
            specie_logger=specie_logger,
            color=color,
            energy_cost=energy_cost,
            sight_size=sight_size,
        )
