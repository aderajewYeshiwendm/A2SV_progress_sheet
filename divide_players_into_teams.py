class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        chemistry = 0
        left, right = 0, len(skill) - 1
        
        skill.sort()
        
        check_skill = skill[left] + skill[right]
        
        while left < right:
            if skill[left] + skill[right] != check_skill:
                return -1
            else:
                chemistry += skill[left] * skill[right]
                left += 1
                right -= 1
        return chemistry
            
        
        
