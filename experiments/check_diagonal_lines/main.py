import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from charlotte import Symbol, Board,E,O,X;

from collections import defaultdict


def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))

def check_consecutive(nums, x):
    for i in range(len(nums) - x + 1):
        if all(nums[i] == nums[i + j] for j in range(x)):
            return True
    return False

def is_diagonal_win(self: Board, player: Symbol) -> bool :
    return __is_diagonal_win(self,player,lambda x, y: x + y) or __is_diagonal_win(self,player,lambda x, y: x - y)
def __is_diagonal_win(self: Board, player: Symbol,closure) -> bool :
    for item in groups(self.board,closure) :
        __len = len(item)
        if __len < self.in_row_to_win :
            continue
        
        if __len == self.in_row_to_win :
            if all([i == player for i in item]) :
                return True
        
        if check_consecutive(item,self.in_row_to_win) :
            return True

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