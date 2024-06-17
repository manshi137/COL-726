import numpy as np
import matplotlib.pyplot as plt

# Function to compute the next iteration based on the given recurrence relation
def iterate(x_prev, y_prev):
    x_next = 111 - (1130 - 3000/y_prev) / x_prev
    y_next = x_prev
    return x_next, y_next

# Initial point
x_true, y_true = 5, 5

# Perturbation values
perturbations = np.logspace(-16, 0, 17)  # Vary perturbation from 1e-16 to 1

# Arrays to store x_values and y_values for each perturbation
all_x_values = []
all_y_values = []

# Perform iterations for each perturbation
for perturbation in perturbations:
    x_init, y_init = x_true + perturbation, y_true + perturbation
    
    # Arrays to store the evolution of [xk+1, xk]
    x_values = np.zeros(0, dtype=np.float32)
    y_values = np.zeros(0, dtype=np.float32)
    x_values = [x_init]
    y_values = [y_init]

    # Perform iterations
    for _ in range(50):
        x_next, y_next = iterate(x_values[-1], y_values[-1])
        x_values.append(x_next)
        y_values.append(y_next)

    # Store x_values and y_values for this perturbation
    all_x_values.append(x_values)
    all_y_values.append(y_values)

# Plotting
plt.figure(figsize=(10, 6))

for i in range(len(perturbations)):
    plt.plot(all_x_values[i], all_y_values[i], label=f'Perturbation: {perturbations[i]:.1e}')

plt.xlabel('xk+1')
plt.ylabel('xk')
plt.title('Evolution of [xk+1, xk] for different perturbation values')
plt.legend()
plt.grid(True)
plt.show()
