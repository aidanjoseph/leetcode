class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digMap = {"2": {"a","b","c"}, 
                 "3": {"d", "e", "f"},
                 "4": {"g","h","i"},
                 "5": {"j","k","l"},
                 "6": {"m","n","o"},
                 "7": {"p", "q", "r", "s"},
                 "8": {"t", "u", "v"},
                 "9": {"w", "x", "y", "z"}
                }
        length = len(digits)
        res = []
        curr = []
        def backtrack(curr, currLen):
            if currLen == length:
                stringRes = "".join(curr)
                res.append(stringRes)
                return
            for letter in digMap[digits[currLen]]:
                curr.append(letter)
                backtrack(curr, currLen + 1)
                curr.pop()
        backtrack([], 0)
        return res
                


