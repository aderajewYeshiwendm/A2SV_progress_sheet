class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n== 1:
            return 1
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            t0 = 0
            t1 = 1
            t2 = 1
            ans = 0
            for i in range(3, n):
                temp = t1 + t2 + t0
                
                t0 = t1
                t1 = t2
                t2 = temp
                ans = t0 + t1 + t2
                
                
                
            return ans
        