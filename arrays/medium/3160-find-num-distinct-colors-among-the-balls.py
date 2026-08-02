class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Ball : color
        # colors : num balls

        balls = {}
        colors = collections.defaultdict(int)
        res = []
        curr = 0
        for query in queries:
            ball, color = query[0], query[1]
            # Haven't seen ball before
            if ball not in balls:
                #new color 
                if colors[color] == 0:
                    balls[ball] = color
                    colors[color] = 1
                    curr += 1
                    res.append(curr)
                # a color used before
                else:
                    balls[ball] = color
                    colors[color] += 1
                    res.append(curr)
            # we haev seen this ball before
            else: 
                # is it the same color?
                if color == balls[ball]:
                    res.append(curr)
                # if a different color
                else:
                    oldColor = balls[ball]
                    balls[ball] = color
                    colors[oldColor] -= 1 
                    #lose a color
                    if colors[oldColor] == 0:
                        curr -= 1
                    # if in use then add one, if not then don't
                    if colors[color] > 0:
                        res.append(curr)
                    else:
                        curr += 1
                        res.append(curr)
                    colors[color] += 1
        return res