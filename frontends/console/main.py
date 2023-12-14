# TODO : Keep this until charloote lib is not published, then remove it 
import os
from symtable import Symbol
import sys
sys.path.insert(0, os.path.abspath('.'))

from charlotte import Board;

def get_grid_dimensions():
    grid_size = int(input("Enter the grid dimensions (n x n) , (defaults to 3 x 3): "))
    if grid_size < 3:
        print("Invalid grid size. Please enter a grid size of at least 3.")
        return get_grid_dimensions()
    return grid_size

def get_in_row_to_win(dimensions) :
    n = int(input("Enter the number of 'symbols' in row to win (default is 3): "))
    if n < dimensions :
        print(f"Invalid number , please enter a number >= {n}")
        return get_in_row_to_win(dimensions)
    
    return n

def get_ja_nein_response(prompt):
    op = input(f"{prompt} (y/n)? ")
    if op.lower() not in ["y", "n"]:
        print("Invalid input. Please enter 'y' or 'n'.")
        return get_ja_nein_response(prompt)
    return op.lower() == "y"

def successful_move(successful) : 
    print("Move made successfully." if successful else "Invalid coordinates. Please enter a valid coordinate.")

def player_wins(board) :
    if board.has_won(board.current_player.other()) :
        print(f"{board.current_player} wins")
        print(board)
        exit(0)

def input_coords(board : Board,coords) :
    try:
        row, col = coords.split(",")
        row = int(row)
        col = int(col)

        successful_move(board.make_move((row, col)))
        player_wins(board)
    except ValueError:
        print("Invalid input. Please enter a valid coordinate string, separated by a comma.")

def ai_moves(board) :
    #TODO  
    #successful_move(board.make_move((row, col)))
        #player_wins(board)

    pass

def main() :
    dimensions = get_grid_dimensions()
    in_row_to_win = get_in_row_to_win(dimensions)
    is_single_player = get_ja_nein_response("Would you like to player in single player mode")
    enable_undo = get_ja_nein_response("Would you like to enable undo support")
    board = Board(dimensions,in_row_to_win)

    while True :
        print(board)
    
        action = input(f"What would you like to do?\n{"" if is_single_player else "(coords) Make a move (Enter coordinates)\n"}(undo) Undo a move\n(quit) Quit\n")

        match action :
            case "quit" : exit(0)
            case "undo" : 
                if enable_undo : 
                    board.undo_last_move()
                    continue
                
                print("Undo is currently disabled.")
            case _ : (print("Note: Do not enter the coordinates in a single player game"),ai_moves(board)) if is_single_player else input_coords(board,coords=action)

if __name__ == "__main__": main()