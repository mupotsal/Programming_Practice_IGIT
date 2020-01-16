def odd_occurence (my_list):
    minimum = -10000000
    key = - 1000000000000
    new_dict = {}
    for i in my_list:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1

    for i in new_dict:
        if (new_dict[i])%2 == 1:
            minimum = new_dict[i]
            key = i
    print("The number {} occurred {} times".format(key, minimum))


def main():
    mylist=[1,1,3,4,3]
    odd_occurence(mylist)

main()