# https://leetcode.com/problems/palindrome-number/


def isPalindrome(x: int) -> bool:
    s = str(x)
    isp = True
    i = 0
    if len(s) % 2 == 0:
        d = len(s)/2 - 1
    else:
        d = (len(s) - 1)/2
    while (i <= d):
        if s[i] != s[len(s) - 1 - i]:
            isp = False
            break
        i = i + 1
    return isp


print(isPalindrome(12345321))
