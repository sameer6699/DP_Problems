class Solution(object):
    def isValid(self, s):        
        bracket_pairs = {')': '(', '}': '{', ']': '['} 
        stack = []      
        for char in s:
            if char in bracket_pairs:
                top_element = stack.pop() if stack else '#'
                if bracket_pairs[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

if __name__ == "__main__":
    solution = Solution()
    s1 = "()"
    print(solution.isValid(s1))
    s2 = "()[]{}"
    print(solution.isValid(s2))
    s3 = "(]"
    print(solution.isValid(s3))
