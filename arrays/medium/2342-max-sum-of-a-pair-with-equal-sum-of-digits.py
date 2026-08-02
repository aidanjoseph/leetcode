class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def addDigits(num):
            strNum = str(num)
            res = 0 
            for char in strNum:
                res += int(char)
            return res
        res = float("-inf")
        digitsMap = {}
        #digit: {less than max, max}
        for num in nums:
            dig = addDigits(num)
            if dig not in digitsMap:
                digitsMap[dig] = num
            else:
                #if only one number in digitsMap
                # if len(digitsMap[dig]) == 1:
                #     res = max(res, digitsMap[dig][0] + num)
                #     if num < digitsMap[dig][0]:
                #         digitsMap[dig].insert(0, num)
                #     else:
                #         digitsMap[dig].append(num)
                # #two in digit map
                # else:
                #     #if less than
                #     if num < digitsMap[dig][0]:
                #         continue
                #     # if larger than both 
                #     elif num > digitsMap[dig][1]:
                #         res = max(res, digitsMap[dig][1] + num)
                #         digitsMap[dig][0] = digitsMap[dig][1]
                #         digitsMap[dig][1] = num
                #     else:
                #         #in middle
                #         res = max(res, digitsMap[dig][1] + num)
                #         digitsMap[dig][0] = num
                res = max(res, digitsMap[dig] + num)
                digitsMap[dig] = max(digitsMap[dig], num)
        if -1 > res:
            return -1
        return res
                        

