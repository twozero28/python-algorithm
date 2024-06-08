def selection_sort(arr, asc = True):
    new_arr = arr.copy()

    if asc:
        for i in range(len(new_arr)):
            smallest = new_arr[i]
            smallest_index = i

            for j in range(i + 1, len(new_arr)):
                if new_arr[j] < smallest:
                    smallest = new_arr[j]
                    smallest_index = j

            new_arr[smallest_index] = new_arr[i]
            new_arr[i] = smallest
    else:
        for i in range(len(new_arr)):
            biggest = new_arr[i]
            biggest_index = i

            for j in range(i + 1, len(new_arr)):
                if new_arr[j] > biggest:
                    biggest = new_arr[j]
                    biggest_index = j

            new_arr[biggest_index] = new_arr[i]
            new_arr[i] = biggest

    return new_arr

print(selection_sort([5, 3, 2, 10, 8, 1]))