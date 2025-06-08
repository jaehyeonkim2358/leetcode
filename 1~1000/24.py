# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        if length <= 1: return head
        length = length // 2 * 2

        v1 = head
        v2 = head.next
        i = 0
        while i < length:
            nxt_v1 = v2.next
            nxt_v2 = v2.next.next if v2.next else None
            v2.next = v1
            v1.next = nxt_v2 if nxt_v2 else nxt_v1
            if i == 0:
                head = v2
            v1 = nxt_v1
            v2 = nxt_v2
            i += 2
        return head
