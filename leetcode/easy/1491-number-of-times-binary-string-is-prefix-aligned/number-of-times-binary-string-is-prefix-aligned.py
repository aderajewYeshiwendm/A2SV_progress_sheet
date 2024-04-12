class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_index = 0  # Initialize the maximum index of bulbs turned on
        count = 0  # Initialize the count of moments when all bulbs are blue

        for i, flip in enumerate(flips, 1):
            max_index = max(max_index, flip)  # Update the maximum index
            if max_index == i:  # If the maximum index equals the current index, all bulbs up to this index are blue
                count += 1  # Increment the count

        return count
