import uuid

from model.agents.herbivore import Herbivore


class AgentGenerator:
    def __init__(self, model, schedule, grid):
        self.schedule = schedule
        self.grid = grid
        self.model = model

    def add_agents_randomly(
            self,
            agents_number,
            agent_class=Herbivore,
            agent_parameters=None,
    ):
        for _i in range(agents_number):
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

            self.grid.place_agent_randomly(agent)

    def initialise_agents(self):
        self.add_agents_randomly(
            agents_number=1
        )
