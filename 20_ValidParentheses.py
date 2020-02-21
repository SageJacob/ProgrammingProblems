'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        opening =   ['(', '{', '[']
        closed = [')', '}', ']']
        stack = []
        top = -1
        findIndex = 0
        for char in range(len(s)):
            if s[char] in opening or s[char] in closed:
                # Add to the stack if the char is an opening paren
                if s[char] in opening:
                    stack.append(s[char])
                    top += 1
                # If the char is a closing paren, check the top of the stack for a match
                if s[char] in closed:
                    findIndex = closed.index(s[char])
                    # If the stack is empty but char is in closed, return False
                    if top < 0:
                        return False
                    if stack[top] == opening[findIndex]:
                        stack.pop(top)
                        top -= 1
                    else:
                        return False
        # If there are no more chars and stack still has parens, return False
        if len(stack) != 0:
            return False
        return True
