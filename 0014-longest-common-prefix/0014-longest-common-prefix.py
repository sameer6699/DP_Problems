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

#Solution of the Given Problem Statement 
"""
Explanation:
1) Class Definition: The Solution class contains the longestCommonPrefix method.
2) Method longestCommonPrefix: This method takes a list of strings strs and returns the longest common prefix.
3) Initial Check: If strs is empty, return an empty string.
4) Initial Prefix: Start by assuming the entire first string is the common prefix.
5) Compare Each String: Iterate through the remaining strings in the list:
    Use the find method to check if the current string starts with the prefix.
    If the current string does not start with the prefix, shorten the prefix by one character and check again.
    Repeat this process until a common prefix is found or the prefix becomes empty.
6) Return the Result: After processing all strings, return the common prefix.

"""