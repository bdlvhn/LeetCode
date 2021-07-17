class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = []
        for list_node in lists:
            while list_node:
                heapq.heappush(q, list_node.val)
                list_node = list_node.next
            
        root = step = ListNode(None)

        while q:
            now = heapq.heappop(q)
            step.next = ListNode(now)
            step = step.next

        return root.next