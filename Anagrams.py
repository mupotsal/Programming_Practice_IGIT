def isAnagram1( s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
        print(dic1[item])
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2

def main():
    s = "abcd"
    t = "cdab"

    print(isAnagram1(s,t))

main()