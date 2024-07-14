def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    
    # Number of vertices
    n = int(data[index])
    index += 1
    
    # Number of operations
    k = int(data[index])
    index += 1
    
    # Initialize adjacency list
    graph = {i: [] for i in range(1, n + 1)}
    
    # Collect output to print at the end
    output = []
    
    # Process each operation
    for _ in range(k):
        operation = int(data[index])
        index += 1
        
        if operation == 1:
            u = int(data[index])
            index += 1
            v = int(data[index])
            index += 1
            
            # Add edge (u, v)
            graph[u].append(v)
            graph[v].append(u)
            
        elif operation == 2:
            u = int(data[index])
            index += 1
            
            # Get the list of adjacent vertices
            if u in graph:
                output.append(" ".join(map(str, sorted(graph[u]))))
            else:
                output.append("")
    
    # Print all output at once
    print("\n".join(output))

if __name__ == "__main__":
    main()
