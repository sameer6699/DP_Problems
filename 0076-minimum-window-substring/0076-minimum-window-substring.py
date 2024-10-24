from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # Dictionary which keeps a count of all the unique characters in t
        dict_t = Counter(t)
        
        # Number of unique characters in t which need to be present in the window
        required = len(dict_t)
        
        # Dictionary which keeps a count of all the unique characters in the current window
        window_counts = defaultdict(int)
        
        # Left and Right pointer
        l, r = 0, 0
        
        # The number of unique characters in the current window which match the required count in t
        formed = 0
        
        # ans tuple format will be (window length, left, right)
        ans = float("inf"), None, None
        
        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] += 1
            
            # If the frequency of the current character added matches the desired count in t, then increment the `formed` counter
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            # Try and contract the window till the point where it ceases to be 'desirable'
            while l <= r and formed == required:
                character = s[l]
                
                # Save the smallest window until now
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # The character at the position pointed by the `left` pointer is no longer a part of the window
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                # Move the left pointer ahead
                l += 1
            
            # Keep expanding the window once we are done contracting
            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

# Example usage:
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(solution.minWindow("a", "a"))                # Output: "a"
print(solution.minWindow("a", "aa"))               # Output: ""
