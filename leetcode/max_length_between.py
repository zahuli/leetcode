# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

def maxLengthBetweenEqualCharacters(s: str) -> int:
    if (len(s) == 2):
        if (s[0] == s[1]):
            return 0
        else:
            return -1
    else:
        if (s[0] == s[-1]):
            return len(s) - 2
        else:
            r = s[1:]
            l = s[:-1]
            print(f"levi deo {l} {l[0]} {l[-1]}")
            print(f"desni deo {r} {r[0]} {r[-1]}")
            maxLengthBetweenEqualCharacters(l)
            maxLengthBetweenEqualCharacters(r)


print(maxLengthBetweenEqualCharacters('afca'))

# abcakajk
