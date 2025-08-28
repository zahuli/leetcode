# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


def removeDuplicates(nums):
    i = 0
    while i <= len(nums) - 1:
        if i == len(nums) - 1:
            break
        elif nums[i] == nums[i+1]:
            nums.pop(i+1)
        else:
            i += 1
    return len(nums)


list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


print(removeDuplicates(list))

list2 = [1, 1, 2]
print(removeDuplicates(list2))
