from mesa import Agent


class Herbivore(Agent):
    def __init__(self, unique_id, model, **kwargs):
        super().__init__(unique_id, model)

    def step(self):
        print("here")

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
