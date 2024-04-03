class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums)
        total = sum(nums[:k])
        max_average = total/k
        left = 0
        for i in range(k, length):
            total += nums[i] - nums[left]
            left += 1
            max_average = max(max_average, total/k)
        return max_average

    
    
    
        