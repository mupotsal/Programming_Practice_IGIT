"""
trying to learn dictionaries in Python

adding
removing
iterating
searching

two methods: using curly brackest and using the dict constructor
"""

age_names = {"Liberty":25,"Tawanda":23,"Saffa":24,"Oginga":27}
print(age_names)
age_names["John"] =19 # This is how to add  in a dictinonary
print(age_names)
staff_ages ={"Groppo":40,"Paul":47,"Yeager":50}
age_names.update(staff_ages)
print("The updated one{}".format(age_names))
# an item involves a key and a value
# to print dictionary items do dictionary name.items
# to get the keys say dictionary .keys()

print(age_names.items())
print(age_names.keys())
print(age_names.values())
print(age_names.get("Saffa"))
# you can not use a value to get a key
age_names["Saffa"]=21
print(age_names.get("Saffa"))

#removing items from a dictionary

age_names.pop("Liberty")
print(age_names)
#age_names.clear()
#print(age_names)

for i,j in age_names.items():
    print(i,j)

for i in age_names.items():
    print(i)

arr = [1,2,1,1,2,3,1,5,4]

def duplicates(my_list):
    minimum = -10000000
    key = - 1000000000000
    new_dict = {}
    for i in my_list:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1

    for i in new_dict:
        if new_dict[i] > minimum:
            minimum = new_dict[i]
            key = i
    print("The number {} occurred {} times".format(key, minimum))

def mode_fun():
    pass

def main():
    #duplicates(arr)
    my_list = [2,3,4]
    my_dict = dict(my_list)
    print(my_dict.items())
main()