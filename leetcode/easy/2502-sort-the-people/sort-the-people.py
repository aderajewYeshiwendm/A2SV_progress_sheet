class Solution(object):
    def sortPeople(self, names, heights):
        dict = {}
        lst = [''] * len(names)
        for i in range(len(names)):
            dict[heights[i]] = names[i]
        maximum = max(heights)
        count = [0] * (maximum + 1)
        for num in heights:
            count[num] += 1

        target = 0
        for index, value in enumerate(count):
            for i in range(value):
                heights[target] = index
                target += 1
        k = 0
        for j in range(len(heights)-1,-1,-1):
            lst[k]=dict[heights[j]]
            k += 1
        return lst




        
        