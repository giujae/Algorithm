class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)

        visited = set() # 방문처리 하되, 중복은 제거

        def dfs(room):
            visited.add(room)
            for key in rooms[room]: # 해당 방을 방문했을 때 얻은 열쇠들에 대해
                if key not in visited:
                    dfs(key)
        dfs(0)

        return len(rooms) == len(visited)


