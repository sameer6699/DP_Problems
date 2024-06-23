class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)
if __name__ == "__main__":
    solution = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    print(solution.strStr(haystack, needle))
    haystack = "leetcode"
    needle = "leeto"
    print(solution.strStr(haystack, needle))
