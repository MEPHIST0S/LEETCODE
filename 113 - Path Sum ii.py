"""
Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. 
A leaf is a node with no children.

Example:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
"""
# Define Tree
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
# === Main === 
class Recursive:
    def pathSum(self, root, targetSum):
        res = []
        if not root:
            return res
        
        def dfs(node, curr_path, curr_sum):
            if not node :
                return res
            
            curr_sum += node.val
            curr_path.append(node.val)
            
            if not node.left  and not node.right and curr_sum == targetSum:
                res.append(curr_path)

            
            dfs(node.left, curr_path, curr_sum)
            dfs(node.right, curr_path, curr_sum)
            
            curr_path.pop()
            curr_sum -= node.val
            
        dfs(root, [], 0)    
            
        return res
# === End Main ===

# # === Main === 
class Itterative:
    def pathSum(self, root, targetSum):

        if not root:
            return 

        res = []
        stack = [(root, root.val, [root.val])]
        
        while stack:
            node, curr_sum, curr_path = stack.pop()

            if not node.right and not node.left and curr_sum == targetSum:
                res.append(curr_path)
                
            if node.left:
                stack.append((node.left, curr_sum + node.left.val, curr_path + [node.left.val]))
            if node.right:
                stack.append((node.right, curr_sum + node.right.val, curr_path + [node.right.val]))
                
        return res
# # === End Main ===