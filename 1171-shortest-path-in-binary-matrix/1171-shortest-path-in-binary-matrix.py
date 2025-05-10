from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1: # 시작지점과 도착지점이 1 이면 가능한 경로가 없음
            return -1

        dx = [-1, -1, -1,  0, 0, 1, 1, 1]
        dy = [-1,  0,  1, -1, 1,-1, 0, 1]

        q = deque([(0, 0, 1)]) # x좌표, y좌표, 거리 (거리 계산 시는 시작 지점 또한 포함 하기 때문에 1)
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while q:
            x, y, distance = q.popleft()
            if x == n - 1 and y == n - 1: # 도착 지점에 도달 하고 나면 거리 반환
                return distance
            
            for i in range(8): # 대각선 까지 포함한 8가지 방향에 대해
                nx, ny = x + dx[i] , y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0: # 범위를 벗어나지 않고 방문한 적이 없으면서 0(가능한 경로) 일 경우
                    visited[nx][ny] = True # 방문처리
                    q.append((nx, ny, distance + 1)) # 현재위치로 부터 이동가능한 다음 위치를 찾기 위해 큐에 넣음

        return -1 # 도착지점에 도착하지 못했을 경우 경로는 없음