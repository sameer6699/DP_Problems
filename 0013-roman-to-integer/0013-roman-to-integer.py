class Solution(object):
    def romanToInt(self, s):        
        roman_to_val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0    
        for i in range(len(s)):
            if i < len(s) - 1 and roman_to_val[s[i]] < roman_to_val[s[i + 1]]:
                total -= roman_to_val[s[i]]
            else:
                total += roman_to_val[s[i]]        
        return total
solution = Solution()
print(solution.romanToInt("III"))     
print(solution.romanToInt("LVIII"))   
print(solution.romanToInt("MCMXCIV"))
