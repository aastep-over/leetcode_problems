from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, att='a'):
        self.val = val
        self.next = next
        self.att = att
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # return None if empty head
        if not head:
            return None

        zero_head = ListNode(0, head)

        while head.next:
            curr = head
            val = curr.val
   
            while (curr.next) and (curr.val == val):
                curr = curr.next
            
            # ensure no duplicate last
            if head.val == curr.val:
                head.next = None
            else:
                head.next = curr
                head = head.next
        
        return zero_head.next



if __name__ == '__main__':
    s = Solution()

    linked_list_1 = [ListNode(1), ListNode(1), ListNode(2)]
    for i in range(len(linked_list_1) - 1):
        linked_list_1[i].next = linked_list_1[i+1]


    unique_list = s.deleteDuplicates(linked_list_1[0])

    while unique_list:
        print(unique_list.val)
        unique_list = unique_list.next


    # Ex 2

    print('\n','EXAMPLE 2: ')
    print([1,1,2,3,3])
    linked_list_2 = [ListNode(1, att='a'), ListNode(1, att='b'), ListNode(2, att='c'), ListNode(3, att='d'), ListNode(3, att='e')]
    for i in range(len(linked_list_2) - 1):
        linked_list_2[i].next = linked_list_2[i+1]


    unique_list = s.deleteDuplicates(linked_list_2[0])

    while unique_list:
        print(unique_list.val)
        unique_list = unique_list.next


    # Ex3: Empty head

    print('\n','EXAMPLE 3: ')
    unique_list = s.deleteDuplicates(None)

    while unique_list:
        print(unique_list.val)
        unique_list = unique_list.next