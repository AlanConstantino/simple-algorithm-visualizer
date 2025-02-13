import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_data(n=50, lower=1, upper=100):
    """
    Generate a list of n random integers between lower and upper.
    """
    return [random.randint(lower, upper) for _ in range(n)]

def bubble_sort(data):
    """
    Bubble Sort algorithm implemented as a generator.
    Yields the list state after each swap.
    """
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                yield data  # Yield the list state after each swap
        if not swapped:
            break

def visualize_sort(data):
    """
    Visualizes the Bubble Sort algorithm using matplotlib's animation.
    """
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort Visualization")
    
    # Create the bar chart
    bar_rects = ax.bar(range(len(data)), data, align="edge")
    ax.set_xlim(0, len(data))
    ax.set_ylim(0, max(data) + 10)
    
    # Display the iteration count on the plot
    iteration = [0]
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update_fig(data_state, rects, iteration):
        """
        Update function for the animation.
        """
        for rect, val in zip(rects, data_state):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"Iterations: {iteration[0]}")
        return rects

    anim = animation.FuncAnimation(
        fig,
        func=update_fig,
        fargs=(bar_rects, iteration),
        frames=bubble_sort(data.copy()),
        interval=50,
        repeat=False
    )
    
    plt.show()

if __name__ == "__main__":
    data = generate_data()
    visualize_sort(data)
