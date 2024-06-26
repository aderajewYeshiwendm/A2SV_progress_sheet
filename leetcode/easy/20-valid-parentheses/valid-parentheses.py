class Solution(object):
    def isValid(self, s):
        brackets = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c in brackets.values():
                stack.append(c)
            elif c in brackets:
                if stack == [] or stack.pop() != brackets[c]:
                    return False
            

        
        return not stack
                
        