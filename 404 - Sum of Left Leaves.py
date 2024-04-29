class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node, is_left):
            if not node:
                return 0 
            if not node.left and not node.rigth and is_left:
                return node.val
            left_sum = traverse(node.left, True)
            right_sum = traverse(node.right, False)
            return left_sum + right_sum
        return traverse(root, False)
    
"""
Time Complexity = O(n)
Space Complexity = O(h)
"""