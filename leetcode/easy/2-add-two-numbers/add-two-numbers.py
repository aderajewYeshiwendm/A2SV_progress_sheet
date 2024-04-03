# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = ''
        s1 = ''
        cur1 = l1
        while cur1:
            s += str(cur1.val)
            cur1 = cur1.next
        cur2 = l2
        while cur2:
            s1 += str(cur2.val)
            cur2 = cur2.next
        a = int(s[::-1]) + int(s1[::-1])
        lst = ''
        b=str(a)
        for i in range(len(b)-1,-1,-1):
            lst+=b[i]+','
        lst = lst[:-1]
        return ListNode(lst)
        
        