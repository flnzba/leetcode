"""
# previous solution 74 / 100 test cases successfull
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        splittedList = []
        for i in range(len(strs)):
            tmp = list(strs[i])
            splittedList.append(tmp)

        for i in range(len(strs)):
            intersect = list(set.intersection(*map(set, splittedList)))

        intersect = "".join(intersect)
        return intersect
"""

# Solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start by assuming the entire first string is the common prefix
        prefix = strs[0]
        
        # Iterate over all strings in the list
        for s in strs:
            # Update the prefix while the current string does not start with it
            while not s.startswith(prefix):
                # Shorten the prefix by removing the last character
                prefix = prefix[:-1]
                # If the prefix is empty, there are no common prefixes
                if not prefix:
                    return ""
        
        return prefix
