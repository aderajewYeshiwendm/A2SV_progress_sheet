class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        ave = sum(nums[:k])
        ma = ave/k
        left = 0
        for i in range(k,n):
            ave += nums[i] - nums[left]
            left += 1
            ma = max(ma,ave/k)
        return ma

        