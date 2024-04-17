class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = k
        for i in range(len(blocks) - k + 1):
            window = blocks[i : i + k]
            no_whites = window.count('W')
            min_operations = min(no_whites, min_operations)
        return min_operations
