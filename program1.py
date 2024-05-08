class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0

        count = 0
        rows, cols = len(grid), len(grid[1])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j]!= 'L':
                return
            grid[i][j] = 'D'
            if 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "L":
                    dfs(i, j)
                    count += 1
        return count