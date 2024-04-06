class Solution(object):
    def longestSubarray(self, nums):
        ones = 0
        zeros = 0
        ans = 0
        for i in nums:
            if i == 1:
                ones += 1
            else:
                ans = max(ans, ones+ zeros)

                zeros = ones
                
                ones = 0
        ans = max(ans, ones+zeros)
        if ans == len(nums):
            return ans - 1
        else:return ans
#         sw = []
#         res=0
#         for i in nums:
#             if i == 0 and 0 in sw:
#                 sw = sw[sw.index(i)+1:]

                
           
#             sw.append(i)
#             res = max(res,len(sw)-1)
#         return res


        