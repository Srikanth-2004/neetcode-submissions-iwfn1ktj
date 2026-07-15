from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = defaultdict(list)
        for char in strs:
            x = "".join(sorted(char))
            strs_map[x].append(char)
        return list(strs_map.values())