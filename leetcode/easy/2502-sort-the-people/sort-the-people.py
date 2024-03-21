class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(1, n):
            key_name = names[i]
            key_height = heights[i]
            j = i - 1
            while j >= 0 and heights[j] < key_height:
                names[j + 1] = names[j]
                heights[j + 1] = heights[j]
                j -= 1
            names[j + 1] = key_name
            heights[j + 1] = key_height
        return names
