class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step = 1
        hold = capacity
        capacity -= plants[0]
        for i in range(1,len(plants)):
            
            if plants[i] > capacity:
                step += 2 * i + 1
                capacity = hold
                capacity -= plants[i]
            else: 
                step += 1
                capacity -= plants[i]

        return step


        