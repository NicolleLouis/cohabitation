from model.agents.carnivore import Carnivore


class Fox(Carnivore):
    name = "Renard"

    def __init__(
            self,
            model,
            unique_id,
            specie_logger,
    ):
        from model.agents.animal_list.rabbit import Rabbit

        stomach_size = 10
        life_expectancy = 40
        reproduction_probability = 10
        maximum_children_number = 4
        sexual_maturity = 10
        weight = 25
        energy_cost = 2
        color = "blue"
        sight_size = 1
        prey_list = {
                Rabbit: 50,
            }
        super(Fox, self).__init__(
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
            prey_list=prey_list,
            energy_cost=energy_cost,
            sight_size=sight_size,
        )
