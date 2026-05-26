# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Inorder traversal should create a sorted, ascending list.
# Traverse the tree itself and check properties live

# 5 (4 (3, n), 6 (n, 7))


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Every node in the left subtree needs to be less than val
        # Every node in the right subtree needs to be more than val

        return self.rangeInorderCheck(root)

    
    def rangeInorderCheck(self, root, lower=-1000, upper=1000):
        if root is None:
            return True

        valid = True

        if not root.val < upper:
            valid = False
        if not root.val > lower:
            valid = False

        return valid and self.rangeInorderCheck(root.left, lower, root.val) and self.rangeInorderCheck(root.right, root.val, upper)
