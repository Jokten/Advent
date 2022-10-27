import numpy as np


class bingo:
    def __init__(self, numbers):
        self.wins = np.zeros((5, 5), int)
        self.board = np.matrix(numbers)
        self.winner = 0

    def find_val(self, val):
        cord = np.where(self.board == val)
        if cord[0].size != 0:
            row = cord[0][0]
            col = cord[1][0]
            return [row, col]

    def check_board(self, val):
        win_cord = self.find_val(val)
        if win_cord is not None:
            self.wins[win_cord[0], win_cord[1]] = 1

    def check_win(self):
        if np.any(np.all(self.wins, axis=0)) or np.any(np.all(self.wins, axis=1)):
            return 1


def sum_board(board, wins):
    sum = 0
    for i in range(5):
        for j in range(5):
            if wins[i, j] == 0:
                sum += board[i, j]
    return sum


def find_boards(lista):
    boards = []
    board = []
    for i in lista:
        if i != '':
            board.append(list(map(int, i.split())))
        else:
            boards.append(board)
            board = []
    return boards


def main():
    with open('input.txt', 'r') as file:
        ran_num = file.readline()
        next(file)
        data = file.read().splitlines()
    num_board = find_boards(data)
    boards = [bingo(i) for i in num_board]
    num = list(map(int, ran_num.split(',')))

    winner = 0
    n = 0
    while winner == 0:
        current = num[n]
        for i in boards:
            i.check_board(current)
            if i.check_win():
                winner = 1
                win_board = i
                final = num[n]
        n += 1
    print(sum_board(win_board.board, win_board.wins) * final)


if __name__ == '__main__':
    main()
