class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        count = 0
        ave = sum(arr[0:k])
        if ave / k >= threshold:
            count += 1
        for i in range(k, len(arr)):
            ave += arr[i] - arr[left]
            left += 1
            if ave / k >= threshold:
                count += 1
        return count
            
        
#         count = 0
#         sum0 = sum(arr[0:k])
#         if sum0/k >= threshold:
#             count+=1
#         for i in range(1,len(arr)-k+1):
#             sum0+=(arr[k+i-1])
#             sum0-=arr[i-1]
            
#             if sum0 / k >= threshold:
#                 count += 1
#         return count