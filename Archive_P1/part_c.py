def logistic_map(x, r):
    return r * x * (1 - x)

def iterate_logistic_map(r, x0, threshold=1e-6, max_iterations=1000):
    x = x0
    trajectory = [x]  # Store the trajectory for plotting
    for iteration in range(max_iterations):
        x_next = logistic_map(x, r)
        trajectory.append(x_next)
        if abs(x_next - x) < threshold:
            return trajectory  # Return the trajectory
        x = x_next
    return trajectory  # Return the trajectory even if no convergence

# Values of r and initial conditions to analyze
r_values = [2, 3, 3.5, 3.8, 4.0]
initial_conditions = [0.1, 0.3, 0.5]

# Plot trajectories for each r and initial condition
import matplotlib.pyplot as plt

for r in r_values:
    plt.figure()
    for x0 in initial_conditions:
        trajectory = iterate_logistic_map(r, x0)
        plt.plot(trajectory, marker='o', linestyle='-', markersize=4, label=f"x0 = {x0}")
    plt.title(f"Logistic Map Trajectories for r = {r}")
    plt.xlabel("Iteration (n)")
    plt.ylabel("x_n")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"logistic_map_r_{r}_initial_conditions.png")
    plt.close()
    print(f"Plot saved as logistic_map_r_{r}_initial_conditions.png")
