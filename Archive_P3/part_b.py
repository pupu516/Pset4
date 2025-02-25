import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Lorenz system definition
def lorenz(t, state, sigma, rho, beta):
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

# Parameters
sigma = 10
rho = 48
beta = 3

# Time range
t_span = (0, 12)
t_eval = np.linspace(0, 12, 5000)

# Initial conditions (three slightly different ones)
initial_conditions = [[1.0, 1.0, 1.0], [1.01, 1.0, 1.0], [1.0, 1.01, 1.0]]
colors = ['blue', 'red', 'green']

# Plot the Lorenz attractors
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

for init, color in zip(initial_conditions, colors):
    solution = solve_ivp(lorenz, t_span, init, args=(sigma, rho, beta), t_eval=t_eval)
    x, y, z = solution.y
    ax.plot(x, y, z, lw=0.5, color=color, label=f'Init: {init}')
    
    # Mark the start and end points
    ax.scatter(x[0], y[0], z[0], color=color, marker='o', s=50, label=f'Start {init}')
    ax.scatter(x[-1], y[-1], z[-1], color=color, marker='x', s=50, label=f'End {init}')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Lorenz Attractor with Different Initial Conditions")
ax.legend()
plt.savefig('part_b.png')

