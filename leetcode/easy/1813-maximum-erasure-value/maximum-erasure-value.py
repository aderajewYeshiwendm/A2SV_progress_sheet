
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        visited = set()
        res = 0
        curr_sum = 0
        
        while right < len(nums):
            if nums[right] not in visited:
                visited.add(nums[right])
                curr_sum += nums[right]
                right += 1
                res = max(res, curr_sum)
            else:
                visited.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
                
        return res
