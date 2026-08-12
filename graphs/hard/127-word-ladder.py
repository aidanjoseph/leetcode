class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord):
            return 0 
        words = set(wordList)
        if endWord not in words:
            return 0
        q = collections.deque([])
        q.append(beginWord)
        counter = 2

        while len(q) != 0:
            for _ in range(len(q)):
                temp = q.popleft()
                for j in range(len(temp)):
                    for k in "abcdefghijklmnopqrstuvwxyz":
                        new = temp[:j] + k + temp[j+1:]
                        if new == endWord:
                            return counter
                        if new in words:
                            q.append(new)
                            words.remove(new)
            counter += 1
        return 0