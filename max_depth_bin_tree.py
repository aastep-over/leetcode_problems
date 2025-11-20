# TODO: Given the root of a binary tree, return its maximum depth.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth1(self, root: Optional[TreeNode], curr_depth: int) -> int:
        if (root.left == None) and (root.right == None):
            return curr_depth
        
        max_depth = curr_depth
        if root.left != None:
            left_depth = self.maxDepth1(root.left, curr_depth+1)
            if left_depth > max_depth:
                max_depth = left_depth
        
        if root.right != None:
            right_depth = self.maxDepth1(root.right, curr_depth+1)
            if right_depth > max_depth:
                max_depth = right_depth

        return max_depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not bool(root):
            return 0
        
        max_depth = self.maxDepth1(root, 1)

        return max_depth


if __name__ == '__main__':
    s = Solution()
    
    # Ex1
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)

    p1.left = p2  
    p1.right = p3
    p3.left = p4
    p3.right = p5
    p_nodes = [p1, p2, p3, p4, p5]

    print(s.maxDepth(p1))

    # Ex2
    p1 = TreeNode(1)
    p2 = TreeNode(2)

    p1.right = p2
    p_nodes = [p1, p2]

    print(s.maxDepth(p1))
        