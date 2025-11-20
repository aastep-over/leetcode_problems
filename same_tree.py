from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, up=None):
        self.val = val
        self.left = left
        self.right = right
        self.up = up
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # print(p.val, q.val)
        if not bool(p):
            return bool(q) == False
        if not bool(q):
            return bool(p) == False 
        
        if ((p.left == None) and (p.right == None)) and ((q.left == None) and (q.right == None)):
            is_same_node = p.val == q.val
            return is_same_node
        
        is_same_node = (p.val == q.val) and (bool(p.left) == bool(q.left)) and (bool(p.right) == bool(q.right))
        # print(p.val, q.val, is_same_node)
        

        if (p.left != None) and (q.left != None):
            # print('Left: ', p.val, q.val)
            is_same_node = is_same_node and self.isSameTree(p.left, q.left)
        # print(p.val, q.val)
        if (p.right != None) and (q.right != None):
            # print('Right: ', p.val, q.val)
            is_same_node = is_same_node and self.isSameTree(p.right, q.right) 

        return is_same_node



s = Solution()


# Ex1
p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)

p1.left = p2  
p1.right = p3
p_nodes = [p1, p2, p3]


q1 = TreeNode(1)
q2 = TreeNode(2)
q3 = TreeNode(3)

q1.left = q2  
q1.right = q3
q_nodes = [q1, q2, q3]

print(s.isSameTree(p_nodes[0], q_nodes[0]))

# Ex 2
p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)

p1.left = p2  
p1.right = p3
p_nodes = [p1, p2, p3]


q1 = TreeNode(1)
q2 = TreeNode(2)
q3 = TreeNode(3)
q4 = TreeNode(4)
q5 = TreeNode(5)

q1.left = q2  
q1.right = q3
q3.left = q4
q3.right = q5
q_nodes = [q1, q2, q3, q4, q5]

print(s.isSameTree(p_nodes[0], q_nodes[0]))