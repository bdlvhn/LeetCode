# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        numbers = [0,0]
        n1, n2 = l1, l2
        ten = 1
        while n1:
            numbers[0] += n1.val * ten
            ten *= 10
            n1 = n1.next
        
        ten = 1
        while n2:
            numbers[1] += n2.val * ten
            ten *= 10
            n2 = n2.next
        result = sum(numbers)
        
        node = prev = ListNode(None)
        
        if result == 0:
            return ListNode()
        else:
            while result:
                prev.next = ListNode(result % 10)
                prev = prev.next
                result = result // 10

            return node.next