# TODO : Keep this until charloote lib is not published, then remove it 
import os
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
    n = int(input("Enter the number of 'symbols' in row to win (default is 3)"))
    if n < dimensions :
        print(f"Invalid number , please enter a number >= {n}")
        return get_in_row_to_win(dimensions)
    
    return n

def get_undo_option():
    undo_option = input("Would you like to enable undo support (y/n)? ")
    if undo_option.lower() not in ["y", "n"]:
        print("Invalid input. Please enter 'y' or 'n'.")
        return get_undo_option()
    return undo_option.lower() == "y"

def input_coords(board : Board,coords) :
    try:
        row, col = coords.split(",")
        row = int(row)
        col = int(col)

        print("Move made successfully." if board.make_move((row, col)) else "Invalid coordinates. Please enter a valid coordinate.")
    except ValueError:
        print("Invalid input. Please enter a valid coordinate string, separated by a comma.")
        
def main() :
    dimensions = get_grid_dimensions()
    in_row_to_win = get_in_row_to_win(dimensions)
    enable_undo = get_undo_option()
    board = Board(dimensions,in_row_to_win)

    while True :
        print(board)
        
        #TODO : Check if it is solved and show who in the hell won
        action = input("What would you like to do?\n(1) Make a move (Enter coordinates)\n(2) Undo a move\n(3) Quit\n")
        
        match action :
            case "quit" : exit(0)
            case "undo" : 
                if enable_undo : 
                    board.undo_last_move()
                    continue
                
                print("Undo is currently disabled.")
            case _ : input_coords(board,coords=action)


if __name__ == "__main__": main()