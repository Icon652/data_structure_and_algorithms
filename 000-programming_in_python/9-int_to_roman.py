def int_to_roman(n):
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    
    roman = ''
    
    for value, symbol in sorted(roman_numerals.items(), reverse=True):
        while n >= value:
            roman += symbol
            n -= value
    
    return roman

if __name__ == "__main__":
    test_interger= 27
    print(int_to_roman(test_interger))
