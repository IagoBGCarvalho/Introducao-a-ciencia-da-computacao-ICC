def length(s):
    if s == "":
        return 0
    return 1 + length(s[1:])

def concat(s1, s2):
    if s1 == "":
        return s2
    return s1[0] + concat(s1[1:], s2)

def rev(s):
    if s == "":
        return s
    return rev(s[1:]) + s[0]

def prefix(s1, s2):
    if s1 == "":
        return True
    if s2 == "":
        return False
    if s1[0] != s2[0]:
        return False
    return prefix(s1[1:], s2[1:])

s1 = input().strip()
s2 = input().strip()

print(concat(s1, s2))
print(rev(s1))
print(prefix(s1, s2))
