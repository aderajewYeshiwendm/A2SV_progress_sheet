# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    a = set(map(int, input().split())) 
    n = int(input()) 
    res = True
    
    for i in range(n):
        b = set(map(int, input().split()))
        
        if not a.issuperset(b) or a == b:
            res = False
            break
    
    print(res)
