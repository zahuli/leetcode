# https://leetcode.com/problems/valid-parentheses/

def isValid(s: str) -> bool:
    opened = {"{", "[", "("}
    closed = {"}", "]", ")"}
    if (len(s) % 2 != 0) or s[0] in closed or s[-1] in opened:
        return False
    else:
        last_opened = []
        for i in range(len(s)):
            if s[i] in closed and len(last_opened) == 0:
                return False
            if s[i] in opened:
                last_opened.append(s[i])
            if s[i] in closed:
                if last_opened[-1] == "(" and s[i] in {"}", "]"}:
                    return False
                elif last_opened[-1] == "[" and (s[i] in {"}", ")"}):
                    return False
                elif last_opened[-1] == "{" and (s[i] in {"]", ")"}):
                    return False
                else:
                    last_opened.pop()
        if len(last_opened) == 0:
            return True
        else:
            return False


print(isValid("[[[]"))
print(isValid("(()]"))
print(isValid("((()))"))
print(isValid("()[]{}"))
print(isValid("[([]])"))
