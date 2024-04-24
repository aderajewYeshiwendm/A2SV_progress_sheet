class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n==1:
            return n
        elif n <= 3:
            return n -1
        
        else:
            t0 = 0
            t1 = 1
            t2 = 1
            for i in range(3, n):
                temp = t1 + t2 + t0
                
                t0 = t1
                t1 = t2
                t2 = temp
                
            return t0 + t1 + t2
        