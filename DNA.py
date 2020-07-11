def is_valid_input():
    string = "1234"
    for i in string:
        if i.isdigit() == False:
            return False
    else:
        return True

print(is_valid_input())