def romanToInt(self, s: str) -> int:
    roman_to_int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    current_val = 0
    for char in s[::-1]:
        val = roman_to_int_dict[char]
        if current_val <= val:
            result = result + val
        else:
            result = result - val
        current_val = val
    return result