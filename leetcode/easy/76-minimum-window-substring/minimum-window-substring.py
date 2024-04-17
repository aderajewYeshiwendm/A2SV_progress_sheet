class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Create two hashmaps / dictionaries for window [i, j) --> this helps to solve boundary cases
        window = dict()
        
        # need stores needed characters in t and their frequency
        need = dict()
        for c in t:
            need[c] = need.get(c, 0) + 1
            
        # Sliding window: right++ to expand, left++ to shrink, [0,0) No elements
        left, right = 0, 0
        
        # we need the condition: valid = number of candidate characters == len(need)
        # Shrink when valid satisfies what we need
        valid = 0
        
        # record the address and length of the min substring
        start = 0
        length = sys.maxsize
        
        # Start sliding
        while right<len(s): # max{right} = m-1, this is the max subscript of s
            c = s[right] # c is the next char moving into the window as the window is [left, right)
            right += 1
            if c in need.keys():
                window[c] = window.get(c,0) + 1
                # update valid
                if window[c] == need[c]:
                    valid += 1
            
            # start shrinking
            while (valid == len(need)):
                # update the min substring
                if right-left < length:
                    start = left
                    length = right - left
                # shrink: the order is the reverse of expansion
                d = s[left] # the char moving out
                left += 1
                if d in need.keys():
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window.get(d) - 1
        
        if length == sys.maxsize:
            return ''
        else:
            return s[start:start+length]