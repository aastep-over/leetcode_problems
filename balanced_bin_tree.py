
# TODO: Given a binary tree, determine if it is height-balanced.

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def auxBinTree(self, root: Optional[TreeNode]) -> (int, bool):
        if not bool(root):
            return 0, True

        if (root.left == None) and (root.right == None):
            return 1, True

        balanced = True
        left_st_depth = 0
        right_st_depth = 0
        
        l_depth, is_l_balanced = self.auxBinTree(root.left)
        left_st_depth += l_depth
        
        r_depth, is_r_balanced = self.auxBinTree(root.right)
        right_st_depth += r_depth

        diff = abs(left_st_depth - right_st_depth)

        balanced = balanced and is_l_balanced and is_r_balanced and diff <= 1

        return 1 + max(left_st_depth, right_st_depth) , balanced

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not bool(root):
            return True
        
        is_balanced = self.auxBinTree(root)[1]

        return is_balanced

def traversalBST(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    
    queue, result = deque([root]), []
    
    while queue:
        node = queue.popleft()
        result.append(node.val)  # Process the node
        
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        queue_vals = [node.val for node in queue]
    
    return result



if __name__ == '__main__':
    sol = Solution()

    # Ex1
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
    print("Expected:", True, "\t", "Output:", sol.isBalanced(root))

    print(traversalBST(root))

    print('\n---------------------------------------------------\n')

    # Ex2
    print('Example 2. \n')
    node0 = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)

    node0.left, node0.right = node1, node2
    node1.left, node1.right = node3, node4
    node3.left, node3.right = node5, node6

    root = node0
    print("Expected:", False, "\t", "Output:", sol.isBalanced(root))

    print('\n---------------------------------------------------\n')

    # Ex 3
    print('Example 3. \n')
    root = None
    print("Expected:", True, "\t", "Output:", sol.isBalanced(root))

    print('\n---------------------------------------------------\n')

    # Ex 4
    print('Example 4. \n')
    node0 = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)

    node0.left, node0.right = node1, node2
    node1.left = node3
    node2.right = node4
    node3.left = node5
    node4.right = node6

    root = node0
    print("Expected:", False, "\t", "Output:", sol.isBalanced(root))
    print(traversalBST(root))
