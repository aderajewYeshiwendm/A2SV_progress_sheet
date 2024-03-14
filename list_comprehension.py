def getcoordinates(x, y, z, n):
  
  return [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]


x = int(input())
y = int(input())
z = int(input())
n = int(input())


coordinates = getcoordinates(x, y, z, n)


print(coordinates)
