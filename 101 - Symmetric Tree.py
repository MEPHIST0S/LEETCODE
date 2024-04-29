class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def preOrder(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2 or n1.val != n2.val:
                return False
            return preOrder(n1.left, n2.right) and preOrder(n1.right, n2.left)
        if not root:
            return False
        return preOrder(root.left, root.right)

"""
Time Complexity = O(n)
Space Complexity = O(n)
"""