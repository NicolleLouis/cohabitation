from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid

from model.model.model import CohabitationModel


class VisualizationService:
    @classmethod
    def display_model(
            cls,
            size=25,
    ):
        grid = CanvasGrid(
            portrayal_method=cls.agent_portrayal,
            grid_width=size,
            grid_height=size,
            canvas_width=500,
            canvas_height=500,
        )
        server = ModularServer(
            model_cls=CohabitationModel,
            visualization_elements=[
                grid,
            ],
            model_params={
                "size": size,
            }
        )
        server.port = 8521
        server.launch()

    @staticmethod
    def agent_portrayal(agent):
        return agent.display()
