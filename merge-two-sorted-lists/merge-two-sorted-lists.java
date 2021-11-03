/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode root = new ListNode();
        ListNode result = root;

        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                result.next = new ListNode(l1.val);
                result = result.next;
                l1 = l1.next;
            }
            else {
                result.next = new ListNode(l2.val);
                result = result.next;
                l2 = l2.next;
            }
        }
        result.next = (l1 == null ? l2 : l1);

        return root.next;
    }
}