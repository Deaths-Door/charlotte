from charlotte import Symbol, Board;


def is_vertical_or_horizontal(board : Board) : 
    row = 1
    riter_index = 0
    # Stop if row is last
    while row != board.dimensions :
        r = row + riter_index
        if board.board[r - 1][0] == board.board[r][0] :
            riter_index += 1
        else :
            row += 1
        pass
    pass


board = Board(dimensions=3,in_row_to_win=3)
board.board = [
    [Symbol.CROSS,Symbol.CROSS,Symbol.CROSS],
    [Symbol.NAUGHT,None,Symbol.NAUGHT],
    [None,Symbol.NAUGHT,None],
]

is_vertical_or_horizontal(board)