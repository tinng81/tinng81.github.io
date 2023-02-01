def reverseArray(array):
    return array[::-1]  # ar[start:stop:increment]

arr_count = int(input("Array Length:\n"))
arr = list(map(int, input("Input Array:\n").rstrip().split()))

result = reverseArray(arr)
print(result)
