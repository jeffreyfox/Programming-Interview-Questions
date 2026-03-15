# solution using greedy lookup
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        result = []

        for value, symbol in values:
            while num >= value:
                result.append(symbol)
                num -= value

        return "".join(result)

# My solution using look up table. Readability improved by ChatGPT.
class Solution:
    def intToRoman(self, num: int) -> str:
        # (one, five, ten) symbols for ones, tens, hundreds
        symbols = [
            ("I", "V", "X"),
            ("X", "L", "C"),
            ("C", "D", "M"),
        ]

        def encode_digit(d: int, one: str, five: str, ten: str) -> str:
            if d <= 3:
                return one * d
            if d == 4:
                return one + five
            if d <= 8:
                return five + one * (d - 5)
            return one + ten   # d == 9

        parts = []
        place = 0

        while num > 0:
            digit = num % 10

            if place == 3:
                parts.append("M" * digit)
            else:
                one, five, ten = symbols[place]
                parts.append(encode_digit(digit, one, five, ten))

            num //= 10
            place += 1

        return "".join(reversed(parts))