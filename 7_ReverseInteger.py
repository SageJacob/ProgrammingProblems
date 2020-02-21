'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        find_size = 0
        flag = 0
        if x < 0:
            x *= -1
            flag = 1
        keep_num = x
        while (x > 0):
            x = x // 10
            find_size += 1
        while (keep_num > 0):
            num += (keep_num % 10) * (10 ** (find_size - 1))
            find_size -= 1
            keep_num = keep_num // 10
        if flag == 1:
            num *= -1
        if num > (2 ** 31) - 1 or num < (2 ** 31) * -1:
            return 0
        return num
