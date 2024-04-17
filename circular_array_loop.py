class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def dfs(i):
            if i in local_set:
                return True 
                
            if i in visited:
                return 

            visited.add(i)
            local_set.add(i)

            next_node = (i+nums[i])%n 

            if i == next_node or (nums[i] > 0) != (nums[next_node] > 0):
                return False 

            if dfs(next_node):
                return True 

            return False 

        
        visited = set()

        for i in range(n):
            local_set = set()
            if dfs(i):
                return True 

        return False 
