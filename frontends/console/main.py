# TODO : Keep this until charloote lib is not published, then remove it 
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from charlotte import Board , Symbol;

def get_grid_dimensions():
    while True:
        try:
            grid_size = int(input("Enter the grid dimensions (n x n) , (defaults to 3 x 3): "))
            if grid_size < 3 :
                raise ValueError()
        except ValueError:
            print("Invalid grid size. Please enter a grid size of at least 3.")
            continue
        else:
            return grid_size

def get_in_row_to_win(dimensions) :
    while True:
        try:
            n = int(input("Enter the number of 'symbols' in row to win (default is 3): "))
            if n > dimensions and n != 1:
                raise ValueError()
        except ValueError:
            print("Invalid input, please enter a valid integer")
            continue
        else:
            return n

def get_ja_nein_response(prompt):
    while True:
        try:
            op = input(f"{prompt} (y/n)? ")
            if op.lower() not in ["y", "n"]:
                raise ValueError()
        except ValueError:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        else:
            return op.lower() == "y"    

def input_coordinates(board : Board,player_symbol,string) :
    try :
        row, col = string.split(",")
        row = int(row)
        col = int(col)
    
        successful_move(board,player_symbol,board.make_move_with_current_player_and_switch((row,col)))
        pass 
    except ValueError:
        print("Invalid input. Please enter a valid coordinate string, separated by a comma.")

def successful_move(board,player_symbol,successful) : 
    if successful :
        print("Move made successfully.")
        check_for_wins(board,player_symbol)
        return
    
    print("Invalid coordinates. Please enter a valid coordinate.")

def check_for_wins(board : Board,player_symbol) :
    winner = board.has_any1_won()

    if winner is not None :
        print(board)
        print("You have won!" if player_symbol == winner else "Sorry , but you lost!")
        exit(0)

def main() :
    dimensions = get_grid_dimensions()
    in_row_to_win = get_in_row_to_win(dimensions)
    is_single_player = get_ja_nein_response("Would you like to player in single player mode")

    player_symbol = (Symbol.CROSS if get_ja_nein_response("Would you like to be player 1 (X)?") else Symbol.NAUGHT) if is_single_player else None
    enable_undo = get_ja_nein_response("Would you like to enable undo support")
    board = Board(dimensions,in_row_to_win)


    while True :
        print(board)

        # AI only there in is_single_player 
        # Opposite of human player
        is_ai_turn = is_single_player and player_symbol != None and board.current_player != player_symbol
        print(f"is_ai_turn = {is_ai_turn}")
        print(f"board.current_player = {board.current_player}")
        if is_ai_turn :
            move = board.best_move_for_current_player()
            if move is not None : 
               successful_move(board,player_symbol,board.make_move_and_switch(move)) 
            continue
            
        action = input(
            "What would you like to do?\n" +
            "(coords) Make a move (Enter coordinates)\n" + 
            ("(undo) Undo a move\n" if enable_undo else "") + 
            "(quit) Quit\n"
        )

        match action :
            case "quit" : exit(0)
            case "undo" : 
                if enable_undo : 
                    if len(board.moves) == 0 :
                        print("Note: Can not undo no moves")
                        continue

                    board.undo_last_move()
                    continue
                
                print("Undo is currently disabled.")
            case _ : input_coordinates(board,player_symbol,action)

if __name__ == "__main__": main()