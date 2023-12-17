import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from charlotte import Symbol, Board;

def __vertical(board : Board) :
    row = 1
    col = 0
    riter_index = 0
    # Stop if row is last
    while col < board.dimensions :
        r = row + riter_index
        if board.board[r - 1][col] == board.board[r][col] :
            riter_index += 1
        else :
            row += 1

        if not row < board.dimensions - 1 :
            col += 1
            row = 0
            riter_index = 0

        if riter_index == board.in_row_to_win - 1:
            return True
    
    return False

def __horizontal(board : Board) :
    col = 1
    row = 0
    citer_index = 0

    while row < board.dimensions: 
        c = col + citer_index
        if board.board[row][c - 1] == board.board[row][c] :
            citer_index += 1
        else :
            col += 1

        if not col < board.dimensions - 1 :
            row += 1
            col = 0
            citer_index = 0
        
        if citer_index == board.in_row_to_win - 1:
            return True
    
    return False


def is_vertical_or_horizontal(board : Board) : 
    return __vertical(board) #or __horizontal(board)

def update(expected,new_board) :
    board.board = new_board
    print(f"Expected {expected}, but got {is_vertical_or_horizontal(board)}")


board = Board(dimensions=3,in_row_to_win=3)

# Checks vertical wins
update(
    True,
    [
        [Symbol.CROSS,Symbol.NAUGHT,Symbol.NAUGHT],
        [Symbol.CROSS,None,Symbol.NAUGHT],
        [Symbol.NAUGHT,None,Symbol.NAUGHT],
    ]
)

update(
    False,
    [
        [Symbol.CROSS,Symbol.CROSS,Symbol.NAUGHT],
        [Symbol.CROSS,Symbol.CROSS,Symbol.CROSS],
        [Symbol.NAUGHT,Symbol.CROSS,Symbol.NAUGHT],
    ]
)

update(
    True,
    [
        [Symbol.CROSS,Symbol.CROSS,Symbol.NAUGHT],
        [Symbol.CROSS,Symbol.NAUGHT,Symbol.CROSS],
        [Symbol.CROSS,Symbol.CROSS,Symbol.NAUGHT],
    ]
)

board.dimensions = 4

update(
    True,
    [
        [Symbol.CROSS,None          ,Symbol.CROSS ,None],
        [None        ,Symbol.NAUGHT,Symbol.NAUGHT,None],
        [Symbol.CROSS,None         ,Symbol.NAUGHT,None],
        [None        ,Symbol.CROSS ,Symbol.NAUGHT,None],
    ]
)

update(
    False,
    [
        [Symbol.CROSS,None         ,Symbol.CROSS ,None],
        [None        ,Symbol.NAUGHT,Symbol.NAUGHT,None],
        [Symbol.CROSS,None         ,Symbol.CROSS ,None],
        [None        ,Symbol.CROSS ,Symbol.NAUGHT,None],
    ]
)