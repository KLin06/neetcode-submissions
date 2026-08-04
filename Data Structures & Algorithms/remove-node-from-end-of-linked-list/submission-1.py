# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = curr = ListNode()
        temp.next = n_ahead = head

        i = 0
        while n_ahead:
            n_ahead = n_ahead.next
            if i >= n:
                curr = curr.next
            i += 1
        
        curr.next = curr.next.next

        return temp.next
        