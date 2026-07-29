class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        arr.sort()
        for num in arr:
            #already paired
            if freq[num] == 0:
                continue
            if num < 0 and num % 2 != 0:
                #ex -5 % 2 = odd, not possible, odd neg case
                return False
            if num > 0:
                target = num * 2 #find something double it if positive
            else:
                target = num // 2 #double, but divide since negative
            if freq[target] == 0:
                return False
            freq[num] -= 1
            freq[target] -= 1
        return True