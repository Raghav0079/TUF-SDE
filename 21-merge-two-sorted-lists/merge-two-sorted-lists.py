# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
       
        dummy_node = ListNode(-1)
        temp = dummy_node

      
        while list1 is not None and list2 is not None:
            
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

      
        if list1 is not None:
            temp.next = list1
        else:
            temp.next = list2

        
        return dummy_node.next