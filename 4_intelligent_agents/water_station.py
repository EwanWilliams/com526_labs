from agent import Agent
import utils

class WaterStation(Agent):

    def __init__(self, position):
        super().__init__(position)

    def decide(self, percept):
        pass

    def act(self, environment):
        pass

    def __str__(self):
        return '💧'