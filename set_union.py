# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
   
    n = int(input())
    eng_subscribers = set(map(int, input().split()))
    m = int(input())
    french_subscribers = set(map(int, input().split()))
    uni = eng_subscribers.union(french_subscribers)
    
    
    print(len(uni))
