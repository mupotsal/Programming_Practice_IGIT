def rotate_string(originalString, start, end):
    # originalString = list(originalString)
    while (start < end):
        temp = originalString[start]
        originalString[start] = originalString[end]
        originalString[end] = temp
        start += 1
        end = end - 1


def left_rotate(originalString, direction, amount):
    if direction == 0:  # left rotation
        if amount == 0:
            return

        n = len(originalString)
        rotate_string(originalString, 0, amount - 1)
        rotate_string(originalString, amount, n - 1)
        rotate_string(originalString, 0, n - 1)

    elif direction == 1:
        if amount == 0:
            return
        n = len(originalString)
        rotate_string(originalString, 0, n - 1)
        rotate_string(originalString, 0, amount - 1)
        rotate_string(originalString, amount, n - 1)


def rotateTheString(originalString, direction, amount):
    originalString = list(originalString)
    for i in amount:
        left_rotate(originalString, direction, i)
    originalStrings = ""
    for i in originalString:
        originalStrings += i
    return (originalStrings)


def main():
    string = "Liberty"
    print(rotateTheString(string,0,[2,2]))
main()