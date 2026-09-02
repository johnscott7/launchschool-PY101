class RomanNumeral:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        conversions = [
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

        number = self.number
        result = ""

        for value, numeral in conversions:
            while number >= value:
                result += numeral
                number -= value

        return result