class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        substr = []
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                subs = s[i:j+1]
                substr.append(subs)
        ma = 0
        for letter in substr:
            counter = {}
            for l in letter:
                
                if l not in counter:
                    counter[l] = 0
                counter[l] += 1
            flag = True
            for val in counter:
                if counter[val] > 2:
                    flag = False
                    break
                    
            if flag:  
                ma = max(ma, len(letter))
        return ma
                    
                
                
                
                    
        