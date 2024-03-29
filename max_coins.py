class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        answer = 0
        h = len(piles)
        x = h // 3
        for i in range(x):
            answer += piles[h-2]
            h -= 2
        return answer

        
