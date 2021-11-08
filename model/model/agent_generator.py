import uuid

from model.agents.animal import Animal
from model.agents.animal_list.deer import Deer
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

    def add_rabbit(self):
        rabbit_logger = SpecieLogger(Rabbit)
        self.add_agents_randomly(
            agents_number=100,
            agent_class=Rabbit,
            agent_parameters={
                "specie_logger": rabbit_logger
            }
        )
        return rabbit_logger

    def add_deer(self):
        deer_logger = SpecieLogger(Deer)
        self.add_agents_randomly(
            agents_number=100,
            agent_class=Rabbit,
            agent_parameters={
                "specie_logger": deer_logger
            }
        )
        return deer_logger

    def add_wolf(self):
        wolf_logger = SpecieLogger(Wolf)
        self.add_agents_randomly(
            agents_number=25,
            agent_class=Wolf,
            agent_parameters={
                "specie_logger": wolf_logger
            }
        )
        return wolf_logger

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
        rabbit_logger = self.add_rabbit()
        # deer_logger = self.add_deer()
        wolf_logger = self.add_wolf()
        grass_logger = self.add_grass()
        return [rabbit_logger, wolf_logger, grass_logger]
