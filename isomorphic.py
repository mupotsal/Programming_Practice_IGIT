def isIsomorphic(s,t) -> bool:
    s_dict = {}  # this dictionary will keep the values
    for i in range(len(s)):
        if s[i] not in s_dict.keys():
            if t[i] not in s_dict.values():
                s_dict[s[i]] = t[i]
            elif t[i] in s_dict.values():
                return "false"
        elif s[i] in s_dict.keys():
            if t[i] != s_dict[s[i]] or s_dict[s[i]] != t[i]:
                return "false"

    return "true"
def main():
    s=  "ab"
    t ="aa"
    print(isIsomorphic(s,t))

main()