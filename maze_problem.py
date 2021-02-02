class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.visited = [[False for i in range(len(maze[1]))] for j in range(len(maze))]
        self.heuristics = [[None for i in range(len(maze[1]))] for j in range(len(maze))]
        self.moves = [[0 for i in range(len(maze[1]))] for j in range(len(maze))]
        self.dest = (len(maze)-1, len(maze)-1)
        self.current_x = 0
        self.current_y = 0

    def get_heuristic(self, x, y, ):
        if x >= 0 and y < len(self.maze) and y >= 0 and x < len(self.maze) and self.maze[x][y] == 0:
            if not self.heuristics[x][y]:
                if not self.moves[x][y]:
                    self.moves[x][y] = self.moves[self.current_x][self.current_y] + 1
                self.heuristics[x][y] = self.dest[0] - x + self.dest[1] - y + self.moves[x][y]
            return self.heuristics[x][y], x, y
        return None

    def a_star(self):
        print(self)
        if (self.current_x, self.current_y) == self.dest:
            print("\033[92m" + "Win" + "\033[0m")
            return True
        next_moves = [i for i in [self.get_heuristic(self.current_x + 1, self.current_y),
                                  self.get_heuristic(self.current_x - 1, self.current_y),
                                  self.get_heuristic(self.current_x, self.current_y + 1),
                                  self.get_heuristic(self.current_x, self.current_y - 1)] if i]
        self.visited[self.current_x][self.current_y] = True
        if not next_moves:
            return False
        min = 9999
        next_x = None
        next_y = None
        for i in next_moves:
            if i[0] <= min and not self.visited[i[1]][i[2]]:
                min = i[0]
                next_x = i[1]
                next_y = i[2]
        if isinstance(next_x, int):
            for i in next_moves:
                if i[1] != next_x and i[2] != next_y:
                    self.visited[i[1]][i[2]] = True
        else:
            # if len(next_moves) == 1:
            #     self.maze[next_moves[0][1]][next_moves[0][2]] = 1
            #     next_x = self.current_x
            #     next_y = self.current_y
            # else:
                for i in next_moves:
                    if i[0] <= min:
                        min = i[0]
                        next_x = i[1]
                        next_y = i[2]
                self.maze[self.current_x][self.current_y] = 1
        self.current_x = next_x
        self.current_y = next_y
        return self.a_star()

    def run(self):
        is_done = self.a_star()
        if not is_done:
            print("\033[91m" + "Unsuccessful" + "\033[0m")

    def __str__(self):
        print_maze = [row[:] for row in self.maze]
        print_maze[self.current_x][self.current_y] = 4
        return ('\n'.join([''.join(['{:4}'.format(item) for item in row])
                           for row in print_maze])) + '\n'


# Example 1
# maze_1 = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#           [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
#           [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
#           [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0],
#           [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
#           [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
#           [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
#           [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#           [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
#           [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
#           [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
#           [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0],
#           [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
#           [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
#           [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#           [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0], ]

maze_1 = [[0, 0, 0, 0, 0, 1, 0, 1, 0],
          [0, 1, 1, 1, 1, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 0, 1, 0],
          [0, 1, 1, 1, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 1, 0],
          [1, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 1, 0, 1, 0]]
Maze(maze_1).run()
