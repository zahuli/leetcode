# https://leetcode.com/problems/two-sum/
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums) - 1):
        j = i + 1
        while (j < len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            j = j+1


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
