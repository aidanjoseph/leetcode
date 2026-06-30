from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        # two pointer
        #left and right
        #if cross then either know its a odd num of words
        #or we reached a space
        s = s.strip()
        q = deque([])
        word = ""
        for char in s:
            if char != " ":
                word += char
            else:
                if word:
                    q.append(word)
                word = ""
        if word:
            q.append(word)
        res = []
        while q:
            res.append(q.pop())
        # SUPER IMPORTANT, concatenating strings is O(n^2), because strings are immutable and each concatenation copies the whole string. Building a list and joining is O(n).
        return " ".join(res)
