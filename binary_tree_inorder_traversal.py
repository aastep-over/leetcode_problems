from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not bool(root):
            return []

        if (root.left == None) and (root.right == None):
            return [root.val]
        
        output = []
        if root.left != None:
            output += self.inorderTraversal(root.left)
        
        output += [root.val]
        if root.right != None:
            output += self.inorderTraversal(root.right)
        
        return output
    
    def treeNodesFromList(self, node_vals: List[int]) -> List[int]:
        nodes = []
        last_index = 0
        j = 0
        while last_index < len(node_vals) - 1:
            if node_vals[j] != None:
                node = TreeNode(node_vals[j])
                node.left = TreeNode(node_vals[last_index + 1])
                if (last_index + 2) < len(node_vals):
                    node.right = TreeNode(node_vals[last_index + 2])
                nodes.append(node)
                last_index += 2
            j += 1
        print(j)
        while j < len(node_vals):
            nodes.append(TreeNode(node_vals[j]))
            j += 1
        
        return nodes


s = Solution()

# Ex 1
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.right = node2
node2.left = node3
nodes = [node1, node2, node3]

# node_vals = [1,None,2,3]
# nodes = s.treeNodesFromList(node_vals)
# print([node.val for node in nodes])
# for node in nodes:
#     left = node.left.val if node.left != None else None
#     right = node.right.val if node.right != None else None
#     print(node.val, left, right)

 
print(s.inorderTraversal(nodes[0]))

# Ex 2

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)

node1.left, node1.right = node2, node3
node2.left, node2.right = node4, node5
node3.left, node3.right = None, node8
node4.left, node4.right = None, None
node5.left, node5.right = node6, node7
node6.left, node6.right = None, None
node7.left, node7.right = None, None
node8.left, node8.right = node9, None
node9.left, node9.right = None, None
nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9]

# node_vals = [1,2,3,4,5,None,8,None,None,6,7,9]
# nodes = s.treeNodesFromList(node_vals)
print(s.inorderTraversal(nodes[0]))
# nodes = []
# last_index = 0
# j = 0
# while last_index < len(node_vals) - 1:
#     # print(j, last_index)
#     if node_vals[j] != None:
#         node = TreeNode(node_vals[j])
#         node.left = TreeNode(node_vals[last_index + 1])
#         if (last_index + 2) < len(node_vals):
#             node.right = TreeNode(node_vals[last_index + 2])
#         nodes.append(node)
#         last_index += 2
#     j += 1
# print([node.val for node in nodes])
# # for node in nodes:
# #     left = node.left.val if node.left != None else None
# #     right = node.right.val if node.right != None else None
# #     print(node.val, left, right)

