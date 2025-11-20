from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, lst: Optional[TreeNode], rst: Optional[TreeNode]) -> bool:
        
        if ((lst.left == None) and (lst.right == None)) and ((rst.left == None) and (rst.right == None)):
            return lst.val == rst.val
        
        is_symmetric = lst.val == rst.val
        if lst.left != None:
            if bool(rst.right):
                is_symmetric = is_symmetric and self.isSymmetric(lst.left, rst.right)
            else:
                is_symmetric = False
                return False # early exit since can't be symmetric anymore
        
        if lst.right != None:
            if bool(rst.left):
                is_symmetric = is_symmetric and self.isSymmetric(lst.right, rst.left)
            else:
                is_symmetric = False
                return False # early exit since can't be symmetric anymore
        
        return is_symmetric



s = Solution()


# Ex1
p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(2)
p4 = TreeNode(3)
p5 = TreeNode(4)
p6 = TreeNode(4)
p7 = TreeNode(3)

p1.left = p2  
p1.right = p3
p2.left = p4
p2.right = p5
p3.left = p6
p3.right = p7
p_nodes = [p1, p2, p3, p4, p5, p6, p7]

print(s.isSymmetric(p1, p1))


# Ex 2
p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(2)
p4 = TreeNode(3)
p5 = TreeNode(3)

p1.left = p2  
p1.right = p3
p2.right = p4
p3.right = p5
p_nodes = [p1, p2, p3, p4, p5]

print(s.isSymmetric(p1, p1))

# Ex3
p1 = TreeNode(1)
print(s.isSymmetric(p1, p1))