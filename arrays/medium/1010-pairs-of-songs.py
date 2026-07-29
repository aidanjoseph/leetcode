class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #mod everythign by 60
        #check how many of it's complements are in hashmap
        #add solution (i,j) to a set, check if that is in set
        #return length of set?
        remainders = collections.defaultdict(int)
        res = 0
        for t in time:
            if t % 60 == 0:
                res += remainders[0]
            else:
                res += remainders[60-t%60]
            remainders[t%60] += 1
        return res
        
        
        

        