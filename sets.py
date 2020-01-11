# add remove find and create length
# Creating a set
my_set = {2}
print(type(my_set))
my_tuple = (2, 4, 5, "stri")
print(type(my_tuple))
this_set = set(my_tuple)  # set constructor
print(type(this_set))
my_list = [2, 3, 4, 5, 6, 7, 8, 8, 9]
my_set = set(my_list)
print(type(my_set))

# adding elements to a set
# add for one item

h = 15
my_set.add(h)
print(my_set)
age_list = [23, 22, 45, 78, 97]
list_of_ages = set(age_list)

my_set.update(list_of_ages)
print(my_set)

set_one = {3, 6, 9, 23}
set_two = {2, 4, 6, 8, 23}
set_three = set_one.union(set_two)
set_four = set_one.intersection(set_two)
print(set_three)
print(set_four)

# removing items from as set

set_num = {3, 4, 5, 9, 1, 2}
set_num.remove(4)

print(set_num)

set_num.pop()  # pop method removes an elemnt(is it random or not?)
print(set_num)

set_num.pop()
print(set_num)

# set_num.clear()
# print(set_num)

# finding the length of the set
print(len(set_num))

for i in set_num:
    print(i)


# Given an array of integers , arr = [3,1,1,2] find the duplicated element
def duplicates(arr):
    new_set = set()
    for i in arr:
        if i not in new_set:
            new_set.add(i)
        else:
            return i


arr = [3, 1, 1, 2]
print("The duplicated element is {}. Thanks ".format(duplicates(arr)))
