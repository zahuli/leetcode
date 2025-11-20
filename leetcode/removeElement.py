# https://leetcode.com/problems/remove-element/

def removeElements(nums: list, val: int) -> None:
    noElements = False
    while not (noElements):
        try:
            nums.remove(val)
        except:
            ValueError
            noElements = True
    return len(nums)


nums = [0, 1, 2, 2, 3, 0, 4, 2]
print(nums)

print(removeElements(nums, 2), nums)
