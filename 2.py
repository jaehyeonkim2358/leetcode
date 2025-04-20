# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curl1 = l1
        curl2 = l2
        root = ListNode(0)
        node = root

        # l1, l2 중 하나라도 남은 노드가 있으면 반복
        while curl1 != None or curl2 != None:
            value = node.val
            if curl1 != None: value += curl1.val
            if curl2 != None: value += curl2.val

            node.val = value % 10
            new_node_value = value // 10

            if curl1 != None: curl1 = curl1.next
            if curl2 != None: curl2 = curl2.next

            # l1, l2 중 하나라도 끝에 도달하지 않았거나, 모두 끝에 도달했더라도 new_node_value가 0보다 클 때
            if (curl1 != None or curl2 != None) or new_node_value > 0:
                new_node = ListNode(new_node_value)
                node.next = new_node
                node = node.next

        return root
