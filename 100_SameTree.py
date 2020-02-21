'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def check(p, q):
    if not p or not q:
        if not p and not q:
            return True
        else:
            return False
    if p.val != q.val:
        return False
    return check(p.left, q.left) and check(p.right, q.right)


class Solution(object):
    def isSameTree(self, p, q):
        return check(p, q)
