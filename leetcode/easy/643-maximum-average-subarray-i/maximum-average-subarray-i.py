class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        var = sum(nums[:k])
        ma = var/k
        left = 0
        for i in range(k,n):
            var += nums[i] - nums[left]
            left += 1
            ma = max(ma,var/k)
        return ma

        