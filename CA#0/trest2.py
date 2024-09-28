def merge(arr, temp, left, mid, right):
    inv_count = 0
    i = left  # Starting index of left subarray
    j = mid  # Starting index of right subarray
    k = left  # Starting index of to be sorted subarray
    while (i <= mid - 1) and (j <= right):
        if arr[i] > arr[j]:
            print(f"arr[i]: {arr[i]}, arr[j]:{arr[j]}")
            print()
            temp[k] = arr[j]
            k += 1
            j += 1
            inv_count += (mid - i)

        else:
            temp[k] = arr[i]
            k += 1
            i += 1
    while i <= mid - 1:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inv_count


def _merge_sort(arr, temp, left, right):
    inv_count = 0
    if right > left:
        mid = (left + right) // 2
        inv_count += _merge_sort(arr, temp, left, mid)
        inv_count += _merge_sort(arr, temp, mid + 1, right)
        inv_count += merge(arr, temp, left, mid + 1, right)
    return inv_count


def count_inversions(arr):
    n = len(arr)
    temp = [0] * n
    return _merge_sort(arr, temp, 0, n - 1)


# Example usage:
arr = [1 , 8 , 3 ,19,5,  15, 8, 12]
result = count_inversions(arr)
print(f"Number of inversions: {result}")


def merge(arr, temp, left, mid, right):
    inv_count = 0
    i = left  # Starting index of left subarray
    j = mid  # Starting index of right subarray
    k = left  # Starting index of to be sorted subarray
    while (i <= mid - 1) and (j <= right):
        if arr[i] > arr[j]:
            temp[k] = arr[j]
            k += 1
            j += 1
            inv_count += (mid - i)
        else:
            temp[k] = arr[i]
            k += 1
            i += 1
    while i <= mid - 1:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inv_count


def _merge_sort(arr, temp, left, right):
    inv_count = 0
    if right > left:
        mid = (left + right) // 2
        inv_count += _merge_sort(arr, temp, left, mid)
        inv_count += _merge_sort(arr, temp, mid + 1, right)
        inv_count += merge(arr, temp, left, mid + 1, right)
    return inv_count


def count_inversions(arr):
    n = len(arr)
    temp = [0] * n
    return _merge_sort(arr, temp, 0, n - 1)


# Example usage:
arr = [1, 8, 3 ,19, 5, 15, 8, 12]
result = count_inversions(arr)
print(f"Number of inversions: {result}")


def find_triplets(arr):
    n = len(arr)
    triplets = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] > arr[j] > arr[k]:
                    triplets.append((i, j, k))
    return triplets

# Example usage:
arr = [1, 8, 3, 19, 5, 15, 7, 12]
triplets = find_triplets(arr)
print(f"Found {len(triplets)} triplets: {triplets}")


def merge(left, right):
    inversions = 0
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            inversions += len(left) - i
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])

    merged, inv_merge = merge(left, right)

    return merged, inv_left + inv_right + inv_merge


def count_triplets(arr):
    n = len(arr)
    _, inversions = merge_sort(arr)

    triplets = 0
    for i in range(1, n - 1):
        left_inversions = sum(1 for x in arr[:i] if x > arr[i])
        right_inversions = sum(1 for x in arr[i + 1:] if x > arr[i])

        triplets += left_inversions * right_inversions

    return triplets


arr = [1, 8, 3, 19, 5, 15, 8, 12]
triplets_count = count_triplets(arr)
print(triplets_count)


def count_triplets(arr):
    n = len(arr)
    left_greater = [0] * n
    right_smaller = [0] * n

    for i in range(1, n):
        count = 0
        for j in range(i):
            if arr[j] > arr[i]:
                count += 1
        left_greater[i] = count

    for i in range(n - 2, -1, -1):
        count = 0
        for j in range(n - 1, i, -1):
            if arr[j] < arr[i]:
                count += 1
        right_smaller[i] = count

    triplets_count = 0
    for i in range(n):
        triplets_count += left_greater[i] * right_smaller[i]

    return triplets_count


arr = [1, 8, 3, 19, 5, 15, 8, 12]
triplets_count = count_triplets(arr)
print(triplets_count)


def merge(left, right):
    merged = []
    inversions = 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i][0] > right[j][0]:
            inversions += len(left) - i
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])

    merged, inv_merge = merge(left, right)

    return merged, inv_left + inv_right + inv_merge


def count_triplets(arr):
    n = len(arr)
    indexed_arr = [(arr[i], i) for i in range(n)]

    sorted_arr, _ = merge_sort(indexed_arr)

    left_greater = [0] * n
    right_smaller = [0] * n

    for i in range(1, n):
        count = 0
        for j in range(i):
            if sorted_arr[j][1] < sorted_arr[i][1]:
                count += 1
        left_greater[sorted_arr[i][1]] = count

    for i in range(n - 2, -1, -1):
        count = 0
        for j in range(n - 1, i, -1):
            if sorted_arr[j][1] > sorted_arr[i][1]:
                count += 1
        right_smaller[sorted_arr[i][1]] = count

    triplets_count = 0
    for i in range(n):
        triplets_count += left_greater[i] * right_smaller[i]

    return triplets_count
