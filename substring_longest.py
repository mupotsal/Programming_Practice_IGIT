def longest_substring(s):
    nums_list = []
    y = len(s)
    for i in range(y):
        new_string = ""
        v = s[i:]
        print(v,i)
        for j in v:
            if j not in new_string:
                new_string += j
            else:
                break
        nums_list.append(len(new_string))

    print(nums_list)
    if nums_list:
        return max(nums_list)
    else:
        return 0

def main():
    s = "tmmzuxt"
    print(longest_substring(s))

main()