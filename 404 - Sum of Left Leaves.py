"""Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node. 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
"""
# Define Tree
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
# === Main === 
class Recursive:
    def sumOfLeftLeaves(self, root):
        def dfs(node):
            if not node:
                return 0
            
            total = 0
            
            if node.left and not node.left.right and not node.left.left:
                total += node.left.val
            
            sumr = dfs(node.right)
            suml = dfs(node.left)
            
            return total + sumr + suml
        
        return dfs(root)
# === End Main ===

# # === Main === 
class Itterative:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        
        res = 0
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            
        return res
# # === End Main ===