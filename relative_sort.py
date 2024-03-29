class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        ans1 = []
        for i in arr2:
            for j in arr1:
                if j == i:
                    ans.append(j)
        
                if j not in arr2:
                    ans1.append(i)
        ans1.sort()
        return ans+ans1
        
