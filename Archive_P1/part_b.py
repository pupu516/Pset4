def logistic_map(x, r):
    return r * x * (1 - x)

def iterate_logistic_map_dp(r, x0=0.2, threshold=1e-6, max_iterations=1000):
    # DP table to store computed values of x_n
    dp_table = {}
    x = x0
    trajectory = [x]  # Store the trajectory for plotting
    for iteration in range(max_iterations):
        if x in dp_table:
            x_next = dp_table[x]  # Reuse previously computed value
        else:
            x_next = logistic_map(x, r)
            dp_table[x] = x_next  # Store the computed value in the DP table
        trajectory.append(x_next)
        if abs(x_next - x) < threshold:
            return x_next, iteration + 1, trajectory  # Return final value, iterations, and trajectory
        x = x_next
    return None, max_iterations, trajectory  # If no convergence within max_iterations

# Values of r to analyze
r_values = [2, 3, 3.5, 3.8, 4.0]

for r in r_values:
    final_value, iterations, trajectory = iterate_logistic_map_dp(r)
    if final_value is not None:
        print(f"For r = {r}, the logistic map converges to {final_value:.6f} in {iterations} iterations.")
    else:
        print(f"For r = {r}, the logistic map did not converge within the maximum number of iterations.")

    # Optional: Plot the trajectory
    import matplotlib.pyplot as plt
    plt.figure()
    plt.plot(trajectory, marker='o', linestyle='-', markersize=4)
    plt.title(f"Logistic Map Trajectory for r = {r}")
    plt.xlabel("Iteration (n)")
    plt.ylabel("x_n")
    plt.grid(True)
    plt.savefig(f"logistic_map_r_{r}.png")
    plt.close()
    print(f"Plot saved as logistic_map_r_{r}.png\n")
