class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        number = 0
        s = s[::-1]
        previous_letter = 0
        while(s):
            current_letter = roman_numerals.get(s[0])
            # For example, IV is V - I (5 - 1 = 4)
            if current_letter < previous_letter:
                number -= current_letter
            else:
                number += current_letter
            previous_letter = current_letter
            s = s[1:]
        return number
