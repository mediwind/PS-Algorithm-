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
        OldToNew = {None: None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            OldToNew[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = OldToNew[cur]
            copy.next = OldToNew[cur.next]
            copy.random = OldToNew[cur.random]
            cur = cur.next
        
        return OldToNew[head]