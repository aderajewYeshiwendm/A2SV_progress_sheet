if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = []
    for i in arr:
        if i== max(arr):
            pass
        else:
            res.append(i)
    print(max(res))
