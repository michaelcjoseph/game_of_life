import os
import time

class Life(object):
	def __init__(self, board):
		self.board = board
		self.max_row = 20
		self.max_col = 20
		for (i, j) in board:
			if i > self.max_row:
				self.max_row = i
			if j > self.max_col:
				self.max_col = j

	def tick(self):
		self.board = self.NewBoard()

	def NewBoard(self):
		all_cells = self.NeighborUnion()
		new_board = set()

		for (i, j) in all_cells:
			check_alive = self.NextState(i, j)
			if check_alive == 1:
				new_board = new_board.union([(i, j)])

		return new_board

	def NeighborUnion(self):
		union_set = set()

		for (i, j) in self.board:
			union_set = union_set.union(self.ReturnNeighbors(i, j)).union(self.board)

		return union_set

	def NextState(self, i, j):
		alive_neighbors = self.ReturnAliveNeighbors(i, j)

		if (i, j) in self.board:
			if alive_neighbors < 2 or alive_neighbors > 3:
				return 0
			else:
				return 1
		else:
			if alive_neighbors == 3:
				return 1
			else:
				return 0

	def ReturnAliveNeighbors(self, i, j):
		return len(self.board.intersection(self.ReturnNeighbors(i,j)))

	def ReturnNeighbors(self, i, j):
		neighbors = set()
		min_neighbor_row = i - 1
		max_neighbor_row = i + 1
		min_neighbor_col = j - 1
		max_neighbor_col = j + 1
		
		if i == 0:
			min_neighbor_row = self.max_row
		elif i == self.max_row:
			max_neighbor_row = 0
		
		if j == 0:
			min_neighbor_col = self.max_col
		elif j == self.max_col:
			max_neighbor_col = 0
		
		neighbors = set([(min_neighbor_row, min_neighbor_col), 
						 (min_neighbor_row, j), 
						 (min_neighbor_row, max_neighbor_col), 
						 (i, min_neighbor_col), 
						 (i, max_neighbor_col), 
						 (max_neighbor_row, min_neighbor_col), 
						 (max_neighbor_row, j), 
						 (max_neighbor_row, max_neighbor_col)])
		return neighbors

	def PrintBoard(self):
		board_matrix = []
		for i in range(0, self.max_row+1):
			row = []
			for j in range(0, self.max_col+1):
				row.append('-')
			board_matrix.append(row)

		for (i, j) in self.board:
			board_matrix[i][j] = '1'

		for i in range(0, self.max_row+1):
			row = ''
			for j in range(0, self.max_col+1):
				row += board_matrix[i][j] + ' '
			print row

def main():
	board = set([(1,1),(1,2),(1,3),(2,3),(3,2)])
	game = Life(board)

	i = 0
	while i < 100:
		os.system('clear')
		game.PrintBoard()
		time.sleep(0.5)
		game.tick()
		i += 1

if __name__ == "__main__":
  main()