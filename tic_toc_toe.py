from random import randrange


class Player:
    def __init__(self, symbol, is_computer):
        self.symbol = symbol
        self.is_computer = is_computer
        self.symbol_list = {'X': 1, 'O': -1, '_': 0}

    def play(self, board):
        if self.is_computer:
            print('PC Turn')
            global count
            depth = 9 - count
            value, place = self.alpha_beta(board, depth, -10, 10, True)
        else:
            print('your Turn')
            place = int(input('enter a number from 1 to 9: ')) - 1
            while self.is_invalid(board, place):
                place = int(input('enter again: ')) - 1
        board.tiles[int(place / 3)][place % 3] = self.symbol_list[self.symbol]

    def alpha_beta(self, board, depth, alpha, beta, is_max_player):
        value = board.check_if_won()
        if value != 0:
            return value, -1
        if depth == 0:
            return value, -1
        if is_max_player:
            value = -10
            list_of_numbers = list(range(9))
            while list_of_numbers:
                random = list_of_numbers.pop(randrange(len(list_of_numbers)))
                x = int(random / 3)
                y = random % 3
                if board.tiles[x][y] == 0:
                    board.tiles[x][y] = self.symbol_list[players[1].symbol]
                    temp_value = self.alpha_beta(board, depth - 1, alpha, beta, False)[0]
                    if temp_value > value:
                        value = temp_value
                        place = random
                    alpha = max(alpha, value)
                    board.tiles[x][y] = 0
                    if alpha >= beta:
                        break
        else:
            value = 10
            list_of_numbers = list(range(9))
            while list_of_numbers:
                random = list_of_numbers.pop(randrange(len(list_of_numbers)))
                x = int(random / 3)
                y = random % 3
                if board.tiles[x][y] == 0:
                    board.tiles[x][y] = self.symbol_list[players[0].symbol]
                    temp_value = self.alpha_beta(board, depth - 1, alpha, beta, True)[0]
                    if temp_value < value:
                        value = temp_value
                        place = random
                    beta = min(beta, value)
                    board.tiles[x][y] = 0
                    if beta <= alpha:
                        break
        return value, place

    @staticmethod
    def is_invalid(board, place):
        if place not in list(range(9)) or board.tiles[int(place / 3)][place % 3] != 0:
            print('invalid input.')
            return True
        return False


class Board:
    def __init__(self):
        self.tiles = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.symbol_list = {1: 'X', -1: 'O', 0: '_'}

    def __str__(self):
        print_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                print_list[i][j] = self.symbol_list[self.tiles[i][j]]
        return ('\n'.join([''.join(['{:4}'.format(item) for item in row])
                           for row in print_list]))

    def check_if_won(self):
        for i in range(3):
            x, y = 0, 0
            for j in range(3):
                x += self.tiles[i][j]
                y += self.tiles[j][i]
            if x == 3 or y == 3:
                return 1
            if x == -3 or y == -3:
                return -1
        value = self.tiles[1][1]
        if self.tiles[1][1] != 0:
            if (self.tiles[0][0] == value and self.tiles[2][2] == value) or (
                    self.tiles[0][2] == value and self.tiles[2][0] == value):
                return value
        return 0


print("you play first")
players = [Player('O', False), Player('X', True)]
turn = 0
count = 0
who_won = False
board = Board()
while not who_won:
    print(board)
    players[turn].play(board)
    who_won = board.check_if_won()
    turn = 1 - turn
    count += 1
    if count == 9:
        break
print(board)
if who_won == 1:
    print("\033[91m" + "You lose")
elif who_won == -1:
    print("\033[92m" + "You Win")
else:
    print("\033[93m" + "Draw")
