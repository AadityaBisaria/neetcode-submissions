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
        seen={None:None}
        cur=head

        while cur:
            copy=Node(cur.val)
            seen[cur]=copy
            cur=cur.next

        cur=head
        while cur:
            copy=seen[cur]
            copy.next=seen[cur.next]
            copy.random=seen[cur.random]
            cur=cur.next
        return seen[head]