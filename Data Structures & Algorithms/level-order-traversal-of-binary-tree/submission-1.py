# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        pri=deque([root])
        while pri:
            mini=[]
            for _ in range(len(pri)):
                node=pri.popleft()
                mini.append(node.val)
                if node.left:
                    pri.append(node.left)
                if node.right:
                    pri.append(node.right)
            res.append(mini)
        return res
