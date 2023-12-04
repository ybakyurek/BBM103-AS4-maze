# Maze Solver

## Introduction
This program is designed to solve mazes represented as text files. It provides solutions for two types of mazes: a regular maze and a maze with health points.

## Prerequisites
- Python 3.x

## How to Use

### 1. Download
Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/maze-solver.git
cd maze-solver
```

### 2. Run the Program

Run the following command to execute the maze solver program:

```bash
python3 maze.py maze.txt maze_health.txt output.txt
```

Make sure to replace `maze.txt`, `maze_health.txt`, and `output.txt` with the actual names of your maze files and the desired output file.



## Program Logic

### Reading the Maze
The program reads the maze configurations from two text files: `maze.txt` and `maze_health.txt`.

`MAZE_HEALTH.TXT`

```plaintext
WPPWWW
WWPWPS
WWPWPW
PPHPPW
FWPWWW
WPPPPW
```

`MAZE.TXT`

```plaintext
WPPWWW
WWPWPS
WWPWPW
PPPPPW
FWPWWW
PPPPPW
```




### Solving the Maze
The regular maze is solved using a recursive algorithm that explores possible paths until it finds the exit. The solution path is then marked in the maze.

### Health Points
In the maze with health points, the program identifies the health position ('H') and marks it in the solution path.

### Writing to Output
The program writes the solution of both mazes to an output file named `output.txt`.

`OUTPUT.TXT`

```plaintext
maze solution
0 0 0 0 0 0 
0 0 0 0 1 S 
0 0 0 0 1 0 
1 1 1 1 1 0 
F 0 0 0 0 0 
0 0 0 0 0 0 
health maze solution
0 0 0 0 0 0 
0 0 0 0 1 S 
0 0 0 0 1 0 
1 1 H 1 1 0 
F 0 0 0 0 0 
0 0 0 0 0 0
```

Feel free to explore and modify the maze files to test different scenarios.

Happy Maze Solving!
