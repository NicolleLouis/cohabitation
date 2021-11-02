import uuid

from model.agents.animal import Animal


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

    def initialise_agents(self):
        self.add_agents_randomly(
            agents_number=100,
            agent_parameters={
                "life_expectancy": 25,
                "reproduction_probability": 1,
                "maximum_children_number": 4,
                "sexual_maturity": 10,
            }
        )
