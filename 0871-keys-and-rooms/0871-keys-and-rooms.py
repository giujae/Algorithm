class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)

        visited = [False] * n # 방문처리 배열

        def dfs(room):
            visited[room] = True
            for key in rooms[room]: # 해당 방을 방문했을 때 얻은 열쇠들에 대해
                if not visited[key]:
                    dfs(key)
        dfs(0)

        return all(visited) # iterable 객체 내부에 모든 값이 True 인지


