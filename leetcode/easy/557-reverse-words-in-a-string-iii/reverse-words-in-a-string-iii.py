class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        j = 1
        res = ''
        for i in range(len(s)):
            
            res += s[i]
            
            if s[i] == ' ':
                ans += res[::-1]
                res = ''
            else:pass
        ans = ans + ' ' + res[::-1]
        return ans[1:]
        
        