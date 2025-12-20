import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# BUBBLE SORT (CAPTURE STATES)
def bubble_sort_states(arr):
    """Perform bubble sort but capture the array state after every swap."""
    a = arr.copy()
    n = len(a)
    states = [a.copy()]  # save initial state

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                states.append(a.copy())  # save after swap
                swapped = True
        if not swapped:  # optimized bubble sort
            break
    return states

# GENERATE RANDOM ARRAY 
np.random.seed(1)
n = 30
arr = np.random.randint(1, 100, size=n)
states = bubble_sort_states(arr)
print(f"Total Frames: {len(states)}")

# PLOT & ANIMATION 
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.bar(range(n), states[0])
ax.set_title("Bubble Sort Animation")
ax.set_xlabel("Index")
ax.set_ylabel("Value")
ax.set_ylim(0, max(arr) * 1.1)
# SPEED CONTROL VARIABLE 
speed = 200  # default speed (milliseconds)

def update(frame):
    """Update bar heights for animation frame."""
    for bar, height in zip(bars, states[frame]):
        bar.set_height(height)
    ax.set_title(f"Bubble Sort Animation — Step {frame}/{len(states)-1}")
    return bars
anim = animation.FuncAnimation(fig, update, frames=len(states), interval=speed)
plt.show()
