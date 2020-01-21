def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end - 1


# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    if d == 0:
        return
    n = len(arr)
    rverseArray(arr, 0, d - 1)
    rverseArray(arr, d, n - 1)
    rverseArray(arr, 0, n - 1)
def main():
    the_string =list( 'abc')
    print(leftRotate(the_string, 1))
    the_string = str(the_string)
    print(the_string)
main()