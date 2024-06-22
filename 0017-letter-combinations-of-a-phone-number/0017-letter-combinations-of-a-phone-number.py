class Solution(object):
    def letterCombinations(self, digits):    
        if not digits:
            return []
    
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(index, path):
            if len(path) == len(digits):
                result.append("".join(path))
                return    
            
            current_digit = digits[index]
            for letter in phone_map[current_digit]:                
                path.append(letter)                
                backtrack(index + 1, path)                
                path.pop()        
        result = []
        backtrack(0, [])
        return result
solution = Solution()
digits1 = "23"
print(solution.letterCombinations(digits1))

digits2 = ""
print(solution.letterCombinations(digits2))

digits3 = "2"
print(solution.letterCombinations(digits3))
