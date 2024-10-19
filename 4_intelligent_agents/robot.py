from agent import Agent
import utils
import random
import heapq


class Robot(Agent):

    def __init__(self, position: tuple[int, int]):
        super().__init__(position)
        self.water_level = 100
        self.water_station_location = []

    def decide(self, percept: dict[tuple[int, int], ...]):
        flames = []

        for cell in percept:
            if utils.is_flame(percept[cell]):
                flames.append(cell)
            elif utils.is_water_station(percept[cell]) and cell not in self.water_station_location:
                self.water_station_location.append(cell)
            #elif utils.is_robot(percept[cell]):
            #    pass
        

        if self.water_level == 0 and len(self.water_station_location) > 0:
            return "fill tank"
        elif len(flames) > 0 and self.water_level > 0:
            return "firefight", random.choice(flames)
        
        return None


    def act(self, environment):
        neighbours = self.sense(environment)
        action = self.decide(neighbours)
        
        if action == None: # random move
            new_position = self.select_random_move(neighbours)
            self.move(environment, new_position)
        elif action == "fill tank": # go to water station
            path = self.calc_path(self.position, self.water_station_location[0], environment) # will currently always go to the first water station found, pls change
            print(path)
        elif action[0] == "firefight": # fight fire
            self.firefight(environment, action[1])
            
        
    def firefight(self, environment, fire):
        environment.extinguish(fire)
        self.water_level -= 5

    
    def select_random_move(self, neighbours):
        valid_moves = []

        for cell in neighbours:
            if neighbours[cell] == " ":
                valid_moves.append(cell)
        
        return random.choice(valid_moves)


    def move(self, environment, to):
        if environment.move_to(self.position, to):
            self.position = to
    
    def fill_tank(self):
        self.water_level = 100

    def __str__(self):
        return '🚒'

    # MANHATTAN DISTANCE FUNCTIONS
    def calc_path(self, start, goal, e):
        p_queue = []
        heapq.heappush(p_queue, (0, start))

        directions = {
            "right": (0, 1),
            "left": (0, -1),
            "up": (-1, 0),
            "down": (1, 0)
        }
        predecessors = {start: None}
        g_values = {start: 0}

        while len(p_queue) != 0:
            current_cell = heapq.heappop(p_queue)[1]
            if current_cell == goal:
                return self.get_path(predecessors, start, goal)
            for direction in ["up", "right", "down", "left"]:
                row_offset, col_offset = directions[direction]
                neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)

                if self.viable_move(neighbour[0], neighbour[1], e) and neighbour not in g_values:
                    cost = g_values[current_cell] + 1
                    g_values[neighbour] = cost
                    f_value = cost + self.calc_distance(goal, neighbour)
                    heapq.heappush(p_queue, (f_value, neighbour))
                    predecessors[neighbour] = current_cell

    def get_path(self, predecessors, start, goal):
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = predecessors[current]
        path.append(start)
        path.reverse()
        return path
    
    def viable_move(self, x, y, e):
        print(e.get_cells([(x,y)]))
        if e.get_cells([(x,y)])[(x,y)] == " ":
            return True
        return False

    def calc_distance(self, point1: tuple[int, int], point2: tuple[int, int]):
        x1, y1 = point1
        x2, y2 = point2
        return abs(x1 - x2) + abs(y1 - y2)

    # END OF MANHATTAN DISTANCE FUNCTIONS