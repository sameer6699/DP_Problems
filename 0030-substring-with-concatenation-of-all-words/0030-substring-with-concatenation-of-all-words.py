from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_length = len(words[0])
        total_words = len(words)
        total_length = word_length * total_words
        word_count = Counter(words)
        result = []
        for i in range(word_length):
            left = i
            right = i
            window_word_count = Counter()
            words_used = 0
            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length
                if word in word_count:
                    window_word_count[word] += 1
                    words_used += 1
                    while window_word_count[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        window_word_count[left_word] -= 1
                        words_used -= 1
                        left += word_length
                    if words_used == total_words:
                        result.append(left)
                else:
                    window_word_count.clear()
                    words_used = 0
                    left = right
            
        return result
s = "barfoothefoobarman"
words = ["foo", "bar"]
solution = Solution()
print(solution.findSubstring(s, words)) 