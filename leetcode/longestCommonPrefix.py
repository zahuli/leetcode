
# https://leetcode.com/problems/longest-common-prefix/

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    minLen = 201
    for word in strs:
        if len(word) < minLen:
            prefix = word
            minLen = len(word)
    notFound = False
    while len(prefix) >= 0 and notFound == False:
        notFound = True
        for word in strs:
            if word.startswith(prefix) == False:
                notFound = False
                prefix = prefix[:-1]
                break
    return prefix


print(longestCommonPrefix(["nikola", "niko", "nikolica", "nikolas"]))

print(longestCommonPrefix(["dog", "racecar", "car"]))

print(longestCommonPrefix(["flower", "flow", "flight"]))

print(longestCommonPrefix(["aa", "ab"]))
