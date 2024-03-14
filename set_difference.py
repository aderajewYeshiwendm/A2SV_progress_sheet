# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
   
    n = int(input())
    eng_subscribers = set(map(int, input().split()))
    m = int(input())
    french_subscribers = set(map(int, input().split()))
    eng_only = eng_subscribers.difference(french_subscribers)
    
    
    print(len(eng_only))
