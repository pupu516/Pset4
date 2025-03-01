import numpy as np
import matplotlib.pyplot as plt

def modified_logistic_map(r, gamma, x0, n_iter, n_transient):
    x = x0
    for _ in range(n_transient):
        x = r * x * (1 - x**gamma)
    return x

def find_first_bifurcation(gamma, r_values, x0=0.5, n_iter=1000, n_transient=500):
    bifurcation_points = []
    for r in r_values:
        x = modified_logistic_map(r, gamma, x0, n_iter, n_transient)
        bifurcation_points.append(x)
    return bifurcation_points

# Parameters
gamma_values = np.linspace(0.5, 1.5, 100)
r_values = np.linspace(2.5, 4.0, 1000)
x0 = 0.5
n_iter = 1000
n_transient = 500

# Find first bifurcation points
first_bifurcation = []
for gamma in gamma_values:
    bifurcation_points = find_first_bifurcation(gamma, r_values, x0, n_iter, n_transient)
    first_bifurcation.append(bifurcation_points[0])

# Plot
plt.figure(figsize=(10, 6))
plt.plot(gamma_values, first_bifurcation, 'b-')
plt.xlabel('Gamma')
plt.ylabel('First Bifurcation Point')
plt.title('First Bifurcation Point vs Gamma')
plt.grid(True)
plt.savefig('part_e.png')
