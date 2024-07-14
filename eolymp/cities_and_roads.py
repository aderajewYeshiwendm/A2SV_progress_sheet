def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    matrix = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index + n]))
        matrix.append(row)
        index += n

    # Count the number of roads
    road_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                road_count += 1

    print(road_count)

if __name__ == "__main__":
    main()
