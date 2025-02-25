import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
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

# Create a folder for frames
frame_folder = "lorenz_frames_multi"
os.makedirs(frame_folder, exist_ok=True)

# Solve the system for each initial condition
solutions = [solve_ivp(lorenz, t_span, init, args=(sigma, rho, beta), t_eval=t_eval) for init in initial_conditions]

# Create and save frames
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(min(solutions[0].y[0]), max(solutions[0].y[0]))
ax.set_ylim(min(solutions[0].y[1]), max(solutions[0].y[1]))
ax.set_zlim(min(solutions[0].y[2]), max(solutions[0].y[2]))
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Lorenz System Trajectory Animation - Multiple Initial Conditions")

for i in range(0, len(t_eval), 10):  # Save every 10th frame
    ax.clear()
    ax.set_xlim(min(solutions[0].y[0]), max(solutions[0].y[0]))
    ax.set_ylim(min(solutions[0].y[1]), max(solutions[0].y[1]))
    ax.set_zlim(min(solutions[0].y[2]), max(solutions[0].y[2]))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Lorenz System Trajectory Animation - Multiple Initial Conditions")
    
    for solution, color in zip(solutions, colors):
        x, y, z = solution.y
        ax.plot(x[:i], y[:i], z[:i], lw=0.8, color=color)
    
    plt.savefig(f"{frame_folder}/frame_{i:04d}.png")

plt.close()

# Convert frames to a GIF
frames = [Image.open(f"{frame_folder}/frame_{i:04d}.png") for i in range(0, len(t_eval), 10)]
frames[0].save("lorenz_trajectory_multi.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)

print("GIF saved as lorenz_trajectory_multi.gif")

