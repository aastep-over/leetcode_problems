# TODO: You are given the heads of two sorted linked lists list1 and list2.

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # create a dummy header
        header = ListNode(0)
        curr_node = header

        while list1 and list2:
            if list1.val < list2.val:
                curr_node.next = list1
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next
            curr_node = curr_node.next
        
        # attach the remaining list
        curr_node.next = list1 if list1 else list2

        return header.next 



if __name__ == '__main__':
    sol = Solution()
    list1 = [1,2,4] 
    list2 = [1,3,4]
    
    linked_list1 = []
    linked_list2 = []
    
    for i in range(len(list1)):
        if i == 0:
            node_list1 = ListNode(list1[0])
            linked_list1.append(node_list1)
            continue

        node_list1.next = ListNode(list1[i])
        node_list1 = node_list1.next
        linked_list1.append(node_list1)
        
    for j in range(len(list2)):
        if j == 0:
            node_list2 = ListNode(list2[0])
            linked_list2.append(node_list2)
            continue

        node_list2.next = ListNode(list2[j])
        node_list2 = node_list2.next
        linked_list2.append(node_list2)
    if len(list1) == 0:
        linked_list1.append(None)
    if len(list2) == 0:
        linked_list2.append(None)
    sorted_one_list = []
    output = sol.mergeTwoLists(linked_list1[0], linked_list2[0])
    while output != None:
        sorted_one_list.append(output.val)
        output = output.next

    print(sorted_one_list)

    
