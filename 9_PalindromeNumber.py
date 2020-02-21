'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''
# The followup in the instructions asked if I could solve this problem
# without using strings, so this is my solution without strings
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = 0
        find_size = 0
        keep_num = x
        y = x
        while (x > 0):
            x = x // 10
            find_size += 1
        while (keep_num > 0):
            num += (keep_num % 10) * (10 ** (find_size - 1))
            find_size -= 1
            keep_num = keep_num // 10
        if num == y:
            return True
        else:
            return False
