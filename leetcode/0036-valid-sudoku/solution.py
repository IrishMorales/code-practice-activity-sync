class Solution:
    # loop over rows, for each number seen in that row add it to a set, if already in a set = duplicate in row, return False
    def isRowsValid(self, board) -> bool:
        for row in board:
            if not self.hasNoDuplicates(row):
                return False
        return True

    # loop over columns, for each number seen in that column add it to a set, if already in a set = duplicate in column, return False
    def isColsValid(self, board) -> bool:
        for col in zip(*board):
            if not self.hasNoDuplicates(col):
                return False
        return True

    # loop over grids, for each number seen in that grid add it to a set, if already in a set = duplicate in grid, return False
    def isGridsValid(self, board) -> bool:
        dividers = [0, 3, 6]
        for row_index in dividers:
            for col_index in dividers:
                grid_list = [board[row_subindex][col_subindex] for row_subindex in range(row_index, row_index + 3) for col_subindex in range(col_index, col_index + 3)]
                if not self.hasNoDuplicates(grid_list):
                    return False
        return True

    def hasNoDuplicates(self, elems_list) -> bool:
        elems_digits = [char for char in elems_list if char != '.']
        return len(set(elems_digits)) == len(elems_digits)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isRowsValid(board) and self.isColsValid(board) and self.isGridsValid(board)
        # time complexity: O(n) -> n = 9 or the fows/cols/grid size
        # space complexity: O(n)


