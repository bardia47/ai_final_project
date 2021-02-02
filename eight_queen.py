import random, math
import decimal


class Board:
    def __init__(self):
        self.queens = [-1 for i in range(0, 8)]
        for i in range(0, 8):
            self.queens[i] = random.randint(0, 7)

    def calculate_cost(self):
        threat = 0
        for queen in range(0, 8):
            for next_queen in range(queen + 1, 8):
                if self.queens[queen] == self.queens[next_queen] or abs(queen - next_queen) == abs(
                        self.queens[queen] - self.queens[next_queen]):
                    threat += 1
        return threat

    def __str__(self):
        board_string = ""
        for row, col in enumerate(self.queens):
            for num in range(0, col):
                board_string += ". "
            board_string += "Q"
            for num in range(col + 1, 8):
                board_string += ". "
            board_string += "\n"
        return board_string

    def make_move(self):
        while True:
            random_x = random.randint(0, 7)
            random_y = random.randint(0, 7)
            if self.queens[random_x] != random_y:
                self.queens[random_x] = random_y
                break


class SimulatedAnnealing:
    def __init__(self, board):
        self.board = board

    def run(self):
        success = False
        t = 0
        while True:
            can_move = False
            tmp = Board()
            tmp.queens = self.board.queens[:]
            tmp.make_move()
            dw = self.board.calculate_cost() - tmp.calculate_cost()
            if dw >= 0:
                can_move = True
            else:
                t += 1
                exp = math.e ** (dw * t)
                print(exp)
                if exp > random.uniform(0, 1):
                    can_move = True
            if can_move:
                print("\033[93m" + "Make Move" + "\033[0m")
                self.board.queens = tmp.queens
                print(self.board)
                if self.board.calculate_cost() == 0:
                    print("\033[92m" + "Solution:" + "\033[0m")
                    print(self.board)
                    success = True
                    break
            elif t == 200:
                 break

        if not success:
            print("\033[91m" + "Unsuccessful" + "\033[0m")


board = Board()
print("Board:")
print(board)
SimulatedAnnealing(board).run()
