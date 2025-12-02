class RomanConverter:
    def to_roman(self, num):
        if not isinstance(num, int) or not (0 < num < 4000):
            return "Please enter an integer between 1 and 3999."
        roman_map = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        roman_numeral = ""
        for value, numeral in sorted(roman_map.items(), reverse=True):
            while num >= value:
                roman_numeral += numeral
                num -= value
        return roman_numeral
user_input = int(input("Enter an integer to convert to Roman numeral: "))
converter = RomanConverter()
result = converter.to_roman(user_input)
print(f"The Roman numeral equivalent is: {result}")