from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break
        
        return h_index
if __name__ == "__main__":
    sol = Solution()
    citations1 = [3, 0, 6, 1, 5]
    print(sol.hIndex(citations1))
    citations2 = [1, 3, 1]
    print(sol.hIndex(citations2))