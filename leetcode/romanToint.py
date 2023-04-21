def romanToInt(s: str) -> int:
    roms = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    a = []
    d = []
    for i in range(len(s)):
        a.append(roms[s[i]])
    i = 0

    while i < len(a):
        if i == (len(a) - 1):
            d.append(a[i])
            i = i + 1
        else:
            if a[i] >= a[i+1]:
                d.append(a[i])
                i = i+1
            else:
                d.append(a[i+1] - a[i])
                i = i+2
    return sum(d)


print(romanToInt("MCMXCIV"))
print(romanToInt("MM"))
print(romanToInt("III"))
print(romanToInt("LVIII"))
