# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0, head)
        cur = temp
        while cur.next and cur.next.next:
            # ...cur->v1->v2...
            v1 = cur.next
            v2 = cur.next.next

            v1.next = v2.next
            v2.next = v1
            cur.next = v2
            cur = v1
        return temp.next
