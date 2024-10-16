from agent import Agent
import utils

class WaterStation(Agent):

    def __init__(self, position):
        super().__init__(position)

    def decide(self, percept):
        for cell in percept:
            if utils.is_robot(percept[cell]):
                return "fill", percept[cell]
            return "idle", None

    def act(self, environment):
        decision =  self.decide(self.sense(environment))

        if decision[0] == "fill":
            return decision[1]
        elif decision[0] == "idle":
            return None
        else:
            pass
        

    def __str__(self):
        return '💧'