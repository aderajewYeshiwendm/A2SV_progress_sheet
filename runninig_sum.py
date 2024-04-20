class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        presum = [0]*len(nums)
        presum[0] = nums[0]
        for i in range(1,len(nums)):
            presum[i] = presum[i-1]+nums[i]
        return presum
