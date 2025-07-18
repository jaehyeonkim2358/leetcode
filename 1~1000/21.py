# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None

        head = ListNode()
        cur = head
        while list1 and list2:
            nxt1 = list1.next
            nxt2 = list2.next
            if list1.val < list2.val:
                cur.next = list1
                list1 = nxt1
            else:
                cur.next = list2
                list2 = nxt2
            cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return head.next
