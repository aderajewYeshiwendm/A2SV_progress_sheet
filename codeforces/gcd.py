# Reading input
a, b = input().strip().split()
 
# Since the numbers can be up to 10^100, we treat them as strings.
# We need to compare them directly.
 
if a == b:
    print(a)
else:
    print(1)
