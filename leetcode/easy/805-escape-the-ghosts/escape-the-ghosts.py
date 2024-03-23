class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        lst = []
        ans = abs(target[0]) + abs(target[1])
        for i in ghosts:
            lst.append(abs(target[0]-i[0]) + abs(target[1]- i[1]))
        return ans < min(lst)

        