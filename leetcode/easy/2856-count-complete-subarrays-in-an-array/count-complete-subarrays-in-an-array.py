class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        nums_len = len(set(nums))
        l = r = 0
        sub_arr = 0

        while r < len(nums):
            temp = set(nums[l:r+1])
            if len(temp) == nums_len:
                sub_arr += len(nums) - r
                l += 1
            else:
                r += 1
            
        return sub_arr