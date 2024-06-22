class Solution(object):
    def longestCommonPrefix(self, strs):    
        if not strs:
            return ""     
        prefix = strs[0]        
        for s in strs[1:]:
            while s.find(prefix) != 0:                
                prefix = prefix[:-1]
                if not prefix:
                    return ""        
        return prefix
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))     
print(solution.longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  
print(solution.longestCommonPrefix(["throne", "dungeon"]))        
print(solution.longestCommonPrefix(["throne", "throne"]))     
