import matplotlib.pyplot as plt

def logistic_map(x, r):
    return r * x * (1 - x)

def find_fixed_points(r, x0=0.2, tolerance=1e-6, max_iterations=1000):
    x = x0
    trajectory = [x]  # Store the trajectory for plotting
    for _ in range(max_iterations):
        x_next = logistic_map(x, r)
        trajectory.append(x_next)
        if abs(x_next - x) < tolerance:
            return x_next, trajectory  # Return the fixed point and trajectory
        x = x_next
    return None, trajectory  # If no fixed point is found within max_iterations

def stability_analysis(fixed_point, r):
    if fixed_point is not None:
        derivative = r * (1 - 2 * fixed_point)
        if abs(derivative) < 1:
            stability = "stable"
        else:
            stability = "unstable"
        print(f"Fixed point {fixed_point:.6f} is {stability} for r = {r} (derivative = {derivative:.6f})")
    else:
        print(f"No fixed point found for r = {r} within the given tolerance.")

def plot_trajectory(trajectory, r, save_path=None):
    plt.figure()
    plt.plot(trajectory, marker='o', linestyle='-', markersize=4)
    plt.title(f"Logistic Map Trajectory for r = {r}")
    plt.xlabel("Iteration (n)")
    plt.ylabel("x_n")
    plt.grid(True)
    if save_path:
        plt.savefig(save_path)
    plt.close()

# Values of r to analyze
r_values = [1, 2, 3, 4]

for r in r_values:
    print(f"Analyzing for r = {r}")
    fixed_point, trajectory = find_fixed_points(r)
    stability_analysis(fixed_point, r)
    
    # Plot and save the trajectory
    plot_trajectory(trajectory, r, save_path=f"logistic_map_r_{r}.png")
    print(f"Plot saved as logistic_map_r_{r}.png\n")
