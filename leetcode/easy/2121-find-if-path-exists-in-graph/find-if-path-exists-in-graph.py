class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        
        # BFS
        visited = set()
        queue = deque([source])

        while queue:
            vertex = queue.popleft()

            if vertex == destination:
                return True
            
            visited.add(vertex)

            for neighbour in graph[vertex]:

                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)


        # DFS
        # visited = set()

        # def dfs(current, destination, visited):

        #     if current == destination:
        #         return True
            
        #     visited.add(current)

        #     for neighbour in graph[current]:
        #         if neighbour not in visited:
        #             if dfs(neighbour, destination, visited):
        #                 return True
        #     return False

        # return dfs(source, destination, visited)