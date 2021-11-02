class MovementService:
    @staticmethod
    def random_neighbour(agent):
        new_position = agent.random.choice(
            agent.model.grid.get_agent_neighbour_position(
                agent=agent
            )
        )
        return new_position

    @staticmethod
    def random_position(agent):
        new_position = agent.model.grid.get_random_position()
        return new_position
