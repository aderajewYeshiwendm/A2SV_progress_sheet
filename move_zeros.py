class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        index = 0
        zero = 0

        while zero < len(nums):
            if nums[zero] != 0:
                nums[index] = nums[zero]
                index += 1

            zero += 1

        while index < len(nums):
            nums[index] = 0
            index += 1
