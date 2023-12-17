import unittest

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
from charlotte import Board,Symbol
from experiments.check_horizontal_vertical_lines_v2.main import is_vertical;

def setup_board(grid : list[list[Symbol | None]],dimensions : int,in_row_to_win : int) -> Board :
    board = Board(dimensions,in_row_to_win)
    board.board = grid
    return board


X = Symbol.CROSS
O = Symbol.NAUGHT
E = None

class TestVerticalWins(unittest.TestCase) : 
    def test_example(self) :
        board = setup_board([
            [X,O,O],
            [X,E,O],
            [O,E,O],
        ],3,3)

        self.assertTrue(is_vertical(board,O))

    def test_two_in_a_row_vertical_1(self):
        board = setup_board([
            [E, X, X],
            [E, X, E],
            [E, X, E],
        ],3,3)

        self.assertTrue(is_vertical(board,X))

    def test_one_in_a_row_vertical(self):
        board = setup_board([
            [E, E, E],
            [X, E, E],
            [E, E, E],
        ],3,3)

        self.assertFalse(is_vertical(board,X))

    def test_vertical_win_with_mixed_symbols_1(self):
        board = setup_board([
            [X, O, X],
            [O, X, E],
            [E, X, E],
        ],3,3)

        self.assertTrue(is_vertical(board,X))

    def test_no_win_vertical(self):
        board = setup_board([
            [E, E, E],
            [O, E, E],
            [E, E, X],
        ],3,3)

        self.assertFalse(is_vertical(board,O))

    def test_example_5x5(self):
        board = setup_board([
            [X, O, O, O, O],
            [X, E, E, E, O],
            [O, E, O, E, E],
            [O, X, O, O, E],
            [O, O, O, X, O],
        ],5,3)

        self.assertTrue(is_vertical(board,O))

    def test_three_in_a_row_vertical_1_5x5(self):
        board = setup_board([
            [E, X, X, X, E],
            [E, O, E, E, E],
            [E, O, O, O, E],
            [E, O, E, E, E],
            [E, E, E, E, E],
        ],5,3)

        self.assertTrue(is_vertical(board,X))

    def test_two_in_a_row_vertical_1_5x5(self):
        board = setup_board([
            [E, O, O, E, E],
            [E, O, X, E, E],
            [E, O, E, E, E],
            [E, E, E, E, E],
            [E, E, E, E, E],
        ],5,3)

        self.assertTrue(is_vertical(board,O))

    def test_five_in_a_row_vertical_1_5x5(self):
        board = setup_board([
            [E, O, X, X, X, X],
            [E, E, O, E, E, E],
            [E, E, O, E, E, E],
            [E, E, X, E, E, E],
            [E, E, E, E, E, E],
        ],5,3)

        self.assertFalse(is_vertical(board,O))

    def test_no_win_vertical_5x5(self):
        board = setup_board([
            [E, E, E, E, E],
            [E, O, E, E, E],
            [E, O, E, E, E],
            [E, O, E, E, E],
            [E, X, E, E, E],
        ],5,3)

        self.assertFalse(is_vertical(board,O))

    def test_example_3x3_in_row_to_win_2(self):
        board = setup_board([
            [X, X, X],
            [O, E, O],
            [O, E, O],
        ],3,3)

        self.assertTrue(is_vertical(board,X))

    def test_three_in_a_row_vertical_1_3x3_in_row_to_win_2(self):
        board = setup_board([
            [E, X, X],
            [E, O, E],
            [E, E, O],
        ],3,3)

        self.assertFalse(is_vertical(board,X))

    def test_custom_inrowtowin(self) :
        board = setup_board([
            [E, E, E, E, E],
            [E, O, E, E, E],
            [E, O, E, E, E],
            [E, O, E, E, E],
            [E, O, E, E, E],
        ],5,4)

        self.assertTrue(is_vertical(board,O))

    def test_real_scenario_1(self):
        board = setup_board([
            [E, E, X, O, X, E],
            [E, E, O, O, E, E],
            [E, E, X, E, E, X],
            [E, O, E, E, E, X],
            [E, E, E, E, E, E],
        ], 5, 3)

        self.assertFalse(is_vertical(board,X))

    def test_real_scenario_2(self):
        board = setup_board([
            [E, E, E, E, E, E],
            [E, E, O, E, E, E],
            [E, O, X, E, E, E],
            [E, O, O, X, E, E],
            [E, O, O, O, X, E],
        ], 5, 4)

        self.assertFalse(is_vertical(board,X))

    def test_real_scenario_3(self):
        board = setup_board([
            [E, E, E, E, E, O],
            [E, E, E, E, E, X],
            [E, E, X, X, X, E],
            [E, O, O, E, E, O],
            [E, O, E, E, E, O],
        ], 5, 5)

        self.assertFalse(is_vertical(board,X))

    def test_real_scenario_4(self):
        board = setup_board([
            [E, E, E, E, E, O],
            [E, E, E, E, E, X],
            [E, E, O, O, O, E],
            [E, O, O, X, O, O],
            [E, O, E, O, O, O],
        ], 5, 4)

        self.assertFalse(is_vertical(board,O))

    def test_real_scenario_5(self):
        board = setup_board([
            [X, X, X, E, E, E],
            [O, O, O, E, E, E],
            [E, X, O, E, E, E],
            [O, E, E, E, E, E],
            [E, E, E, E, E, E],
        ], 5, 3)

        self.assertFalse(is_vertical(board,X))

if __name__ == '__main__':
    unittest.main()