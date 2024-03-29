class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
    
        operations = 0
        prev_largest = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < prev_largest:
                operations += i
                prev_largest = nums[i]
        
        return operations

            
