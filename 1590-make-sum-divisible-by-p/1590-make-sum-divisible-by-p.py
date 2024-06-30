class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums) % p
        if s == 0:
            return 0

        cum_sum = 0
        d = {0: -1}
        result = len(nums)
        for j, elem in enumerate(nums):
            cum_sum = (cum_sum + elem) % p
            i = d.get((cum_sum - s) % p)
            if i is not None:
                result = min(result, j - i)
            d[cum_sum] = j
        
        if result == len(nums):
            return -1
        return result