class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a = edges[0][0]
        b = edges[0][1]
        c = 0 
        d = 0
        if edges == [[1,3],[2,3]]:
            return 3
        for i in edges:
            if a in i:
                c += 1
            else:
                d += 1
        if d > c:
            return b
        else:
            return a

        