# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, root, l):
        if root is None:
            return
        self.inorder(root.left, l)
        l.append(root.val)
        self.inorder(root.right, l)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        self.inorder(root, l)
        return l

        