from enum import Enum
from collections import deque

# TODO : ADD has won and ai play methods to the board class 

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

        self.board : list[list[Symbol | None]]  = [[None for _ in range(dimensions)] for _ in range(dimensions)]

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

    def make_move_with(self,symbol : Symbol,cords: tuple[int, int]) -> bool :
        """
        Returns a list of all valid moves on the board.

        A valid move is a position on the board that is not already occupied by a symbol.

        Returns:
            list[tuple[int, int]]: A list of valid move positions
        """
        try :
            if not self.is_valid_point(cords) or not self.is_empty_at(cords) :
                return False
        except :
            return False
        
        x,y = cords
        self.board[x][y] = symbol
        self.moves.append(Move(symbol,cords))

        return True
    
    def make_move(self,cords: tuple[int, int]) -> bool :
        """
        Makes a move on the board with the current player's symbol at the specified position.

        Args:
            cords (tuple[int, int]): The coordinates of the position to place the symbol

        Returns:
            bool: True if the move was successful, False if the position was invalid
        """
        temp = self.make_move_with(self.current_player,cords)
        self.current_player = self.current_player.other()
        return temp
    
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

    # TODO : FIX THIS nly works for horizontal
    def has_won(self, player: Symbol) -> bool:
        pass

    def __repr_row__(self,row : list[Symbol | None]) -> str : 
       return '|'.join([f" {" " if item is None else item.__repr__()} " for item in row])

    def __repr__(self) -> str:
        divider = (("-" * self.dimensions + "+") * self.dimensions)[:-1]
        
        string = ""
        for row in self.board[:-1] :
            string += f"{self.__repr_row__(row)}\n{divider}\n"

        string += self.__repr_row__(self.board[-1])
        
        return string