# Define Tree
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
# === Main === 
class Recursive:
    def reverseOddLevels(self, root):
        def dfs(left, right, level):
            if not left or not right:
                return
            if level%2 == 1:
                left.val, right.val = right.val, left.val
            dfs(left.left, right.right, level+1)
            dfs(right.left, left.right, level+1)
        
        dfs(root.left, root.right, 1)
        return root
# === End Main ===

# # === Main === 
class Itterative:
    def reverseOddLevels(self, root):
        if not root:
            return []
        
        tree = [root]
        level = 0

        while tree:
            for _ in range(len(tree)):
                node = tree.pop(0)
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
            level += 1

            if level%2 != 0:
                l, r = 0 , len(tree) - 1
                while l < r:
                        tree[l].val, tree[r].val = tree[r].val, tree[l].val
                        l += 1
                        r -= 1
        return root
# # === End Main ===