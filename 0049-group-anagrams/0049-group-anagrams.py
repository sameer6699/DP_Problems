from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) 
        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s) 
        return list(anagrams.values())
if __name__ == "__main__":
    solution = Solution()
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: {strs1}\nOutput: {solution.groupAnagrams(strs1)}\n")
    strs2 = [""]
    print(f"Input: {strs2}\nOutput: {solution.groupAnagrams(strs2)}\n")
    strs3 = ["a"]
    print(f"Input: {strs3}\nOutput: {solution.groupAnagrams(strs3)}\n")
