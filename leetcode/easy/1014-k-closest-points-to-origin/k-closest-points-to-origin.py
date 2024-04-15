import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create a min heap to store points based on their distances
        heap = []
        for point in points:
            distance = (point[0]**2 + point[1]**2)**0.5
            # Push tuple (-distance, point) to heap to sort by distance ascendingly
            heapq.heappush(heap, (distance, point))
        
        # Pop k closest points from the heap
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])  # Append point to result
        
        return result
