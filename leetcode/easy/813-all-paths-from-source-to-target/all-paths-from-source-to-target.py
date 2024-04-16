class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        queue = deque([(0, [0])])  # Initialize the queue with starting node 0 and path [0]

        while queue:
            node, path = queue.popleft()

            if node == n - 1:
                paths.append(path)
                continue

            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))

        return paths