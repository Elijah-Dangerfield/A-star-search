import sys, random

if len(sys.argv) != 3:
    print()
    print("Usage: %s [seed] [number of random moves]" % (sys.argv[0]))
    print()
    sys.exit(1)


def main():
    board = [[int(n) for n in line.split()] for line in sys.stdin]

    random.seed(int(sys.argv[1]))
    number_of_moves = int(sys.argv[2])
    prev = (0, 0)

    for x in range(number_of_moves):
        move = random.randrange(4)
        prev = move_board(prev, board, move)

    print_board(board)


def print_board(board): print('\n'.join([' '.join([str(cell) for cell in row]) for row in board]))


def move_board(prev, board, num):
    # 0,1,2,3 up, left, right, down respectively
    # so you would want to take the 0 and swap it with the respective element

    row = prev[0]
    col = prev[1]

    if num == 0:
        # swapping with up
        if row - 1 >= 0:
            temp = board[row - 1][col]
            board[row - 1][col] = 0
            board[prev[0]][prev[1]] = temp
            prev = (row - 1, col)

    if num == 1:
        # swapping with left
        if col - 1 >= 0:
            temp = board[row][col - 1]
            board[row][col - 1] = 0
            board[prev[0]][prev[1]] = temp
            prev = (row, col - 1)

    if num == 2:
        # swapping with right
        if col + 1 <= 2:
            temp = board[row][col + 1]
            board[row][col + 1] = 0
            board[prev[0]][prev[1]] = temp
            prev = (row, col + 1)

    if num == 3:
        # swapping with down
        if row + 1 <= 2:
            temp = board[row + 1][col]
            board[row + 1][col] = 0
            board[prev[0]][prev[1]] = temp
            prev = (row + 1, col)

    return prev


if __name__ == '__main__':
    main()
