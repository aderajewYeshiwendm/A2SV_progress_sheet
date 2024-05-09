class Solution(object):
    def subarraysDivByK(self, nums, k):
        prefix_sum_remainders = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            mod = curr_sum % k
            if mod < 0:  # Ensure mod is positive
                mod += k
            if mod in prefix_sum_remainders:
                count += prefix_sum_remainders[mod]
            prefix_sum_remainders[mod] = prefix_sum_remainders.get(mod, 0) + 1

        return count
