import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from charlotte import Symbol, Board ,X , E,O;

"""
## Note 

Ensure any changes here are reflected in the charlotte.Board.has_won group of functions
"""

# TODO , allow maybe return range / location where it won

def is_vertical(board : Board,player : Symbol) -> bool :
    # So its avoided
    if board.in_row_to_win == board.dimensions : 
        return board.has_won(player) 
    
    ROW_DEFAULT = 0
    row = ROW_DEFAULT
    col = 0

    IN_ROW_DEFAULT = 1
    in_row_till_now = IN_ROW_DEFAULT

    while col < board.dimensions :
        #TODO : Maybe can optimize by checking if at point where a win is not possible eg dimensions/3 = 1.5 so 2nd square and then if its X or empty then O can't win , can technically drastically cut down on number of iters posssible  but not in cases like dimesinos = 5 and inrowtowin = 2 then no point
        if board.board[row][col] == player :
            in_row_till_now += 1

        row += 1

        # means we've reach end of the colum so check next one
        if not row < board.dimensions - 2 :
            col += 1 
            row = ROW_DEFAULT
            in_row_till_now = IN_ROW_DEFAULT

        if in_row_till_now == board.in_row_to_win:
            return True    
    return False

def is_horizontal(board : Board,player : Symbol) -> bool :
    # So its avoided
    if board.in_row_to_win == board.dimensions : 
        return board.has_won(player) 

    COL_DEFAULT = 0
    col = COL_DEFAULT
    row = 0

    IN_ROW_DEFAULT = 1
    in_row_till_now = IN_ROW_DEFAULT

    while row < board.dimensions :
        #TODO : Maybe can optimize by checking if at point where a win is not possible eg dimensions/3 = 1.5 so 2nd square and then if its X or empty then O can't win , can technically drastically cut down on number of iters posssible  but not in cases like dimesinos = 5 and inrowtowin = 2 then no point
        if board.board[row][col] == player :
            in_row_till_now += 1

        col += 1

        # means we've reach end of the column so check next one
        if not col < board.dimensions - 1 :
            row += 1 
            col = COL_DEFAULT
            in_row_till_now = IN_ROW_DEFAULT

        if in_row_till_now == board.in_row_to_win:
            return True 

    return False

"""
def setup_board(grid : list[list[Symbol | None]],dimensions : int,in_row_to_win : int) -> Board :
    board = Board(dimensions,in_row_to_win)
    board.board = grid
    return board

board = setup_board([
    [E, E, E, E, E],
    [E, O, E, E, E],
    [E, O, E, E, E],
    [E, O, E, E, E],
    [E, O, E, E, E],
],5,4)

#assert is_vertical(board,O) is True
"""
"""board = setup_board([
    [E, O, X, X, X, X],
    [E, E, O, E, E, E],
    [E, E, O, E, E, E],
    [E, E, X, E, E, E],
    [E, E, E, E, E, E],
],5,3)

assert is_vertical(board,O) == False
"""
"""

board = Board(dimensions=3,in_row_to_win=3)


def update(expected,new_board) :
    board.board = new_board
    print(f"Expected {expected}, but got {is_vertical(board,Symbol.NAUGHT)}")

update(
    True,
    [
        [Symbol.CROSS,Symbol.NAUGHT,Symbol.NAUGHT],
        [Symbol.CROSS,None,Symbol.NAUGHT],
        [Symbol.NAUGHT,None,Symbol.NAUGHT],
    ]
)"""