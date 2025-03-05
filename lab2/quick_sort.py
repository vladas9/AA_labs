from benchmark import benchmark_function, plot_benchmark_results

def lomuto_partition_generator(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        yield arr.copy() 
    arr[i], arr[high] = arr[high], arr[i]
    yield arr.copy()  
    return i

def quick_sort_generator(arr, low = 0, high = None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = yield from lomuto_partition_generator(arr, low, high)
        yield from quick_sort_generator(arr, low, pivot_index - 1)
        yield from quick_sort_generator(arr, pivot_index + 1, high)

def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = lomuto_partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    return arr


if __name__ == "__main__":
    n_values = [10, 100, 500, 1000, 5000, 10000, 20000, 30000, 50000, 100000, 150000] 
    n_values, times, results = benchmark_function(quick_sort, n_values)
    plot_benchmark_results(n_values, times)
