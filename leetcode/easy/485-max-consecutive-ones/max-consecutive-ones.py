class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dct = 0
        ma = 0
        for i in nums:
            dct = (dct + 1) if i == 1 else 0
            
            ma = max(ma,dct)
               
            
        return ma
        