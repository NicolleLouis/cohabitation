from model.agents.animal import Animal


class SpecieLogger:
    def __init__(
            self,
            agent_class=Animal
    ):
        self.agent_class = agent_class
        self.name = agent_class.name
        self.number_death = {}
        self.number_children = 0

    def add_death(self, reason):
        if reason in self.number_death:
            self.number_death[reason] += 1
        else:
            self.number_death[reason] = 1

    def add_children(self, children_number):
        self.number_children += children_number

    def log(self):
        print("#####")
        print(f'Specie: {self.name}')
        print(f'Number of death: {self.number_death}')
        print(f'Number of reproduction: {self.number_children}')
        print("#####")
