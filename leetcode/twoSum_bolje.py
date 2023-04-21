# https://leetcode.com/problems/two-sum/
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for index, val in enumerate(nums):
        rem = target - val  # oduzima trenutni broj od targeta i smesta u dictionary
        if rem in d:  # posle proverava da li je se sledeci vec nalazi u dic
            return [d[rem], index]
        d[val] = index  # ako se razlika ne nalazi u dic, onda ga smesta


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
