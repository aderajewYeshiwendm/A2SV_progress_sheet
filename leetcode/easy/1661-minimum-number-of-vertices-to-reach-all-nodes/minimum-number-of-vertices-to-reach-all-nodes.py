class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        income = collections.defaultdict(list)
        for src, dst in edges:
            income[dst].append(src)
        result = []
        for i in range(n):
            if not income[i]:
                result.append(i)
        return result
        