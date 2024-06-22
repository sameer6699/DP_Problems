class Solution(object):
    def intToRoman(self, num):
        val_to_roman = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]    
        roman_numeral = ''
        for val, roman in val_to_roman:            
            while num >= val:
                roman_numeral += roman
                num -= val
        return roman_numeral
solution = Solution()
print(solution.intToRoman(3749))
print(solution.intToRoman(58))    
print(solution.intToRoman(1994))  
