class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        node_a=edges[0][0]
        node_b=edges[0][1]
        if edges[1][0]==node_a or edges[1][1]==node_a:
            return node_a
        else:
            return node_b
      

        
        