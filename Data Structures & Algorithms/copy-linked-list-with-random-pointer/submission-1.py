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
        numset={}
        cur=head
        def doit(node):
            if not node:
                return None
            
            if node in numset:
                return numset[node]
            temp=Node(node.val)
            numset[node]=temp
            temp.next=doit(node.next)
            temp.random=doit(node.random)
            return temp
                
        copy=doit(cur)
        return copy

