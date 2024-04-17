class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target_count = n // 4
        count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for char in s:
            count[char] += 1
        
        left, right = 0, 0
        min_length = float('inf')
        
        while right < n:
            count[s[right]] -= 1
            while left < n and all(count[char] <= target_count for char in 'QWER'):
                min_length = min(min_length, right - left + 1)
                count[s[left]] += 1
                left += 1
            right += 1
        
        return min_length
