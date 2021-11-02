from mesa import Agent

from service.movement import MovementService


class Herbivore(Agent):
    def __init__(self, unique_id, model, **kwargs):
        super().__init__(unique_id, model)
        self.grid = self.model.grid

    def step(self):
        self.move()

    def move(self):
        new_position = self.next_position()
        self.modify_position(new_position)

    def next_position(self):
        new_position = MovementService.random_neighbour(agent=self)
        return new_position

    def modify_position(self, position):
        self.grid.move_agent(self, position)

    @staticmethod
    def display():
        """
        Documentation is in the class: CanvasGrid(VisualizationElement)
        file: CanvasGridVisualization from mesa.visualization.modules
        """
        data = {
            "Shape": "circle",
            "Color": "green",
            "Filled": "false",
            "Layer": 0,
            "r": 0.5,
            "w": 0.5,
            "h": 0.5,
            "text_color": "white"
        }
        return data
