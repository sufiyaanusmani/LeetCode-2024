# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorder(self, root, l):
        if root is None:
            return
        l.append(root.val)
        self.preorder(root.left, l)
        self.preorder(root.right, l)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        self.preorder(root, l)
        return l

        