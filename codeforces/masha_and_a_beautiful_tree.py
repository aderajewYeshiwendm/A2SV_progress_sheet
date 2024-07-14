import sys
input = sys.stdin.read
data = input().split()

def solve(l, r):
    if r - l == 1:
        return 0
    
    mid = (l + r) // 2
    max_left = max(arr[l:mid])
    max_right = max(arr[mid:r])
    operations = 0
    
    if max_left > max_right:
        operations += 1
        for i in range(mid - l):
            arr[l + i], arr[mid + i] = arr[mid + i], arr[l + i]
    
    return solve(l, mid) + solve(mid, r) + operations

index = 0
t = int(data[index])
index += 1
results = []

for _ in range(t):
    m = int(data[index])
    index += 1
    arr = list(map(int, data[index:index + m]))
    index += m
    
    operations = solve(0, m)
    if arr == sorted(arr):
        results.append(str(operations))
    else:
        results.append('-1')

sys.stdout.write("\n".join(results) + "\n")
