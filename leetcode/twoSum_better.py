# https://leetcode.com/problems/two-sum/
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for index, val in enumerate(nums):
        rem = target - val  # sunstracts current number from target and puts it to a dictionary
        if rem in d:  # after, it checks if the next one is already in dictionary
            return [d[rem], index]
        # if the difference is NOT in the dictionary, than it puts it in dictionary
        d[val] = index


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
