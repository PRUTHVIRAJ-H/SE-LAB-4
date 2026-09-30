import unittest
# Import your classes from different files
from board import Board
from game import Minesweeper

class TestMyApplication(unittest.TestCase):

    def setUp(self):
        self.board = Board(5,5,5)
       

    def test_inbound(self):
        self.assertEqual(self.board.in_bounds(10,10), False)
        self.assertEqual(self.board.in_bounds(5,5),False)
        self.assertEqual(self.board.in_bounds(4,4),True)
        self.assertEqual(self.board.in_bounds(3,3),True)

    def test_toggle_flag(self):
        self.assertEqual(self.board.toggle_flag((4,4)),True)
        self.assertEqual(self.board.reveal((4,4)),False)
        self.assertEqual(self.board.toggle_flag((4,4)),True)

    def test_reveal(self):
        for i,j in self.board.mines:
            self.assertEqual(self.board.reveal((i,j)),True)
        
        for i in range(self.board.rows):
            for j in range(self.board.cols):
                if (i,j) not in self.board.mines:
                    self.assertEqual(self.board.reveal((i,j)),False)

    def test_adjacent_mines(self):

        neigh = []
        for i,j in self.board.mines:
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                   if dr == 0 and dc == 0:
                       continue
                   nr, nc = i + dr, j + dc
                   if 0 <= nr < self.board.rows and 0 <= nc < self.board.cols:
                       self.assertEqual(self.board.adjacent_mines(nr,nc) > 0,True)
                       neigh.append((nr,nc))

        for i in range(self.board.rows):
            for j in range(self.board.cols):
                if (i,j) not in neigh:
                     self.assertEqual(self.board.adjacent_mines(i,j) > 0,False)
    

    def test_won(self):
        for i in range(self.board.rows):
            for j in range(self.board.cols):
                if (i,j) not in self.board.mines:
                    self.board.reveal((i,j))

        self.assertEqual(self.board.won(),True)
                        
    #def test_different_modes(self):

        
if __name__ == "__main__":
    unittest.main()