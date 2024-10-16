from agent import Agent
from robot import Robot
import utils

class WaterStation(Agent):

    def __init__(self, position):
        super().__init__(position)

    def decide(self, percept):
        for cell in percept:
            if utils.is_robot(percept[cell]):
                return percept[cell]
        return None

    def act(self, environment):
        robot_present = self.decide(self.sense(environment))

        if robot_present:
            robot_present.fill_tank()
            return True
        
        return False
            
        
    def __str__(self):
        return '💧'
    