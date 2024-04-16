class Solution(object):
    def pancakeSort(self, arr):
        flips = []
    
   
        def flip(arr, k):
            left, right = 0, k
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        
        for target in range(len(arr), 0, -1):
           
            index = arr.index(target)
            if index != target - 1:
               
                flip(arr, index)
                flips.append(index + 1)
                
                flip(arr, target - 1)
                flips.append(target)

        return flips
