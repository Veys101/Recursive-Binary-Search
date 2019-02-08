def binary_search(arr, head, tail, value):
    if tail >= head:

        mid = (head + tail) // 2

        if value == arr[mid]:
            return mid
        elif value > arr[mid]:
            return binary_search(arr, mid + 1, tail, value)
        else:
            return binary_search(arr, head, mid - 1, value)
    else:
        return -1


array = [10, 2, 1, 5, 7, 4, 3, 100, 50, 2, 8, 5, 10]
array.sort()
print(array)

print(binary_search(array, 0, len(array) - 1, 3))
