import gol
import unittest

class GOLTest(unittest.TestCase):
	def testReturnNeighbors(self):
		self.assertSetEqual(
			gol.ReturnNeighbors(1,1), set([(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2)]))

	def testGetAliveNeighbors(self):
		board=set([(1,1),(1,2)])
		self.assertEqual(gol.ReturnAliveNeighbors(board,1,1), 1)

	def testNextState(self):
		board=set([(1,1),(1,2)])
		self.assertEqual(gol.NextState(board,1,1),0)

	def testNeighborUnion(self):
 		board=set([(1,1),(1,2)])
 		union_set=gol.NeighborUnion(board);
		x_set=gol.ReturnNeighbors(1,1)
		y_set=gol.ReturnNeighbors(1,2)
		expected_set=x_set.union(y_set).union(board)
		self.assertSetEqual(union_set, expected_set)

	def testNewBoardTrivial(self):
		board=set([(1,1),(1,2)])
		new_board=gol.NewBoard(board)
		self.assertSetEqual(new_board,set())

	def testNewBoard(self):
		board=set([(1,1),(1,2),(2,1)]);
		expected_board=set([(1,1),(1,2),(2,1),(2,2)])
		self.assertSetEqual(gol.NewBoard(board),expected_board)

if __name__ == '__main__':
  unittest.main()
