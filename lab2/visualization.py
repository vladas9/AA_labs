import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from quick_sort import quick_sort_generator
from merge_sort import merge_sort_generator
from heap_sort import heap_sort_generator
from bitonic_sort import bitonic_sort_generator_check



def visualize_sorting(sort_function, arr):
    frames = list(sort_function(arr.copy())) 
    
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(frames[0])), frames[0], align="edge")
    ax.set_ylim(0, max(arr) * 1.1) 

    def update(frame: int):
        for rect, val in zip(bar_rects, frames[frame]):
            rect.set_height(val)
        return bar_rects 

    ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=10, blit=False, repeat=False)

    plt.show()
    return ani 

def generate_random_array(n, min_val = 1, max_val = 100):
    return [random.randint(min_val, max_val) for _ in range(n)]

if __name__ == "__main__":
    arr = generate_random_array(100, 1, 100)
    ani = visualize_sorting(quick_sort_generator, arr)
