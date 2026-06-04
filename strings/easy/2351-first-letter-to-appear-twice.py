'''
pretty calm
just did cuz saw video
did O(26) ~ o(1) space
techcnailly hashset same thing but this is slightly more fun
'''
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = [0] * 26
        for char in s:
            code = ord(char) - 97
            if seen[code] == 1:
                return char
            seen[code] += 1
        
        