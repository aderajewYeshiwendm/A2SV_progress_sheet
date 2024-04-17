class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            count = oddCount = i = 0
            for j in range(len(nums)):
                if nums[j] % 2 != 0:
                    oddCount += 1
                while oddCount > k:
                    if nums[i] % 2 != 0:
                        oddCount -= 1
                    i += 1
                count += j - i + 1
            return count

        return atMostK(nums, k) - atMostK(nums, k - 1)