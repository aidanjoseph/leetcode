class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for item in strs:
            freq = [0] * 26
            for char in item:
                freq[ord(char) - ord("a")] += 1
            res[tuple(freq)].append(item)
        return list(res.values())