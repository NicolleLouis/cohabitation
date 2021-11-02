from mesa import Agent


class Herbivore(Agent):
    def __init__(self, unique_id, model, **kwargs):
        super().__init__(unique_id, model)

    def step(self):
        print("here")
