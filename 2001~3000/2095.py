from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.getLength(head)
        if length == 1: return None

        cur = head
        pre = None
        for _ in range(length // 2):
            pre = cur
            cur = cur.next

        if cur and pre:
            pre.next = cur.next
        return head

    def getLength(self, head):
        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next
        return length
