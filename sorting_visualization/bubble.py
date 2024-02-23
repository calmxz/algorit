import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def bubble_visualization(data):
    n = len(data)
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(data)), data, align="edge")
    iteration = [0]

    def update_fig(data, rects, iteration):
        for rect, val in zip(rects, data):
            rect.set_height(val)  
        iteration[0] += 1
        ax.set_title(f'Iteration {iteration[0]}') 
        
    def bubble(arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if (swapped == False):
                break
            yield list(arr)
    def update_speed(val):
        ani.event_source.interval = val

    ax_speed = plt.axes([0.1, 0.02, 0.8, 0.03])
    speed_slider = plt.Slider(ax=ax_speed, label='Speed', valmin=100, valmax=1000, valinit=500, valstep=100)
    speed_slider.on_changed(update_speed)

    plt.title('Bubble Sort Visualization') 
    ani = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration), frames=bubble(data), repeat=False, interval=500)
    plt.show()

# Example usage
data = [random.randint(1, 100) for _ in range(100)]
bubble_visualization(data)
