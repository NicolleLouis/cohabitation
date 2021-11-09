from model.agents.carnivore import Carnivore


class Wolf(Carnivore):
    name = "Loup"

    def __init__(
            self,
            model,
            unique_id,
            specie_logger,
    ):
        from model.agents.animal_list.rabbit import Rabbit

        stomach_size = 25
        life_expectancy = 80
        reproduction_probability = 2
        maximum_children_number = 1
        sexual_maturity = 15
        weight = 70
        energy_cost = 5
        color = "red"
        prey_list = {
                Rabbit: 80,
            }
        super(Wolf, self).__init__(
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
        )
