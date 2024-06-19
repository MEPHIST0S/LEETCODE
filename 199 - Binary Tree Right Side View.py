""" 
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
"""

# Define Tree
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
# === Main === 
class Recursive:
    def rightSideView(self, root):
        res = []
        
        def dfs(node, level):
            if not node:
                return
            
            if level == len(res):
                res.append(node.val)
            
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return res
# === End Main ===

# # === Main === 
class Itterative:
    def rightSideView(self, root):
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            level_len = len(queue)

            for i in range(level_len):
                node = queue.pop(0)

                if i == level_len - 1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return res
# # === End Main ===