
# TODO: Given the root of a binary tree and an integer targetSum,
# return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # no root
        if not root:
            return False
        has_path_sum = self.auxFunc(root, targetSum)

        return has_path_sum

    def auxFunc(self, root: Optional[TreeNode], targetSum: int, prev_node_val=0) -> bool:

        # child nodes
        if (not root.left) and (not root.right):
            has_path_sum = prev_node_val + root.val == targetSum
            return has_path_sum
        
        prev_node_val += root.val
        if root.left:
            left_has_path_sum = self.auxFunc(root.left, targetSum, prev_node_val)
        else:
            left_has_path_sum = False
        
        if root.right:
            right_has_path_sum = self.auxFunc(root.right, targetSum, prev_node_val)
        else:
            right_has_path_sum = False
        
        
        return left_has_path_sum or right_has_path_sum


if __name__ == '__main__':
    sol = Solution()

    # Ex1

    # root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    print('Example 1. \n')
    node0 = TreeNode(5)
    node1 = TreeNode(4)
    node2 = TreeNode(8)
    node3 = TreeNode(11)
    node4 = TreeNode(13)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    node7 = TreeNode(2)
    node8 = TreeNode(1)

    node0.left, node0.right = node1, node2
    node1.left = node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    node5.right = node8

    root = node0
    print("Expected:", 'True', "\t", "Output:", sol.hasPathSum(root, 22))

    # Ex2

    # root = [1,2,3], targetSum = 5
    print('Example 2. \n')
    node0 = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)

    node0.left, node0.right = node1, node2


    root = node0
    print("Expected:", 'False', "\t", "Output:", sol.hasPathSum(root, 5))

    
    # Ex3

    # root = [], targetSum = 0
    print('Example 3. \n')

    root = None
    print("Expected:", 'False', "\t", "Output:", sol.hasPathSum(root, 0))
