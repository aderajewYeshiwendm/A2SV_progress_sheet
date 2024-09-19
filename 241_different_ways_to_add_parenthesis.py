class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def compute(ex):

            if ex in memo:
                return memo[ex]
            
            res = []

            for index in range(len(ex)):
                if ex[index] in '+-*':
                    left = compute(ex[:index])
                    right = compute(ex[index + 1:])

                    for l in left:
                        for r in right:
                            if ex[index] == '+':
                                res.append(l+r)
                            elif ex[index] == '-':
                                res.append(l-r)
                            else:
                                res.append(l*r)
            if not res:
                res.append(int(ex))
            memo[ex] = res

            
            
            return res
        return compute(expression)
