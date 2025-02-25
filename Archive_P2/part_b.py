import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Parameters
x_density = 800
y_density = 800
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.0, 1.0
c = -0.7 + 0.356j
iterations = 256

# Create a grid of complex numbers
x = np.linspace(x_min, x_max, x_density)
y = np.linspace(y_min, y_max, y_density)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Initialize the output array
output = np.zeros(Z.shape, dtype=int)

# Iterate the function
for i in range(iterations):
    Z = Z**2 + c
    mask = (np.abs(Z) < 2)
    output += mask

# Identify points that belong to the Julia set
julia_points = np.column_stack((X[output == iterations], Y[output == iterations]))

# Compute the convex hull
hull = ConvexHull(julia_points)

# Calculate the area of the convex hull
area = hull.volume  # For 2D, hull.volume gives the area

# Plot the Julia set and the convex hull
plt.figure(figsize=(10, 10))
plt.imshow(output, extent=(x_min, x_max, y_min, y_max), cmap='hot', origin='lower')
plt.colorbar(label='Number of iterations')
plt.title(f'Julia Set (Area of Convex Hull = {area:.4f})')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')

# Plot the convex hull
for simplex in hull.simplices:
    plt.plot(julia_points[simplex, 0], julia_points[simplex, 1], 'b-', lw=2)

plt.savefig('convex_hull_of_snowflake.png')

print(f"Area of the convex hull: {area:.4f}")
