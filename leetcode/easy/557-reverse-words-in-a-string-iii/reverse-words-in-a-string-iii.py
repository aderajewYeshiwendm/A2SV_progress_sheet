class Solution:
    def reverseWords(self, s: str) -> str:
        ans = s.split(' ')

        res = ''
        for i in ans:
            
            b = len(i) - 1
            
            while b >= 0:
                res += i[b]
                b -= 1
            res += ' '
        
        return res[:-1]
        
        