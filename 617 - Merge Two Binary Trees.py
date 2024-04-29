class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        elif not t2:
            return t1
        else:
            res = TreeNode(t1.val + t2.val)
            res.left = self.mergeTrees(t1.left, t2.left)
            res.right = self.mergeTrees(t1.right, t2.right)
        return res
    
"""
Time Complexity = O(m + n)
Space Complexity = O(m + n)
"""