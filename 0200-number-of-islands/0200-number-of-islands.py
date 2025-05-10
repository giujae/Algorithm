class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        dx = [0, 0, 1, -1] # 상하좌우 이동을 위한
        dy = [1, -1, 0, 0]

        count = 0

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] == "0": # 벗어날 경우이거나 0일 경우 리턴
                return
            grid[x][y] = "0" # 위 조건을 통과하면 방문처리
            for i in range(4): # 상하 좌우로 dfs 호출
                 dfs(x + dx[i], y + dy[i])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1": # 1인 위치로 부터 연결된 모든 1을 0으로 방문 처리 후
                    dfs(i, j)
                    count += 1 # 1회 증가

        return count