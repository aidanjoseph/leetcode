class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        res = 0
        seen = {}
        curr = 0
        for right, letter in enumerate(s):
            if letter not in seen:
                curr += 1
                seen[letter] = right
            else:
                if seen[letter] < left:
                    curr += 1
                    seen[letter] = right
                else:
                    left = seen[letter] + 1
                    seen[letter] = right
                    curr = right - left + 1
            res = max(curr, res)
        return res
            

        