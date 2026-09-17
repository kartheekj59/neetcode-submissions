from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # This hashmap stores sorted string as key and anagrams as values.
        groups = defaultdict(list)

        # Loop through every string in the input.
        for s in strs:

            # Sort characters of the string because anagrams have the same sorted form.
            key = ''.join(sorted(s))

            # Add the original string to the matching anagram group.
            groups[key].append(s)

        # Return all grouped anagrams as a list.
        return list(groups.values())