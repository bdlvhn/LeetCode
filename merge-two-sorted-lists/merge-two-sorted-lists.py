# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = l1, l2
        answer = ListNode(None)
        node = answer
        
        while s1 and s2:
            if s1.val < s2.val:
                node.next = ListNode(s1.val)
                node = node.next
                s1 = s1.next
            else:
                node.next = ListNode(s2.val)
                node = node.next
                s2 = s2.next
        
        if s1:
            node.next = s1
        if s2:
            node.next = s2
        
        return answer.next