from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            anagram_groups[key].append(s)
        return list(anagram_groups.values())
