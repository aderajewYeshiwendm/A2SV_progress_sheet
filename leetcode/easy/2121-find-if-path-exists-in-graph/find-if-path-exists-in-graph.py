class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if [source, destination] in edges:
            return True
        if source == destination:
            return True

        # Create an adjacency list from edges
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        print(graph)

        
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
        #     # print(f"visited {visited}")

        #     for neighbour in graph[current]:
        #         # print(f"neighbour {neighbour} and graph {graph[current]}")
        #         if neighbour not in visited:
        #             if dfs(neighbour, destination, visited):
        #                 visited.add(neighbour)
        #                 return True
        #     return False

        # return dfs(source, destination, visited)