class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        
        # get length 
        length,tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
            
        k = k % length
        if k == 0:
            return head
        
        # move to pivot and rotate
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        new_head=cur.next
        cur.next=None
        tail.next=head
        return new_head