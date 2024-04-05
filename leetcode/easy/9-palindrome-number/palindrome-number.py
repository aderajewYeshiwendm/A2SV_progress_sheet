class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=abs(x)
        reverse_num=0
        while num != 0:
            r=num%10
            reverse_num = reverse_num*10+r
            num //= 10
        return reverse_num == x
        