class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        output = []
        def dfs(curr):
            output.append(curr)
            if curr*10 <= n:
                dfs(curr*10)
            if curr+1 <= n and curr % 10 != 9:
                dfs(curr+1)   
        dfs(1)
        return output
