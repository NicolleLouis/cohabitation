class MovementService:
    @staticmethod
    def get_neighbours(agent, radius=1):
        positions = agent.model.grid.get_agent_neighbour_position(
            agent=agent,
            radius=radius
        )
        return positions

    @staticmethod
    def random_position(agent):
        new_position = agent.model.grid.get_random_position()
        return new_position
