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

    print(left_greater)
    print(right_smaller)
    return triplets_count


arr = [1, 8, 3, 19, 5, 15, 7, 12]
triplets_count = count_triplets(arr)
print(triplets_count)





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



############################

def count_triplets(arr):
    n = len(arr)
    indexed_arr = [(arr[i], i) for i in range(n)]

    sorted_arr, _ = merge_sort(indexed_arr)

    bit = [0] * n
    right_smaller = [0] * n

    for i in range(n - 1, -1, -1):
        count = query(bit, sorted_arr[i][1] - 1)
        right_smaller[sorted_arr[i][1]] = count
        update(bit, sorted_arr[i][1], 1)

    triplets_count = 0
    bit = [0] * n  # Reset the Binary Indexed Tree
    for i in range(n):
        count = query(bit, n - 1) - query(bit, sorted_arr[i][1])
        triplets_count += right_smaller[sorted_arr[i][1]] * count
        update(bit, sorted_arr[i][1], 1)

    return triplets_count


def query(bit, index):
    result = 0
    while index > 0:
        result += bit[index]
        index -= index & -index
    return result


def update(bit, index, value):
    while index < len(bit):
        bit[index] += value
        index += index & -index


# The merge_sort function remains the same as in the previous implementation

arr = [4, 3, 2, 1]
triplets_count = count_triplets(arr)
print(triplets_count)
