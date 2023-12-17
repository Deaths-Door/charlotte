from enum import Enum
import math
from typing import Callable

class Symbol(Enum):
    """ 
    Represents the two possible symbols in the game: X and O
    
    Variants:
    - CROSS (str): Symbol for player 1.
    - NAUGHT (str): Symbol for player 2.
    """
    CROSS = "X"
    NAUGHT = "O"

    def other(self) -> "Symbol":
        """
        Returns the opposite symbol of the current symbol.

        Returns:
            Symbol: The opposite symbol of the current symbol
        """
        return Symbol.NAUGHT if self == Symbol.CROSS else Symbol.CROSS

    def __repr__(self) -> str:
        """
        Returns a string representation of the symbol.

        Returns:
            str: The string representation of the symbol
        """
        return self.value

X = Symbol.CROSS
O = Symbol.NAUGHT
E = None

class Move:
    """Represents a move in a Tic-Tac-Toe game."""

    def __init__(self, symbol: Symbol, cords: tuple[int, int]) -> None:
        """
        Initializes a Move instance.

        Args:
            symbol (Symbol): The symbol used for the move
            cords (tuple[int, int]): The coordinates of the position where the move was made
        """
        self.cords = cords
        self.symbol = symbol

class Board:
    """Represents a Tic-Tac-Toe board."""
    
    dimensions: int = 3
    in_row_to_win: int = 3

    def __init__(self, dimensions: int = 3, in_row_to_win: int = 3):
        """
        Initializes a Board instance.

        Args:
            dimensions (int, optional): The dimensions of the board (default: 3)
            in_row_to_win (int, optional): The number of symbols in a row to win (default: 3)
        """

        if in_row_to_win > dimensions: raise ValueError("in_row_to_win cannot be greater then the dimesions of the board")

        self.dimensions : int = dimensions
        self.in_row_to_win : int = in_row_to_win 

        self.board : list[list[Symbol | None]]  = [[None for _ in range(self.dimensions)] for _ in range(self.dimensions)]

        self.current_player = Symbol.CROSS # Player 1 is cross
        self.moves : list[Move] = []

    def move_count(self) -> int:
        """
        Returns the number of moves made on the board.

        Returns:
            int: The number of moves made on the board
        """
        return len(self.moves)

    def is_player1_turn(self) -> bool:
        """
        Checks if it is currently player 1's turn.

        Returns:
            bool: True if it is player 1's turn, False otherwise
        """
        return self.current_player is Symbol.CROSS

    def is_player2_turn(self) -> bool:
        """
        Checks if it is currently player 2's turn.

        Returns:
            bool: True if it is player 2's turn, False otherwise
        """
        return self.current_player is Symbol.NAUGHT


    def is_valid_point(self, cords: tuple[int, int]) -> bool:
        """
        Checks if a given coordinate (x, y) is valid on the board.

        Args:
            cords (tuple[int, int]): The coordinates to check

        Returns:
            bool: True if the coordinates are valid, False otherwise
        """
        x, y = cords
        return 0 <= x < self.dimensions and 0 <= y < self.dimensions

    def symbol_at_position(self, cords: tuple[int, int]) -> Symbol | None:
        """
        Gets the symbol at a given coordinate (x, y) on the board.

        Args:
            cords (tuple[int, int]): The coordinates of the position

        Returns:
            Symbol | None: The symbol at the given position or None if the position is empty

        Raises:
            ValueError: If the coordinates are invalid
        """
        if not self.is_valid_point(cords):
            raise ValueError("Coordinates are not valid")

        x, y = cords
        return self.board[x][y]

    def is_empty_at(self,cords : tuple[int,int]) -> bool :
        """
        Checks if a given position on the board is empty.

        Args:
            cords (tuple[int, int]): The coordinates of the position to check

        Returns:
            bool: True if the position is empty, False otherwise

        Raises:
            ValueError: If the coordinates are invalid
        """
        return self.symbol_at_position(cords) is None

    def has_cross_at(self,cords : tuple[int,int]) -> bool :
        """
        Checks if a given position on the board contains the CROSS symbol.

        Args:
            cords (tuple[int, int]): The coordinates of the position to check

        Returns:
            bool: True if the position contains CROSS, False otherwise

        Raises:
            ValueError: If the coordinates are invalid
        """
        return self.symbol_at_position(cords) is Symbol.CROSS
    
    def has_naught_at(self,cords : tuple[int,int]) -> bool :
        """
        Checks if a given position on the board contains the NAUGHT symbol.

        Args:
            cords (tuple[int, int]): The coordinates of the position to check

        Returns:
            bool: True if the position contains NAUGHT, False otherwise

        Raises:
            ValueError: If the coordinates are invalid
        """
        return self.symbol_at_position(cords) is Symbol.NAUGHT
    
    def valid_moves(self) -> list[tuple[int,int]] : 
        """
        Returns a list of all valid moves on the board.

        A valid move is a position on the board that is not already occupied by a symbol.

        Returns:
            list[tuple[int, int]]: A list of valid move positions
        """
        return [
            (row, col) for row in range(self.dimensions)
            for col in range(self.dimensions)
            if self.board[row][col] is None
        ]
    
    def valid_moves_at_row(self,row : int) -> list[int]:
        """
        Returns a list of all valid moves at a given row of the board.

        A valid move at a row is a position on that row that is not already occupied by a symbol.

        Args:
            row (int): The row index for which to find valid moves

        Returns:
            list[int]: A list of valid move column positions
        """

        return [(col) for col in range(self.dimensions) if self.board[row][col] is None]
    
    def valid_moves_at_col(self,col : int) -> list[int]:
        """
        Returns a list of all valid moves at a given column of the board.

        A valid move at a column is a position on that column that is not already occupied by a symbol.

        Args:
            col (int): The column index for which to find valid moves

        Returns:
            list[int]: A list of valid move row positions
        """
        
        return [(row) for row in range(self.dimensions) if self.board[row][col] is None]
    
    def moves_by(self,symbol : Symbol) -> list[tuple[int,int]] :
        """
            Retrieve all moves made by a specific symbol.

            Args:
                symbol: The symbol to filter moves by. Must be of type `Symbol`.

            Returns:
                A list of tuples representing the coordinates of all moves made by the specified symbol.
        """
        return [move.cords for move in self.moves if move.symbol is symbol]

    def move_by_current_player(self) -> list[tuple[int,int]] :
        """
            Retrieve all moves made by the current player.

            Returns:
                A list of tuples representing the coordinates of all moves made by the current player.
        """
        return self.moves_by(self.current_player)
    
    def switch_players(self) -> None :
        """
        Switch the current player to the other player.

        """
        self.current_player = self.current_player.other()


    def make_move(self,move : Move) -> bool :
        """
        Returns a list of all valid moves on the board.

        A valid move is a position on the board that is not already occupied by a symbol.

        Returns:
            list[tuple[int, int]]: A list of valid move positions
        """
        try :
            if not self.is_valid_point(move.cords) or not self.is_empty_at(move.cords) :
                return False
        except :
            return False
        
        x,y = move.cords
        self.board[x][y] = move.symbol
        self.moves.append(move)

        return True
    
    def make_move_with(self,player : Symbol,cords: tuple[int, int]) -> bool :
        """
        Makes a move on the board with the specified player and coordinates.

        Args:
            player (Symbol): The player to make the move.
            cords (tuple[int, int]): The coordinates of the move.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        return self.make_move(Move(player,cords))
    
    def make_move_with_current_player(self,cords: tuple[int, int]) -> bool : 
        """
        Makes a move on the board with the current player and coordinates.

        Args:
            cords (tuple[int, int]): The coordinates of the move.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        return self.make_move(Move(self.current_player,cords))
    
    def make_move_and_switch(self,move : Move) -> bool :
        """
        Makes a move on the board with the specified move and switches players afterwards.

        Args:
            move (Move): The move to make.

        Returns:
            bool: True if the move was successful, False otherwise.
        """

        t = self.make_move(move)
        if t :
            self.switch_players()
        return t
    
    def make_move_with_and_switch(self,player : Symbol,cords: tuple[int, int]) -> bool :
        """
        Makes a move with the specified player and coordinates, and then switches players afterwards.

        Args:
            player (Symbol): The player to make the move.
            cords (tuple[int, int]): The coordinates of the move.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        t = self.make_move_with(player,cords)
        if t :
            self.switch_players()
        return t

    def make_move_with_current_player_and_switch(self,cords: tuple[int, int]) -> bool :
        """
        Makes a move with the current player and coordinates, and then switches players afterwards.

        Args:
            cords (tuple[int, int]): The coordinates of the move.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        t = self.make_move_with_current_player(cords)
        
        if t :
            self.switch_players()

        return t
    
    def undo_move(self,move : Move) :
        """
        Undoes the specified move by removing the symbol from the board.

        Args:
            move (Move): The Move object to undo
        """
        x,y = move.cords
        self.board[x][y] = None

    def undo_last_move(self) : 
        """Undoes the last move made on the board."""
        self.current_player = self.current_player.other()
        self.undo_move(self.moves.pop())

    def undo_moves(self,moves : list[Move]) :
        """
        Undoes the specified list of moves.

        Args:
            moves (list[Move]): A list of Move objects to undo.
        """
        for move in moves :
            self.undo_move(move)

    def undo_last_moves(self,n : int = 1) :
        """
        Undoes the specified number of moves.

        Args:
            n (int, optional): The number of moves to undo. Defaults to 1.
        """
        for _ in range(n) :
            self.undo_last_move()

    # Can remove all the weird checking
    def __dimesions_equal_in_row_to_win(self,player : Symbol) -> bool:
        # Check horizontal
        for row in self.board:
            if all(symbol == player for symbol in row):
                return True
            

        #Check vertical
        for col in range(self.dimensions) :
            if all(self.board[row][col] == player for row in range(self.dimensions)) :
                return True
            
        # Check diagonals
        return all(self.board[i][i] == player for i in range(self.dimensions))

    def __tougher_check(self,player : Symbol) -> bool :
        #TODO : Replace with real logic
        return False

    def has_won(self,player : Symbol) -> bool :
        """
        Check if the given player has won the game.

        Args:
            player (Symbol): The player to check for victory.

        Returns:
            bool: `True` if the player has won, `False` otherwise.
        """
        return self.__dimesions_equal_in_row_to_win(player) if self.dimensions == self.in_row_to_win else self.__tougher_check(player)

    def has_current_player_won(self) -> bool :
        """
        Check if the current player has won the game.

        Returns:
            bool: `True` if the current player has won, `False` otherwise.
        """
        return self.has_won(self.current_player)
    
    def has_any1_won(self) -> Symbol | None :
        """
        Checks if either player has won the game.

        Returns:
            player : The player who won
        """
        if self.has_won(Symbol.CROSS) :
            return Symbol.CROSS
        
        if self.has_won(Symbol.CROSS) :
            return Symbol.CROSS
        
        return None

    
    def __evaluate_board(self,player : Symbol) -> float : 
        return math.inf if self.has_won(player) else (-math.inf if self.has_won(player.other()) else 0) 

    def __minimax_with_alpha_beta_pruning(
        self,
        final_value : float,
        opposite_maximizing_player : bool,
        player : Symbol,
        possible_moves : list[tuple[int,int]],
        depth : int,
        alpha : float,
        beta : float,
        update_value_condition : Callable[[float,float],bool],
        update_alpha_beta : Callable[[float,float,float],tuple[float,float]]
    ) -> tuple[float,tuple[int,int] | None] :
        final_move = None
        for move in possible_moves :
            self.make_move_with(player,move)
            
            # To figure out how many moves to undo , to keep board same without copying it
           # move_count = self.move_count()
            
            move_value,_ = self.__get_move_for(
                player=player,
                depth=depth - 1,
                maximizing_player=opposite_maximizing_player,
                alpha=alpha,
                beta=beta
            )

           # self.undo_last_moves(self.move_count() - move_count)
            self.undo_last_move()

            if update_value_condition(move_value,final_value) :
                final_value = move_value
                final_move = move

            __a,__b = update_alpha_beta(final_value,alpha,beta)
            alpha = __a
            beta = __b

            if alpha >= beta:
                break

        return final_value , final_move

    def __get_move_for(
        self, 
        player : Symbol,
        depth : int,
        maximizing_player : bool,
        alpha : float = -math.inf,
        beta : float = math.inf
    ) -> tuple[float,tuple[int,int] | None]  : 
        # TODO : Optimze this , as its gonna be last possible moves - movemade
        possible_moves = self.valid_moves()

        if depth == 0 or len(possible_moves) == 1 or (self.has_any1_won() is not None) :
            return self.__evaluate_board(player), None
         
        final_value , update_value_condition , update_alpha_beta = (
            -math.inf,
            lambda mvalue , fvalue :  mvalue > fvalue,
            lambda fvalue , alpha , beta : (max(alpha,fvalue),beta)
        ) if maximizing_player else (
            math.inf,
            lambda mvalue , fvalue :  mvalue < fvalue,
            lambda fvalue , alpha , beta : (alpha,min(beta,fvalue))
        )

        opposite_maximizing_player = not maximizing_player

        return self.__minimax_with_alpha_beta_pruning(
            final_value,
            opposite_maximizing_player,
            player,
            possible_moves,
            depth,
            alpha,
            beta,
            update_value_condition,
            update_alpha_beta
        )

    __optimal_log2 = math.log2(dimensions * in_row_to_win)
    __optimal_depth_for_max_player = math.ceil(__optimal_log2)
    __optimal_depth_for_min_player = math.floor(__optimal_log2) + 1

    def best_move_for(self,player : Symbol,depth : int = __optimal_depth_for_max_player) -> Move | None :
        """
        Finds the best move for the specified player.

        Args:
            player (Symbol): The player for whom to find the best move.
            depth (int, optional): The depth of the search. Defaults to the optimal depth.
        """
        _ , cords = self.__get_move_for(
            player,
            depth,
            maximizing_player=True
        )

        return None if cords is None else Move(player,cords)

    def worst_move_for(self,player : Symbol,depth : int = __optimal_depth_for_min_player) -> Move | None :
        """
        Finds the worst move for the specified player.

        Args:
            player (Symbol): The player for whom to find the worst move.
            depth (int, optional): The depth of the search. Defaults to the optimal depth.
        """
        _ , cords = self.__get_move_for(
            player,
            depth,
            maximizing_player=False
        )

        return None if cords is None else Move(player,cords)

    def best_move_for_current_player(self,depth : int = __optimal_depth_for_max_player) -> Move | None :
        """
        Finds the best move for the current player.

        Args:
            depth (int, optional): The depth of the search. Defaults to the optimal depth.
        """
        return self.best_move_for(self.current_player,depth)

    def worst_move_for_current_player(self,depth : int = __optimal_depth_for_min_player) -> Move | None :
        """
        Finds the worst move for the current player.

        Args:
            depth (int, optional): The depth of the search. Defaults to the optimal depth.
        """
        return self.worst_move_for(self.current_player,depth)

    def __repr_row__(self,row : list[Symbol | None]) -> str : 
       return '|'.join([f" {" " if item is None else item.__repr__()} " for item in row])

    def __repr__(self) -> str:
        divider = (("-" * self.dimensions + "+") * self.dimensions)[:-1]
        
        string = ""
        for row in self.board[:-1] :
            string += f"{self.__repr_row__(row)}\n{divider}\n"

        string += self.__repr_row__(self.board[-1])
        
        return string