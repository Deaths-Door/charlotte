import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from charlotte import Symbol, Board;

# TODO , allow maybe return range / location where it won
def is_vertical(board : Board,player : Symbol) -> bool :
    ROW_DEFAULT = 0
    row = ROW_DEFAULT
    col = 0

    IN_ROW_DEFAULT = 1
    in_row_till_now = IN_ROW_DEFAULT

    while col < board.dimensions :
        #TODO : Maybe can optimize by checking if at point where a win is not possible eg dimensions/3 = 1.5 so 2nd square and then if its X or empty then O can't win , can technically drastically cut down on number of iters posssible  but not in cases like dimesinos = 5 and inrowtowin = 2 then no point
        if board.board[row][col] == player :
            in_row_till_now += 1
        else :
            #in_row_till_now = IN_ROW_DEFAULT
            row += 1

        # means we've reach end of the colum so check next one
        if not row < board.dimensions - 2 :
            col += 1 
            row = ROW_DEFAULT
            in_row_till_now = IN_ROW_DEFAULT

        if in_row_till_now == board.in_row_to_win:
            return True    
    return False

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