class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        stack = []
        for i in range(len(image)):
            stack2 = []
            for j in range(len(image[i])-1,-1,-1):
                stack2.append(image[i][j])
            stack.append(stack2)
        for i in range(len(image)):
            for j in range(len(image[i])):
                if stack[i][j] == 0:
                    stack[i][j] = 1
                else:
                    stack[i][j] = 0
        return stack

        