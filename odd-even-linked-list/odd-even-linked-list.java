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
    public ListNode oddEvenList(ListNode head) {
        ListNode l1 = new ListNode();
        ListNode l2 = new ListNode();
        ListNode odd = l1;
        ListNode even = l2;
        
        int index = 0;
        while (head != null) {
            if (index % 2 == 0) {
                even.next = head;
                even = even.next;
            } else {
                odd.next = head;
                odd = odd.next;
            }
            head = head.next;
            index++;
        }
        
        odd.next = null;
        even.next = l1.next;
        return l2.next;
    }
}