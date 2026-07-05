# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        cnt = 0
        def dfs(node):
            nonlocal cnt, res
            if node is None or res is not None:
                return

            
            dfs(node.left)
            cnt+=1
            if cnt == k:
                res = node
                return
            dfs(node.right)

        dfs(root)
        return res.val
