# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(root,big):
            nonlocal count
            if not root:
                return

            if root.val>=big:
                big=root.val
                count+=1
            
            dfs(root.left,big)
            dfs(root.right,big)
        dfs(root,-float("inf"))
        return count