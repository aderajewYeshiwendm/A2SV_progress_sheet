class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_freq = {0: 1} 
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix_sum_freq:
                count += prefix_sum_freq[curr_sum - k]
            prefix_sum_freq[curr_sum] = prefix_sum_freq.get(curr_sum, 0) + 1

        return count
