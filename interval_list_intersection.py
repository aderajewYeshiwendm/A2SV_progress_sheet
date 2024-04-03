class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
    i, j = 0, 0
    
    while i < len(firstList) and j < len(secondList):
        start1, end1 = firstList[i]
        start2, end2 = secondList[j]
        
        # Check for intersection
        if start1 <= end2 and start2 <= end1:
            result.append([max(start1, start2), min(end1, end2)])
        
        # Move pointers based on end points
        if end1 < end2:
            i += 1
        else:
            j += 1
    
    return result
