from charlotte import Board;

if __name__ == "__main__":
    board = Board()
    while True:
        print(board)
        row = int(input("Enter row (0-indexed): "))
        col = int(input("Enter column (0-indexed): "))
        if not board.make_move((row, col)):
            break