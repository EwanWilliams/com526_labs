import utils
import heapq


def a_star(maze, start, goal):
    p_queue = []
    heapq.heappush(p_queue, (0, start))
    maze_size = len(maze[0])
    directions = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0)
    }

    predecessors = {start: None}  # enables the get_path function to backtrack
    g_values = {start: 0}  # the g score for each cell

    while len(p_queue) > 0:  # loop through the queue, only stop if the queue is empty
        current_cell = heapq.heappop(p_queue)[1]  # get this from the priority queue

        if current_cell == goal:  # check if the current cell is the goal
            return get_path(predecessors, start, goal)

        for direction in directions.values():
            # Figure out the coordinates of the neighbouring cell - the offsets are provided above.
            neighbour = []
            for i in range(len(current_cell)):
                neighbour.append(current_cell[i] + direction[i])
            neighbour = (neighbour[0], neighbour[1])

            # three checks to see if current direction neighbour should be skipped
            if not (0 <= neighbour[0] <= maze_size and 0 <= neighbour[1] <= maze_size):  # if coord is out of bounds
                continue
            if neighbour in g_values:  # if coord already has been checked
                continue
            if maze[neighbour[1]][neighbour[0]] == 'x':
                continue

            cost = g_values[current_cell] + 1
            g_values[neighbour] = cost
            h_score = utils.manhattan_distance(neighbour, goal)
            f_score = h_score + cost

            heapq.heappush(p_queue, (f_score, neighbour))

            predecessors[neighbour] = current_cell
    return None


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path


if __name__ == "__main__":
    maze_map = utils.import_maze("mazes/maze2.txt")     # Change the path as required.
    start = utils.locate(maze_map, 's')
    goal = utils.locate(maze_map, 'g')
    # Print out the path returned by the a_star function (after you have completed it)
    print(a_star(maze_map, start, goal))
