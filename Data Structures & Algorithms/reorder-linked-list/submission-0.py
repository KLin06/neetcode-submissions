# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return 

        curr = slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        rev_head = slow.next
        slow.next = None

        prev = None
        while rev_head:
            dummy = rev_head.next
            rev_head.next = prev
            prev = rev_head
            rev_head = dummy

        while prev:
            dummy = curr.next
            curr.next = prev
            prev = prev.next
            curr.next.next = dummy
            curr = curr.next.next
        
        