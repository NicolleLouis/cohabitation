import uuid

from model.agents.animal import Animal
from model.agents.grass import Grass
from model.logger.grass_logger import GrassLogger
from model.logger.specie_logger import SpecieLogger
from service.geographic import GeographicService


class AgentGenerator:
    def __init__(self, model, schedule, grid):
        self.schedule = schedule
        self.grid = grid
        self.model = model

    def add_agents_randomly(
            self,
            agents_number,
            agent_class=Animal,
            agent_parameters=None,
    ):
        for _i in range(agents_number):
            agent = self.create_agent(
                agent_class=agent_class,
                agent_parameters=agent_parameters
            )

            self.grid.place_agent_randomly(agent)

    def add_agents(
             self,
             agents_number,
             position,
             agent_class=Animal,
             agent_parameters=None,
     ):
        for _i in range(agents_number):
            agent = self.create_agent(
                agent_class=agent_class,
                agent_parameters=agent_parameters
            )

            self.grid.place_agent(
                agent=agent,
                position=position
            )

    def create_agent(
            self,
            agent_class,
            agent_parameters,
    ):
        if agent_parameters is not None:
            agent = agent_class(
                unique_id=uuid.uuid4(),
                model=self.model,
                **agent_parameters,
            )
        else:
            agent = agent_class(
                unique_id=uuid.uuid4(),
                model=self.model,
            )
        self.schedule.add(agent)
        return agent

    def add_herbivore(self):
        animal_logger = SpecieLogger(Animal)
        self.add_agents_randomly(
            agents_number=100,
            agent_parameters={
                "life_expectancy": 25,
                "stomach_size": 5,
                "reproduction_probability": 1,
                "maximum_children_number": 10,
                "sexual_maturity": 10,
                "specie_logger": animal_logger
            }
        )
        return animal_logger

    def add_grass(self):
        grass_logger = GrassLogger()
        positions = GeographicService.get_all_positions(self.model.size)
        for position in positions:
            self.add_agents(
                agents_number=1,
                agent_class=Grass,
                position=position,
                agent_parameters={
                    "grass_logger": grass_logger
                }
            )
        return grass_logger

    def initialise_agents(self):
        animal_logger = self.add_herbivore()
        grass_logger = self.add_grass()
        return [animal_logger, grass_logger]
