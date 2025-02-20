import numpy as np
import matplotlib.pyplot as plt

# Define the logistic map function
def logistic_map(x, r):
    return r * x * (1 - x)

# Parameters
r_values = [1.0, 3.0, 3.45, 3.544, 3.564, 3.57, 3.83, 4.0]  # Critical r values
x0 = 0.2  # Initial condition
iterations = 1000  # Total iterations
last = 100  # Plot the last 100 iterations

# Simulate and plot for each r
for i, r in enumerate(r_values):
    # Initialize
    x = np.zeros(iterations)
    x[0] = x0

    # Iterate the logistic map
    for n in range(1, iterations):
        x[n] = logistic_map(x[n-1], r)

    # Plot the last 'last' iterations
    plt.figure()
    plt.plot(range(iterations - last, iterations), x[-last:], 'b-', label=f'r = {r}')
    plt.xlabel('Iteration (n)')
    plt.ylabel('x_n')
    plt.title(f'Logistic Map Behavior for r = {r}')
    plt.legend()
    plt.grid(True)

    # Save the plot
    plt.savefig(f'logistic_map_r_{i+1}.png')
    plt.close()

print("Graphs saved as 'logistic_map_r_1.png' to 'logistic_map_r_8.png'.")
