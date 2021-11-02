from mesa import Model
from mesa.time import RandomActivation

from model.model.agent_generator import AgentGenerator
from model.model.grid import Grid


class CohabitationModel(Model):
    def __init__(
            self,
            size=25,
            maximum_number_of_turn=500,
    ):
        super().__init__()

        self.schedule = RandomActivation(self)
        self.grid = Grid(
            size=size
        )
        self.agent_generator = AgentGenerator(
            model=self,
            grid=self.grid,
            schedule=self.schedule
        )
        self.loggers = self.generate_agents()

        self.running = True
        self.turn_number = 0
        self.maximum_number_of_turn = maximum_number_of_turn

    def generate_agents(self):
        loggers = self.agent_generator.initialise_agents()
        return loggers

    def step(self):
        self.schedule.step()
        self.should_continue()
        if not self.running:
            self.end_step()

    def should_continue(self):
        self.turn_number += 1
        if self.turn_number > self.maximum_number_of_turn:
            self.running = False
            return

    def end_step(self):
        for logger in self.loggers:
            logger.log()
