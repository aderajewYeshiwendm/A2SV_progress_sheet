class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        sw = []
       
        for i in range(len(blocks)-k+1):
            sw.append(blocks[i:k+i])
        min_operations = k
        for i in sw:
            no_whites = i.count('W')
            min_operations = min(no_whites, min_operations)
        return min_operations


        
              

        