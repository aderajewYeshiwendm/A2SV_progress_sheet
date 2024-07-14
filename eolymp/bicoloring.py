def is_bipartite(n, graph):
    from collections import deque

    color = [-1] * n  # -1 means uncolored, 0 and 1 represent two different colors
    queue = deque()

    # Start BFS from any unvisited node
    for start in range(n):
        if color[start] == -1:  # unvisited node
            queue.append(start)
            color[start] = 0  # color it with color 0

            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 1 - current_color  # switch color

                for neighbor in graph[node]:
                    if color[neighbor] == -1:  # not colored
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        return False  # found conflict, not bipartite

    return True  # all nodes colored without conflict, bipartite

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    index = 0

    results = []

    while index < len(data):
        n = int(data[index])
        index += 1

        if n == 0:
            break

        l = int(data[index])
        index += 1

        # Build the graph as adjacency list
        graph = [[] for _ in range(n)]
        for _ in range(l):
            u, v = map(int, data[index].split())
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
            index += 1

        # Check if the graph is bipartite
        if is_bipartite(n, graph):
            results.append("BICOLOURABLE.")
        else:
            results.append("NOT BICOLOURABLE.")

    # Print all results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
