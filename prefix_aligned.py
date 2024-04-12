class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_index = 0  
        count = 0 
        for i, flip in enumerate(flips, 1):
            max_index = max(max_index, flip)
            if max_index == i: 
                count += 1

        return count
