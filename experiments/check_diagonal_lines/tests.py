import unittest

import os
import sys
sys.path.insert(0, os.path.abspath("."))
from charlotte import Board,Symbol, X , O , E

from experiments.check_diagonal_lines.main import is_diagonal_win;



def setup_board(grid : list[list[Symbol | None]],dimensions : int,in_row_to_win : int) -> Board :
    board = Board(dimensions,in_row_to_win)
    board.board = grid
    return board

class TestDiagonalWins(unittest.TestCase) :
    def test_diagonal_win_primary_3x3(self):
        board = setup_board([
            [X, O, X],
            [X, X, O],
            [O, O, X]
        ], 3, 3)
        self.assertTrue(is_diagonal_win(board, player=X))

    def test_diagonal_win_secondary_3x3(self):
        board = setup_board([
            [O, X, O],
            [X, X, X],
            [X, O, O]
        ], 3, 3)
        self.assertFalse(is_diagonal_win(board, player=X))

    def test_diagonal_win_no_win_3x3(self):
        board = setup_board([
            [O, O, O],
            [O, X, X],
            [X, X, O],
        ], 3, 3)
        self.assertFalse(is_diagonal_win(board, player=X))

    # Test cases for 5x5 board

    def test_diagonal_win_primary_5x5_in_row_to_win_3(self):
        board = setup_board([
            [X, O, X, O, X],
            [O, X, O, X, O],
            [O, O, O, O, O],
            [O, X, X, X, X],
            [X, O, O, X, O]
        ], 5, 3)
        self.assertTrue(is_diagonal_win(board, player=X))

    def test_diagonal_win_secondary_5x5_in_row_to_win_3(self):
        board = setup_board([
            [O, O, O, O, O],
            [X, X, X, X, X],
            [O, X, O, O, O],
            [X, O, O, X, O],
            [O, O, O, X, O]
        ], 5, 3)
        self.assertTrue(is_diagonal_win(board, player=X))

    def test_diagonal_win_in_row_to_win_4_5x5(self):
        board = setup_board([
            [O, O, O, X, O],
            [X, X, X, X, O],
            [O, X, O, X, O],
            [X, O, O, O, O],
            [O, O, O, O, X]
        ], 5, 4)
        self.assertTrue(is_diagonal_win(board, player=X))


    def test_diagonal_win_no_win_5x5(self):
        board = setup_board([
            [O, O, O, O, O],
            [O, O, X, X, O],
            [X, X, X, O, O],
            [O, X, X, O, X],
            [O, O, X, O, O]
        ], 5, 4)
        self.assertFalse(is_diagonal_win(board, player=X))

    def test_diagonal_win_primary_5x5_in_row_to_win_4(self):
        board = setup_board([
            [O, O, O, O, O],
            [O, X, O, X, O],
            [O, X, X, O, O],
            [O, O, X, X, X],
            [X, O, X, O, X]
        ], 5, 4)
        self.assertTrue(is_diagonal_win(board, player=X))

    def test_diagonal_win_secondary_5x5_in_row_to_win_4(self):
        board = setup_board([
            [O, O, X, O, O],
            [O, X, O, X, O],
            [O, X, X, X, X],
            [X, O, O, X, X],
            [O, O, O, X, X]
        ], 5, 4)
        self.assertTrue(is_diagonal_win(board, player=X))

    def test_diagonal_win_no_win_secondary_diagonal_5x5(self):
        board = setup_board([
            [O, O, O, O, O],
            [O, X, X, X, O],
            [X, X, O, O, O],
            [O, X, O, X, O],
            [O, O, O, O, X]
        ], 5, 4)
        self.assertFalse(is_diagonal_win(board, player=X))

    def test_diagonal_win_in_row_to_win_2_primary_5x5(self):
        board = setup_board([
            [X, X, O, O, X],
            [O, X, X, O, X],
            [O, O, X, X, O],
            [X, O, O, X, O],
            [X, X, O, O, X]
        ], 5, 2)
        self.assertTrue(is_diagonal_win(board, player=X))

    def test_diagonal_win_in_row_to_win_2_secondary_5x5(self):
        board = setup_board([
            [X, O, X, O, X],
            [O, X, X, O, X],
            [O, O, O, O, O],
            [X, O, X, X, X],
            [X, X, O, O, O]
        ], 5, 2)
        self.assertTrue(is_diagonal_win(board, player=X))

    def test_diagonal_win_no_win_in_row_to_win_2_5x5(self):
        board = setup_board([
            [O, O, O, O, O],
            [O, O, O, O, X],
            [O, X, X, X, X],
            [X, X, O, X, O],
            [X, X, O, O, X]
        ], 5, 2)
        self.assertTrue(is_diagonal_win(board, player=X))

    def test_diagonal_win_in_row_to_win_3_primary_7x7(self):
        board = setup_board([
            [X, O, X, O, O, O, O],
            [O, X, X, O, O, O, O],
            [O, O, X, X, O, O, O],
            [O, O, O, X, X, X, O],
            [O, O, X, O, X, X, X],
            [O, O, O, O, O, X, X],
            [X, O, O, X, O, O, X]
        ], 7, 3)
        self.assertTrue(is_diagonal_win(board, player=X))

    def test_diagonal_win_in_row_to_win_5_secondary_7x7(self):
        board = setup_board([
            [X, O, X, O, O, O, O],
            [O, X, X, O, O, O, O],
            [O, O, X, X, O, O, O],
            [O, O, O, X, X, X, O],
            [O, O, O, X, X, O, O],
            [O, O, O, O, X, X, X],
            [X, X, O, X, O, O, X]
        ], 7, 5)
        self.assertTrue(is_diagonal_win(board, player=X))

    # Test cases for 9x9 board

    def test_diagonal_win_in_row_to_win_4_primary_9x9(self):
        board = setup_board([
            [X, O, X, O, O, O, O, O, O],
            [O, X, X, O, O, O, O, O, O],
            [O, O, X, X, O, O, O, O, O],
            [O, O, O, X, X, X, O, O, O],
            [O, O, X, O, X, X, X, O, O],
            [O, O, O, O, O, X, X, X, O],
            [O, X, O, O, X, X, X, O, O],
            [X, O, O, O, O, X, O, O, X]
        ], 9, 4)
        self.assertTrue(is_diagonal_win(board, player=X))

    def test_diagonal_win_in_row_to_win_4_secondary_9x9(self):
        board = setup_board([
            [X, O, X, O, O, O, O, O, O],
            [O, X, X, O, O, O, O, O, O],
            [O, O, X, X, O, O, O, O, O],
            [O, X, O, X, X, X, X, O, O],
            [O, O, O, O, X, X, X, X, O],
            [O, O, O, O, O, X, X, X, X],
            [O, O, X, X, X, X, X, O, X],
            [X, O, O, O, O, O, O, X, O]
        ], 9, 4)
        self.assertTrue(is_diagonal_win(board, player=X))

    def test_diagonal_win_mixed_diagonals_9x9(self):
        board = setup_board([
            [O, X, O, O, O, O, O, O, X],
            [O, O, X, X, X, X, O, O, O],
            [O, O, X, X, O, O, O, X, O],
            [O, O, X, O, X, X, X, X, X],
            [X, O, X, O, O, O, X, X, X],
            [O, X, O, O, X, X, O, X, O],
            [O, O, X, O, X, X, O, O, O],
            [O, O, O, O, O, O, X, O, X]
        ], 9, 4)
        self.assertTrue(is_diagonal_win(board, player=X))


if __name__ == "__main__":
    unittest.main()