class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        res = 0 
        remainders = collections.defaultdict(int)

        for hour in hours:
            if hour % 24 == 0:
                res += remainders[0]
            else:
                res += remainders[24-hour%24]
            remainders[hour%24] += 1
        return res
        