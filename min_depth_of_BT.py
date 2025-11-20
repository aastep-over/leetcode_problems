# TODO: Given a binary tree, find its minimum depth.

## cazzata
import sys
sys.path.append("d:\\Documents\\self_learning\\programming\\LeetCode\\test_folder")


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if (not root.left) and (not root.right):
            return 1
        
        left_st_depth, right_st_depth = 1, 1
        if root.left:
            left_st_depth += self.minDepth(root.left)
        if root.right:
            right_st_depth += self.minDepth(root.right)
        
        if left_st_depth == 1:
            return right_st_depth
        elif right_st_depth == 1:
            return left_st_depth
        else:
            return min(left_st_depth, right_st_depth) 




if __name__ == '__main__':
    sol = Solution()

    # Ex1

    # root = [3,9,20,null,null,15,7]
    print('Example 1. \n')
    node0 = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)

    node0.left, node0.right = node1, node2
    node2.left = node3
    node2.right = node4

    root = node0
    print("Expected:", 2, "\t", "Output:", sol.minDepth(root))

    # Ex2

    # root = [2,null,3,null,4,null,5,null,6]
    print('Example 2. \n')
    node0 = TreeNode(2)
    node1 = TreeNode(3)
    node2 = TreeNode(4)
    node3 = TreeNode(5)
    node4 = TreeNode(6)

    node0.right = node1
    node1.right = node2
    node2.right = node3
    node3.right = node4


    root = node0
    print("Expected:", 5, "\t", "Output:", sol.minDepth(root))

    


