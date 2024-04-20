class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix= [0 for _ in range(len(nums))]
        postfix= [0 for _ in range(len(nums))]
        n=len(nums)
        prefix[0]=nums[0]
        postfix[n-1]=nums[n-1]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        for i in range(len(nums)-2,-1,-1):
            postfix[i]=postfix[i+1]+nums[i]
        for i in range(len(prefix)):
             if(prefix[i]==postfix[i]):
                  return i
        return -1
