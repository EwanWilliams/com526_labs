import utils


class Environment:

    def __init__(self, map_path):
        self.file_path = map_path
        self.world = self.load_assets(self.load_map())

    def load_map(self):
        try:
            with open(self.file_path) as f:
                world_map = row = [[col.lower() for col in line.strip()] for line in f]

                # quick error check
                first_row = len(world_map[0])
                for row in world_map:
                    if len(row) != first_row:
                        raise Exception("Map rows are not even")
                return world_map
        except FileNotFoundError:
            print(f"File not found")
        except PermissionError:
            print(f"File read permissions were denied")
        except IOError as e:
            print(f"IO error: {e}")

        return []

    def load_assets(self, world_map:list):
        for i in range(len(world_map)):
            for j in range(len(world_map[i])):
                if world_map[i][j] == 's':
                    world_map[i][j] = utils.WaterStation((j, i))
                elif world_map[i][j] == 'r':
                    world_map[i][j] = utils.Robot((j, i))
                elif world_map[i][j] == '*':
                    world_map[i][j] = utils.Flame()
        return world_map

    def get_cells(self, positions:list) -> dict[tuple[int,int],...]:
        cells = {}
        for pos in positions:
            cells[pos] = self.world[pos[1]][pos[0]]
        return cells
    
    def move_to(self, current, new):
        if self.world[current[1]][current[0]] != " ":
            moving_char = self.world[current[1]][current[0]]
            self.world[current[1]][current[0]] = " "
            self.world[new[1]][new[0]] = moving_char
            return True
        return False
    
    def extinguish(self, fire):
        if utils.is_flame(self.world[fire[1]][fire[0]]):
            self.world[fire[1]][fire[0]] = " "
            return True
        return False
        

    def __str__(self):
        out = ""
        for row in self.world:
            for col in row:
                out += f"{col}\t"
            out += "\n"
        return out


if __name__ == "__main__":
    e = Environment("map.txt")

    water = e.world[1][5]
    robot1 = e.world[5][5]
    robot1.water_level = 5
    robot1.water_station_location.append((5,1))
    print(e)
    input()
    
    for i in range(1000):  # Change 1 simulate more moves. I.e. 100 would simulate 100 moves
        # Call the act method for each agent operating in the environment
        
        water.act(e)
        robot1.act(e)
        print(f"Water level: {robot1.water_level}")
        print(f"Water station: {robot1.water_station_location}")
        print(e)
        print(i)
        input()
