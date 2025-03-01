import numpy as np
import matplotlib.pyplot as plt

def julia_set(c, x_min, x_max, y_min, y_max, width, height, max_iter):
    """Generate the Julia set."""
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    julia = np.zeros(Z.shape, dtype=int)

    for i in range(max_iter):
        with np.errstate(over='ignore', invalid='ignore'):
            Z = Z**2 + c
        mask = np.abs(Z) < 2
        julia += mask

    return julia

def box_counting(julia_set, box_sizes):
    """Estimate the fractal dimension using the box-counting method."""
    counts = []
    for size in box_sizes:
        # Ensure the Julia set dimensions are divisible by the box size
        if julia_set.shape[0] % size != 0 or julia_set.shape[1] % size != 0:
            raise ValueError(f"Box size {size} must divide the Julia set dimensions {julia_set.shape}.")
        
        # Divide the space into boxes of size `size`
        grid = (julia_set > 0).reshape(
            julia_set.shape[0] // size, size,
            julia_set.shape[1] // size, size
        )
        # Count the number of boxes containing at least one point of the Julia set
        N = np.sum(np.any(grid, axis=(1, 3)))
        counts.append(N)
    return counts

# Parameters for Julia set
c = -0.7 + 0.356j  # Complex parameter for Julia set
x_min, x_max = -1.5, 1.5
y_min, y_max = -1, 1
width, height = 800, 800  # Resolution
max_iter = 256  # Number of iterations

# Generate Julia set
julia = julia_set(c, x_min, x_max, y_min, y_max, width, height, max_iter)


# Box sizes for box-counting (must divide 800 evenly)
box_sizes = [1, 2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 80, 100, 200, 400, 800]

# Perform box-counting
counts = box_counting(julia, box_sizes)

# Estimate fractal dimension
epsilons = [1 / size for size in box_sizes]
log_N = np.log(counts)
log_inv_eps = np.log(1 / np.array(epsilons))

# Fit a line to estimate the fractal dimension
coefficients = np.polyfit(log_inv_eps, log_N, 1)
fractal_dimension = coefficients[0]

# Plot the box-counting results
plt.figure(figsize=(10, 6))
plt.scatter(log_inv_eps, log_N, color='b', label='Data Points')
plt.plot(log_inv_eps, np.polyval(coefficients, log_inv_eps), 'r--', label=f'Fit: D = {fractal_dimension:.2f}')
plt.xlabel('log(1/ε)')
plt.ylabel('log(N(ε))')
plt.title('Box-Counting Method for Fractal Dimension')
plt.legend()
plt.grid(True)
plt.savefig('box_counting.png')

print(f"Estimated Fractal Dimension: {fractal_dimension:.2f}")
