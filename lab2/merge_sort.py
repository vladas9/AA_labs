from benchmark import benchmark_function, plot_benchmark_results


def merge_generator(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
        yield arr.copy()

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
        yield arr.copy()

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1
        yield arr.copy()

def merge_sort_generator(arr, left= 0, right= None):
    if right is None:
        right = len(arr) - 1

    if left < right:
        mid = (left + right) // 2
        yield from merge_sort_generator(arr, left, mid)
        yield from merge_sort_generator(arr, mid + 1, right)
        yield from merge_generator(arr, left, mid, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


if __name__ == "__main__":
    n_values = [10, 100, 500, 1000, 5000, 10000, 20000, 30000, 50000, 100000, 150000] 
    n_values, times, results = benchmark_function(merge_sort, n_values)
    plot_benchmark_results(n_values, times)
