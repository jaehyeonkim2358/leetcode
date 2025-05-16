# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        node = head
        while node:
            node.val = arr.pop()
            node = node.next
        return head
