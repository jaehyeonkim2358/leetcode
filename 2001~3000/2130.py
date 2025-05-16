# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        answer = 0
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next

        length = len(vals)
        for i in range(length // 2):
            answer = max(answer, vals[i] + vals[length - 1 - i])
        return answer
