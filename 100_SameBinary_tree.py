# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        same_or__not = self.isSame(p,q)
        return same_or__not

    def isSame(self,p,q):
        if p == None and q == None:
            return True
        if (p and q) and (p.val == q.val):
            return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
        else:
            return False



p = TreeNode(1)
p.right = TreeNode(2)
p.right.left = TreeNode(3)

q = TreeNode(1)
q.right = TreeNode(2)
q.right.left = TreeNode(3)

sol = Solution()
print(sol.isSameTree(p, q))



#Also a nice solution 
def isSameTree2(self, p, q):
    stack = [(p, q)]
    while stack:
        node1, node2 = stack.pop()
        if not node1 and not node2:
            continue
        elif None in [node1, node2]:
            return False
        else:
            if node1.val != node2.val:
                return False
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
    return True

# IF WE FIND ANy false it will return immediately not like recursive