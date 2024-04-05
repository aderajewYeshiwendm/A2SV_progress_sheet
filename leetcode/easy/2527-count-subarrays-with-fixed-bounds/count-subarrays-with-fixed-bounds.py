class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        fast,slow = -1,-1
        start = 0
        res = 0
        for i in range(len(nums)):
            
            if nums[i] < minK or nums[i] > maxK:
                fast,slow = -1,-1
                start = i+1
            if nums[i] == minK:
                slow = i
            if nums[i] == maxK:
                fast = i
            res += max(0,min(slow,fast)-start+1)

        return res