# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p1=head
        p2=head
        size=0
        while(p2 and p2.next):
            p1=p1.next
            p2=p2.next.next
        if p2!=None:
            p1=p1.next
        prev=None
        while(p1):
            nest=p1.next
            p1.next=prev
            prev=p1
            p1=nest
        while(prev):
            if prev.val!=head.val:
                
                return False
            prev=prev.next
            head=head.next
            
        return True
            
            
