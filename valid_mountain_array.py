class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ma_index = arr.index(max(arr))
        if ma_index == len(arr) -1 or ma_index == 0:
            return False
        if len(arr) < 3:
            return False
        for i in range(ma_index):
            if arr[i] >= arr[i+1]:
                return False
        for j in range(len(arr)-1,ma_index, -1):
            if arr[j] >= arr[j-1]:
                return False
        return True
        
            
        
