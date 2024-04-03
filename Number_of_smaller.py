def count_smaller_elements(arr1, arr2):
    counts = []
    for num in arr2:
        left, right = 0, len(arr1)
        while left < right:
            mid = (left + right) // 2
            if arr1[mid] < num:
                left = mid + 1
            else:
                right = mid
        counts.append(left)
    return counts

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

counts = count_smaller_elements(arr1, arr2)
print(*counts)
