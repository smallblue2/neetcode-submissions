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
        inorder_trav = self._inorder(root)
        print(inorder_trav)
        sorted_list = sorted(inorder_trav)
        set_items = sorted(list(set(inorder_trav)))
        return inorder_trav == sorted(inorder_trav) and  set_items == inorder_trav
        # root.left < root.val < root.right
        # if root is None:
        #     print("None -> True")
        #     return True

        # valid = True

        # if root.left is not None:
        #     if not root.left.val < root.val:
        #         valid = False
        # if root.right is not None:
        #     if not root.right.val > root.val:
        #         valid = False

        # print(f"val: {root.val} ({root.left.val if root.left is not None else 'None'}, {root.right.val if root.right is not None else 'None'}) -> {valid}")
        
        # return valid and self.isValidBST(root.left) and self.isValidBST(root.right)

    def _inorder(self, root):
        if root is None:
            return []

        return self._inorder(root.left) + [root.val] + self._inorder(root.right)