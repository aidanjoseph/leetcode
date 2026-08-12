class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #basically longest window with 2 unique elements
        #seen index map

        seen = [[-1,0],[-1,0]]
        #Fruit type, last seen index
        # res = 0 
        # curr = 0 
        # for index, fruit in enumerate(fruits):
        #     if fruit == seen[0][0]:
        #         seen[0][1] = index 
        #         curr += 1
        #     elif fruit == seen[1][0]:
        #         seen[1][1] = index 
        #         curr += 1
        #     else: 
        #         if seen[0][0] == -1:
        #             seen[0][0] = fruit
        #             seen[0][1] = index
        #             curr += 1
        #         elif seen[1][0] == -1:
        #             seen[1][0] = fruit
        #             seen[1][1] = index
        #             curr += 1
        #         elif seen[0][1] < seen[1][1]:
        #             old_index = seen[0][1]
        #             seen[0][0] = fruit
        #             seen[0][1] = index
        #             curr = index - old_index

        #         else:
        #             old_index = seen[1][1]
        #             seen[1][0] = fruit
        #             seen[1][1] = index
        #             curr = index - old_index
        #     print(seen)
        #     res = max(curr, res)
        # return res


        seen = {}  # fruit -> last seen index
        left = 0
        res = 0

        for right, fruit in enumerate(fruits):
            seen[fruit] = right

            if len(seen) > 2:
                remove = min(seen, key=seen.get)
                left = seen[remove] + 1
                del seen[remove]

            res = max(res, right - left + 1)

        return res

        