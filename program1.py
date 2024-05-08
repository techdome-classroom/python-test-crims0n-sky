class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0

        island_count = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j]!= 'L':
                return
            grid[i][j] = "W" 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "L":
                    dfs(i, j)
                    island_count += 1
        return island_count