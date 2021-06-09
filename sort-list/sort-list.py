class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        def mergeSort(node: ListNode):
            if node.next is None:
                return node
            
            root = follower = runner = ListNode(None)
            follower.next = node
            runner.next = node
            
            while runner and runner.next:
                follower = follower.next
                runner = runner.next.next
            
            newer = follower.next
            follower.next = None
            root = root.next
            
            answer = result = ListNode(None)
            a = mergeSort(root)
            b = mergeSort(newer)
            while a and b:
                if a.val > b.val:
                    result.next = b
                    b = b.next
                else:
                    result.next = a
                    a = a.next
                result = result.next
                
            if a:
                result.next = a
            else:
                result.next = b

            return answer.next
        
        return mergeSort(head)