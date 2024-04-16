class Solution(object):
    def pancakeSort(self, arr):
        flips = []
    
    # Helper function to flip the array up to index k
        def flip(arr, k):
            left, right = 0, k
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        # Iterate from the last index to the first
        for target in range(len(arr), 0, -1):
            # Find the index of the target element
            index = arr.index(target)
            if index != target - 1:
                # If the target is not already at its correct position
                # Flip the array up to the index of the target element
                flip(arr, index)
                flips.append(index + 1)
                # Flip the entire array to move the target element to the last position
                flip(arr, target - 1)
                flips.append(target)

        return flips