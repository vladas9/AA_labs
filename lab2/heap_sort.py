
from benchmark import benchmark_function, plot_benchmark_results



def heapify_generator(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        yield arr.copy()
        yield from heapify_generator(arr, n, largest)

def heap_sort_generator(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify_generator(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        yield arr.copy()
        yield from heapify_generator(arr, i, 0)  


def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1 
    right = 2 * i + 2 

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 

        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0) 

if __name__ == "__main__":
    n_values = [10, 100, 500, 1000, 5000, 10000, 20000, 30000, 50000, 100000, 150000] 
    n_values, times, results = benchmark_function(heap_sort, n_values)
    plot_benchmark_results(n_values, times)
