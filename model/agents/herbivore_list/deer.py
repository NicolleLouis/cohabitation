from model.agents.herbivore import Herbivore


class Deer(Herbivore):
    name = "Biche"

    def __init__(
            self,
            model,
            unique_id,
            specie_logger,
    ):
        stomach_size = 30
        life_expectancy = 50
        reproduction_probability = 10
        maximum_children_number = 1
        sexual_maturity = 5
        color = "blue"
        super(Deer, self).__init__(
            unique_id=unique_id,
            model=model,
            stomach_size=stomach_size,
            life_expectancy=life_expectancy,
            reproduction_probability=reproduction_probability,
            maximum_children_number=maximum_children_number,
            sexual_maturity=sexual_maturity,
            specie_logger=specie_logger,
            color=color,
        )
