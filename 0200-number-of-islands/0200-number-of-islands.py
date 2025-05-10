class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        count = 0

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] != "1":
                return
            grid[x][y] = "0"
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count
