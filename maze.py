# Assignment4
# student: Yildirim Bayazit Akyurek
# number : 21904343
# section: BBM103-1

import os
import sys

# Command-line arguments
maze_text = sys.argv[1]
health_maze_text = sys.argv[2]
outputFile = sys.argv[3]

# Function to read the maze from a file
def read_maze(filename):
    maze = []
    with open(filename, "r") as f:
        for line in f:
            row = [item for item in line if item != "\n"]
            maze.append(row)
    return maze

# Function to print the maze
def print_maze(maze):
    for row in maze:
        for item in row:
            print(item, end=" ")
        print()

# Function to find the position of a specific point in the maze
def find_point_position(maze, point):
    coordinate = {"row": 0, "col": 0}
    for i, row in enumerate(maze):
        for j, item in enumerate(row):
            if item == point:
                coordinate["row"] = i
                coordinate["col"] = j
    return coordinate

# Function to create a 2D list with zeros
def path_list(r, c):
    liste = [[0 for _ in range(c)] for _ in range(r)]
    return liste

# Recursive function to solve the maze
def solve_maze(maze, road, r, c):
    road[r][c] = 1

    if maze[r][c] == 'F':
        return road

    # Move left
    if c > 0 and maze[r][c - 1] != 'W' and road[r][c - 1] == 0:
        return solve_maze(maze, road, r, c - 1)

    # Move right
    if c < len(maze[0]) - 1 and maze[r][c + 1] != 'W' and road[r][c + 1] == 0:
        return solve_maze(maze, road, r, c + 1)

    # Move up
    if r > 0 and maze[r - 1][c] != 'W' and road[r - 1][c] == 0:
        return solve_maze(maze, road, r - 1, c)

    # Move down
    if r < len(maze) - 1 and maze[r + 1][c] != 'W' and road[r + 1][c] == 0:
        return solve_maze(maze, road, r + 1, c)

# Main part of the code

# Read and solve the first maze
maze1 = read_maze(maze_text)
row_size1 = len(maze1)
column_size1 = len(maze1[0])
path_list1 = path_list(row_size1, column_size1)

start1 = find_point_position(maze1, "S")
finish1 = find_point_position(maze1, "F")

r1 = start1["row"]
c1 = start1["col"]

solving_road1 = solve_maze(maze1, path_list1, r1, c1)
path_list1[r1][c1] = 'S'
path_list1[finish1["row"]][finish1["col"]] = 'F'

# Read and solve the health maze
maze2 = read_maze(health_maze_text)
row_size2 = len(maze2)
column_size2 = len(maze2[0])
path_list2 = path_list(row_size2, column_size2)

start2 = find_point_position(maze2, "S")
finish2 = find_point_position(maze2, "F")

r2 = start2["row"]
c2 = start2["col"]

solving_road2 = solve_maze(maze2, path_list2, r2, c2)
path_list2[r2][c2] = 'S'
path_list2[finish2["row"]][finish2["col"]] = 'F'

# Write to the output file
with open(outputFile, 'w') as file:
    first_stdout = sys.stdout
    sys.stdout = file

    # Maze 1
    print('maze solution')
    for row in path_list1:
        for item in row:
            print(item, end=" ")
        print()

    # Health Maze
    health_position = find_point_position(maze2, 'H')
    path_list2[health_position['row']][health_position['col']] = 'H'
    print('health maze solution')
    for row in path_list2:
        for item in row:
            print(item, end=" ")
        print()

    sys.stdout = first_stdout
