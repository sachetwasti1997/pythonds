from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def find_balance(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left = find_balance(root.left)
            right = find_balance(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return False if find_balance(root) == -1 else True
