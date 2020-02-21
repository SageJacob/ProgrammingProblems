'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        value1 = 0
        value2 = 0
        multiply = 1
        while (l1):
            value1 = value1 + l1.val * multiply
            multiply = multiply * 10
            l1 = l1.next
        multiply = 1
        while (l2):
            value2 = value2 + l2.val * multiply
            multiply = multiply * 10
            l2 = l2.next
        reverse = value1 + value2
        newList = ListNode(0)
        head = newList
        while (reverse > 0):
            newList.val = reverse % 10
            reverse = reverse // 10
            if (reverse > 0):
                newList.next = ListNode(0)
                newList = newList.next
        return head
