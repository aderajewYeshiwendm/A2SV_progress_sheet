def find_sources_and_sinks(adj_matrix, n):
    sources = []
    sinks = []
    
    # Check for sources (no incoming edges)
    for col in range(n):
        is_source = True
        for row in range(n):
            if adj_matrix[row][col] == 1:
                is_source = False
                break
        if is_source:
            sources.append(col + 1)  # +1 to convert 0-based index to 1-based
    
    # Check for sinks (no outgoing edges)
    for row in range(n):
        is_sink = True
        for col in range(n):
            if adj_matrix[row][col] == 1:
                is_sink = False
                break
        if is_sink:
            sinks.append(row + 1)  # +1 to convert 0-based index to 1-based
    
    return sources, sinks

# Reading input
n = int(input())
adj_matrix = []
for _ in range(n):
    adj_matrix.append(list(map(int, input().split())))

# Finding sources and sinks
sources, sinks = find_sources_and_sinks(adj_matrix, n)

# Output results
print(len(sources), ' '.join(map(str, sources)))
print(len(sinks), ' '.join(map(str, sinks)))
