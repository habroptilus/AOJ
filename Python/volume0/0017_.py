def _rot(c, i):
    if ord("a") < ord(c) and ord(c) < ord("z"):
        return chr((ord(c) - ord("a") + i) % 26 + ord("a"))
    if ord("A") < ord(c) and ord(c) < ord("Z"):
        return chr((ord(c) - ord("A") + i) % 26 + ord("A"))
    return c


def rot(str, i):
    g = [_rot(c, i) for c in str]
    return "".join(g)


def caesar(str):
    for i in range(26):
        s=".".join(rot(str, i).split()).split(".")
        if "the" in s or "that" in s or "this" in s:
            return rot(str,i)
    return 'none'


while True:
    try:
        line = input()
        print(caesar(line))
    except:
        break
