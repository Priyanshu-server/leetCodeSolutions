# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        stack = self.traverse(root)
        return stack
    def traverse(self,root,stack = []):
        if root:
            self.traverse(root.right)
            stack.append(root.val)
            self.traverse(root.left)
        return stack


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

sol = Solution()
print(sol.inorderTraversal(tree))