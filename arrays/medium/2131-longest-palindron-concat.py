class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        #frequency list of all the two letter words
        freq = Counter(words)
        res = 0 
        center = False #if we shove some random repeat in center for 2 extra

        for word in words:
            reverse = word[::-1] #reverse the word
            #case if we find a repeat
            if word == reverse: 
                pairs = freq[word] // 2 # divide floor by 2 to find num pairs
                res += pairs * 4 # each pair is 4
                freq[word] -= pairs * 2 #decrease in freq map for later
                if freq[word] == 1:
                    center = True
            else:
                #we find somethign like ab and ba
                if reverse in freq:
                    #take min freq for pairs
                    pairs = min(freq[word], freq[reverse])
                    res += pairs * 4
                    freq[word] -= pairs
                    freq[reverse] -= pairs
        if center:
            res += 2
        return res

        