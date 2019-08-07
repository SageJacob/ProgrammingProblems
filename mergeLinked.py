# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        makeHead = 0
        if not l1 or not l2:
            return l1 or l2

        while l1 is not None and l2 is not None:
            # If head is not yet established, create one
            if makeHead == 0:
                makeHead += 1
                if l1.val < l2.val:
                    head = ListNode(l1.val)
                    l1 = l1.next
                    temp = head
                    continue
                else:
                    head = ListNode(l2.val)
                    l2 = l2.next
                    temp = head
                    continue
            # If l1 < l2, add l1 to our linked list
            if l1.val < l2.val:
                node = ListNode(l1.val)
                temp.next = node
                temp = temp.next
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                temp.next = node
                temp = temp.next
                l2 = l2.next
        # If l1 is empty (l2 is longer) just extend the rest of l2 to our linked list
        if l1 is None:
            while l2 is not None:
                node = ListNode(l2.val)
                temp.next = node
                temp = temp.next
                l2 = l2.next
        else:
            while l1 is not None:
                node = ListNode(l1.val)
                temp.next = node
                temp = temp.next
                l1 = l1.next
        return head
