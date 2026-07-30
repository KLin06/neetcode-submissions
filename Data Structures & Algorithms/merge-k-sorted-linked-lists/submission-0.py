# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        pq = []
        head = node = ListNode()

        for i in range(k):
            pq.append((lists[i].val, i, lists[i]))

        heapq.heapify(pq)

        while pq:
            val, i, curr = heapq.heappop(pq)

            node.next = curr
            node = curr

            if curr.next:
                heapq.heappush(pq, (curr.next.val, i, curr.next))
                
        return head.next