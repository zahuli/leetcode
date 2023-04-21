def maxLengthBetweenEqualCharacters(s: str) -> int:
    max = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                d = j - i - 1
                if d > max:
                    max = d

    if max > 0:
        return max
    else:
        if (len(s) == 2) and ((s[0] == s[1])):
            return max
        else:
            return -1


print(maxLengthBetweenEqualCharacters('abcaa'))
