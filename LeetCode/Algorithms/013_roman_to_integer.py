# SOlution using a dict for just single characters numerals. Look ahead by one and
# add or substract current value from total sum.

# Solution using a dict for both single and double character numerals
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        total = 0
        i = 0
        while i < len(s):
            # First match two characters, if not, then match one
            if i + 1 < len(s) and s[i:i+2] in d:
                total += d[s[i:i+2]]
                i += 2
            else:
                total += d[s[i]]
                i += 1
        return total
