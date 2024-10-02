import pathfinding
import utils


def display_map(maze):
    for row in maze:
        for col in row:
            print(f"{col} ", end="")
        print()


def show_path(maze, path):
    path = path[1:-1]
    for row in range(len(maze)):
        for col in range(len(maze)):
            current = (col, row)
            if current in path:
                print("- ", end="")
            else:
                print(f"{maze[row][col]} ", end="")
        print()


if __name__ == "__main__":
    maze_map = utils.import_maze("mazes/maze2.txt")
    start = utils.locate(maze_map, 's')
    goal = utils.locate(maze_map, 'g')
    display_map(maze_map)
    show_path(maze_map, pathfinding.a_star(maze_map, start, goal))