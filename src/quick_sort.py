def quick_sort(arr, asc = True):
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[0]
    less = [i for i in arr[1:] if i < pivot]
    greater = [i for i in arr[1:] if i >= pivot]

    if asc:
        return quick_sort(less) + [pivot] + quick_sort(greater)
    else:
        return quick_sort(greater, False) + [pivot] + quick_sort(less, False)

ex_arr = [5, 10, 1, 30, 12, 13]
print(quick_sort(ex_arr))
print(quick_sort(ex_arr, False))