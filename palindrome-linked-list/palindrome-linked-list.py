class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = ListNode()
        step = head

        while step:
            temp = ListNode()
            temp.val, temp.next = step.val, node
            node = temp
            step = step.next
        
        while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True