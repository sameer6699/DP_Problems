class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
        return answer
solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))  
print(solution.dailyTemperatures([30,40,50,60]))  
print(solution.dailyTemperatures([30,60,90]))  