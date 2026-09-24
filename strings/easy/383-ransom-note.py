class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store = Counter(magazine)

        for letter in ransomNote:
            if letter not in store:
                return False
            elif store[letter] == 0:
                return False
            else:
                store[letter] -= 1
        return True
            
        