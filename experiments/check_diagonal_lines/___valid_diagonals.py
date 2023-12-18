import os
from re import L
import sys
sys.path.insert(0, os.path.abspath('.'))

from charlotte import Symbol, Board,E,O,X;

# USELESS 
# USELESS

def get_diagonal_coords(self: Board, player: Symbol | None, length: int) -> list[tuple[int, int]]:
    # Check for win on primary diagonal
    primary_diagonal_indices = []
    index = 0
    while index < self.dimensions and len(primary_diagonal_indices) < length:
        if index < length:
            primary_diagonal_indices.append(index)
        index += 1

    primary_diagonal_coords = []
    if len(primary_diagonal_indices) >= length:
        for i in range(length):
            primary_diagonal_coords.append((primary_diagonal_indices[i], i))

    # Check for win on secondary diagonal (top right to bottom left)
    secondary_diagonal_indices = []
    index = self.dimensions - 1
    while index >= 0 and len(secondary_diagonal_indices) < length:
        if index >= length:
            secondary_diagonal_indices.append(index)
        index -= 1

    secondary_diagonal_coords = []
    if len(secondary_diagonal_indices) >= length:
        for i in range(length):
            secondary_diagonal_coords.append((index, i))

    # Check for win on tertiary diagonal (bottom right to top left)
    tertiary_diagonal_indices = []
    index = self.dimensions - 1
    while index >= length - 1 and len(tertiary_diagonal_indices) < length:
        if index >= length - 1:
            tertiary_diagonal_indices.append(index)
        index -= 1

    tertiary_diagonal_coords = []
    if len(tertiary_diagonal_indices) >= length:
        for i in range(length):
            tertiary_diagonal_coords.append((i, index))

    return primary_diagonal_coords + secondary_diagonal_coords + tertiary_diagonal_coords


board = Board(dimensions=5,in_row_to_win=3)

print(get_diagonal_coords(board,None,board.in_row_to_win))