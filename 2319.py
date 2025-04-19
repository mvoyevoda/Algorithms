class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        left_diagonal, right_diagonal = 0, n
        for x in range(n):
            for y in range(n):
                if x == y or x+y == n-1:
                    if grid[x][y] == 0:
                        return False
                elif grid[x][y] != 0:
                    return False

        return True
