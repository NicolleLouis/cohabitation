import uuid

from model.agents.animal import Animal
from model.agents.animal_list.rabbit import Rabbit
from model.agents.animal_list.wolf import Wolf
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
             agent_class,
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

    def add_animal(self, animal_class, number=100):
        animal_logger = SpecieLogger(animal_class)
        self.add_agents_randomly(
            agents_number=number,
            agent_class=animal_class,
            agent_parameters={
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
        rabbit_logger = self.add_animal(Rabbit, 100)
        wolf_logger = self.add_animal(Wolf, 1)
        grass_logger = self.add_grass()
        return [rabbit_logger, wolf_logger, grass_logger]
