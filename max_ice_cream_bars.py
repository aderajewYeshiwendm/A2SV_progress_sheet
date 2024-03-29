class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total = 0
        count = 0
        for i in costs:
            total += i
            count += 1
            if total > coins:
                count = count - 1
                break
        return count


