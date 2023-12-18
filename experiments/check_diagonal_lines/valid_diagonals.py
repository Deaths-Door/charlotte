import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from charlotte import Symbol, Board,E,O,X;

def is_diagonal_win(self: Board, player: Symbol) -> bool:
    # Check for win on primary diagonal
    for i in range(self.dimensions) :
        if __is_diagonal_win(self, player, i):
            return True
   
    # Check for win on secondary diagonal (top right to bottom left)
        
    for i in range(self.dimensions) :
        if __is_diagonal_win(self, player, (self.dimensions - 1) - i):
            return True
        
  #  for i in range(self.dimensions):
       # secondary_diagonal_indices.append((self.dimensions - 1) - i)
    #if __is_diagonal_win(self, player, secondary_diagonal_indices):
      #  return True

    # Check for win on tertiary diagonal (bottom right to top left)
        
    for i in reversed(range(self.dimensions)) :
        if __is_diagonal_win(self, player,i):
            return True
        

   # tertiary_diagonal_indices = list(reversed(range(self.dimensions)))
   # if __is_diagonal_win(self, player, tertiary_diagonal_indices):
    #    return True

    return False

def __is_diagonal_win(self: Board,player: Symbol, diagonal_index: int = 0) -> bool:
    """
    Checks for a win on any diagonal for the given player.

    Args:
        player (Symbol): The player to check for victory.
        diagonal_index (int): The index of the diagonal to check (0 for primary, 1 for secondary, etc.).

    Returns:
        bool: `True` if the player has won on the specified diagonal, `False` otherwise.
    """

    if diagonal_index < 0 or diagonal_index >= self.dimensions:
        raise ValueError(f"Invalid diagonal index {diagonal_index} for board size {self.dimensions}")

    current_row = 0
    current_col = diagonal_index
    in_row_till_now = 1

    while current_row < self.dimensions and current_col < self.dimensions:
        if self.board[current_row][current_col] == player:
            in_row_till_now += 1

            if in_row_till_now == self.in_row_to_win:
                return True
        else:
            in_row_till_now = 1

        current_row += 1
        current_col += (diagonal_index + 1) if diagonal_index % 2 == 0 else (diagonal_index - 1)

    return False
def setup_board(grid : list[list[Symbol | None]],dimensions : int,in_row_to_win : int) -> Board :
    board = Board(dimensions,in_row_to_win)
    board.board = grid
    return board


board = setup_board([
    [E, O, X],
    [E, X, E],
    [X, O, X],
],3,3)

assert is_diagonal_win(board,X) is True