class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
       
        n = len(grid)
        dp = [[0] * n for _ in range(n)]

        # Initialize the first row of dp
        for j in range(n):
            dp[0][j] = grid[0][j]

        # Iterate over the rows of the grid
        for i in range(1, n):
            # Iterate over the elements in the current row
            for j in range(n):
                # Initialize the minimum value to be infinity
                min_val = float('inf')
                # Iterate over the elements in the previous row
                for k in range(n):
                    # Check if the previous element is not in the same column
                    if k != j:
                        # Update the minimum value
                        min_val = min(min_val, dp[i - 1][k])
                # Update dp with the minimum sum
                dp[i][j] = grid[i][j] + min_val

        # Return the minimum value from the last row of dp
        return min(dp[-1])

