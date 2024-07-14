import sys

def superDigit(n, k):
    # Function to compute the super digit
    res = sum(int(x) for x in n) * k
    
    # Loop until res is a single-digit number
    while res >= 10:
        res = sum(int(x) for x in str(res))
    
    return res


if __name__ == '__main__':
    input_data = sys.stdin.read().strip().split()
    n = input_data[0]
    k = int(input_data[1])
    
    result = superDigit(n, k)
    
    print(result)
