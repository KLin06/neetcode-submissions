"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # iterate through list, create a dummy node for random 
        # populate it when you actually get to it
        nodes = {}
        dummy = curr = Node(0)
        while head:
            if head in nodes:
                curr.next = nodes[head]
            else:
                curr.next = Node(head.val)
                nodes[head] = curr.next
            
            if head.random and head.random not in nodes:
                nodes[head.random] = Node(head.random.val)
            if head.random:
                curr.next.random = nodes[head.random]

            curr = curr.next
            head = head.next

        return dummy.next

        