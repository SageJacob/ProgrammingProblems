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
