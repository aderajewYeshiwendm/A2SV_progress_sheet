class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        index = 0
        zero = 0

        # while unpicked values, consume and put to end of nonzero section
        while zero < len(nums):
            # if we encounter 0s, the putter stays in place
            if nums[zero] != 0:
                nums[index] = nums[zero]
                index += 1

            # the picker moves up regardless
            zero += 1

        # when picker reaches end, putter continues with just 0s
        while index < len(nums):
            nums[index] = 0
            index += 1