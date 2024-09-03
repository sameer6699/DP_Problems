class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is "0", return "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize the result array
        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)
        
        # Multiply each digit in num1 with each digit in num2
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                # Multiply the current digits
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                # Determine the position in the result array
                p1, p2 = i + j, i + j + 1
                
                # Add to the current position and manage carry
                sum = mul + result[p2]
                result[p2] = sum % 10
                result[p1] += sum // 10
        
        # Convert the result array to a string, skipping leading zeros
        result_str = ''.join(map(str, result)).lstrip('0')
        
        return result_str

# Driver code
solution = Solution()
print(solution.multiply("2", "3"))  # Output: "6"
print(solution.multiply("123", "456"))  # Output: "56088"