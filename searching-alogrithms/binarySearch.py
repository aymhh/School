array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def binarySearch(array, value):

    arrayLength = len(array)

    if arrayLength%2 == "0":
        arrayMiddleValue = array[round(arrayLength/2)]
        print(f"{arrayMiddleValue} this is the middle value if the array is even")
    elif arrayLength%2 != "0":
        arrayMiddleValue = array[round((arrayLength - 1)/2)]
        print(f"{arrayMiddleValue} this is the middle value if the array is odd")

    if value == arrayMiddleValue:
        return print("found")
    elif (arrayLength > 1):
        print