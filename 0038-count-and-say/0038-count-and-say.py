class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"        
        def next_number(s):
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                result.append("{}{}".format(count, s[i]))
                i += 1
            return ''.join(result)        
        current = "1"
        for _ in range(n - 1):
            current = next_number(current)        
        return current
solution = Solution()
print(solution.countAndSay(4)) 
print(solution.countAndSay(1))  