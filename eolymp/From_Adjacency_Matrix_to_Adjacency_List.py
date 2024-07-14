def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    n = int(data[0])
    adjacency_matrix = [[0] * n for _ in range(n)]
    
    for i in range(1, n + 1):
        if data[i].strip() == "0":
            continue
        edges = list(map(int, data[i].strip().split()[1:]))
        for j in edges:
            adjacency_matrix[i - 1][j - 1] = 1
    
    for row in adjacency_matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
