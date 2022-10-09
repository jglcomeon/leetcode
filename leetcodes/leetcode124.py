# Definition for a binary tree node.
from json import tool
import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        res = -sys.maxsize
        def DFS(root):
            if not root:
                return -sys.maxsize
            nonlocal res
            left = self.maxPathSum(root.left)
            right = self.maxPathSum(root.right)
            res = max(res, left, right, root.val, root.val+left, root.val + right, root.val + left + right)
            print(res, left, right, root.val, root.val+left, root.val + right, root.val + left + right)

            return max(root.val, root.val+left, root.val + right)
        DFS(root)
        return res
if __name__ == '__main__':
    s =Solution()
    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(-1)
    root.right.left = TreeNode(-2)
    s.maxPathSum(root)