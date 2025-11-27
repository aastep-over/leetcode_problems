
# TODO: Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        n = len(nums)
        # border cases
        if n == 1:
            return nums[0]
        
        if n == 2:
            root = TreeNode(nums[0])
            root.right = TreeNode(nums[1])


        # Initialize BST
        bst = [TreeNode(0) for i in range(n)]
        if n % 2 == 0:
            i = n//2 -1
            j = n//2
            
        else:
            i, j = ((n+1) // 2) - 1, ((n+1) // 2) - 1

        root_idx = i
        # Add nodes based on their index in nums
        while (i > 0) and (j < n-1):
            lst = TreeNode(nums[i])
            rst = TreeNode(nums[j])
            
            lst.left = TreeNode(nums[i-1])
            rst.right = TreeNode(nums[j+1])
            
            bst[i], bst[j] = lst, rst
            
            i -= 1
            j += 1
            curr_bst = [(node.val, nodeValORNone(node.left), nodeValORNone(node.right)) for node in bst]


        # update left and right nodes of last lst, rst
        if i == 1:
            bst[i].left = TreeNode(nums[0])
        if j == n - 2:
            bst[j].right = TreeNode(nums[n-1])

        curr_bst = [(node.val, nodeValORNone(node.left), nodeValORNone(node.right)) for node in bst]
        
        # Add root node
        root = bst[root_idx]
        # if i == j:
        #     root = TreeNode(nums[i])
        #     root.left, root.right = bst[i-1], bst[j+1]
        #     bst[i] = root
        
        return root, bst
    
    def sortedArrayToBST2(self, nums: List[int]) -> Optional[TreeNode]:
        
        # Base Cases
        if len(nums) == 1:
            return TreeNode(nums[0])
        if len(nums) == 0:
            return None
        
        mid_pt = len(nums) // 2
        root = TreeNode(nums[mid_pt])
        
        left_node = self.sortedArrayToBST2(nums[:mid_pt])
        right_node = self.sortedArrayToBST2(nums[mid_pt+1:])

        root.left = left_node
        root.right = right_node

        return root 

def nodeValORNone(node: Optional[TreeNode]):
    if node:
        return node.val
    else:
        return 'null'

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
    s = Solution()

    # Ex.1
    nums = [-10, -3, 0, 5, 9] # [-20, -15, -10, -3, 0, 5, 9, 12, 14], [-25, -20, -15, -10, -3, 0, 5, 9, 12, 14, 18]
    print("Nums =", nums)
    # root, bst = s.sortedArrayToBST(nums)
    root = s.sortedArrayToBST2(nums)
    print(root.val, nodeValORNone(root.left), nodeValORNone(root.right))
    print(traversalBST(root))
    # print([(node.val, nodeValORNone(node.left), nodeValORNone(node.right)) for node in bst])

    print("\nNaive: ")
    test_bst = []
    node0 = TreeNode(0)
    node1 = TreeNode(-3)
    node2 = TreeNode(9)
    node3 = TreeNode(-10)
    node4 = TreeNode(5)

    node0.left, node0.right = node1, node2
    node1.left = node3
    node2.left = node4

    root2 = node0
    print(traversalBST(root2))
