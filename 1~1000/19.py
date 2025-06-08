# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLength(head)
        if length == 1: return None

        index = length - n
        cur = head
        pre = None
        idx = 0
        while cur:
            if idx == index:
                if pre: pre.next = cur.next
                else:
                    head = cur.next
                break
            pre = cur
            cur = cur.next
            idx += 1

        return head

    def getLength(self, node):
        cur = node
        length = 0
        while cur:
            cur = cur.next
            length += 1
        return length
