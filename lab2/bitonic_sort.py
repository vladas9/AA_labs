from benchmark import benchmark_function, plot_benchmark_results



def bitonic_compare(arr, low, cnt, direction):
    half = cnt // 2
    for i in range(low, low + half):
        if (arr[i] > arr[i + half]) == direction:
            arr[i], arr[i + half] = arr[i + half], arr[i]

def bitonic_merge(arr, low, cnt, direction):
    if cnt > 1:
        bitonic_compare(arr, low, cnt, direction)
        half = cnt // 2
        bitonic_merge(arr, low, half, direction)
        bitonic_merge(arr, low + half, half, direction)

def bitonic_sort(arr, low, cnt, direction):
    if cnt > 1:
        half = cnt // 2
        bitonic_sort(arr, low, half, True)  
        bitonic_sort(arr, low + half, half, False) 
        bitonic_merge(arr, low, cnt, direction)

def bitonic_sort_check(arr):
    n = len(arr)
    if n & (n - 1) != 0: 
        raise ValueError("Bitonic sort requires array length to be a power of 2.")
    
    bitonic_sort(arr, 0, n, True)
    return arr

def bitonic_compare_generator(arr, low, cnt, direction):
    half = cnt // 2
    for i in range(low, low + half):
        if (arr[i] > arr[i + half]) == direction:
            arr[i], arr[i + half] = arr[i + half], arr[i]
    yield arr.copy()

def bitonic_merge_generator(arr, low, cnt, direction):
    if cnt > 1:
        yield from bitonic_compare_generator(arr, low, cnt, direction)
        half = cnt // 2
        yield from bitonic_merge_generator(arr, low, half, direction)
        yield from bitonic_merge_generator(arr, low + half, half, direction)

def bitonic_sort_generator(arr, low, cnt, direction):
    if cnt > 1:
        half = cnt // 2
        yield from bitonic_sort_generator(arr, low, half, True)  
        yield from bitonic_sort_generator(arr, low + half, half, False)  
        yield from bitonic_merge_generator(arr, low, cnt, direction)

def bitonic_sort_generator_check(arr):
    n = len(arr)
    print(n)
    if n & (n - 1) != 0:  
        raise ValueError("Bitonic sort requires array length to be a power of 2.")
    
    yield from bitonic_sort_generator(arr, 0, n, True)


if __name__ == "__main__":
    n_values = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]
    n_values, times, results = benchmark_function(bitonic_sort_check, n_values)
    plot_benchmark_results(n_values, times)
