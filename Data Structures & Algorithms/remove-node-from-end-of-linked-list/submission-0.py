# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head

        n_ahead = head
        curr = temp
        for i in range(n):
           n_ahead = n_ahead.next
        
        while n_ahead:
            n_ahead = n_ahead.next
            curr = curr.next
        
        curr.next = curr.next.next

        return temp.next
        