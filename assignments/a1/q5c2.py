import numpy as np
import matplotlib.pyplot as plt

def recompute_f0(n, c):
    # Initial conditions
    f0_original = 1
    f1_original = 1

    # Initialize arrays to store original and recomputed values
    original_f0_values = [f0_original]
    recomputed_f0_values = [f0_original]

    # Recompute f0 for k = n-2, n-3, ..., 0
    for k in range(n-2, -1, -1):
        f0_recomputed = f1_original - c * f0_original
        original_f0_values.append(f0_original)
        recomputed_f0_values.append(f0_recomputed)
        f1_original = f0_original
        f0_original = f0_recomputed

    return original_f0_values, recomputed_f0_values

# Number of terms to recompute
n_values = np.arange(2, 50)  # Adjust the range as needed
c = 1 + np.sqrt(3)/100  # Adjust the value of c as needed

# Plot both original and recomputed f0 for each n
for n in n_values:
    original_f0, recomputed_f0 = recompute_f0(n, c)
    plt.plot(range(n+1), original_f0, label=f'Original f0 (n={n})', linestyle='--', alpha=0.5)
    plt.plot(range(n+1), recomputed_f0, label=f'Recomputed f0 (n={n})', marker='o')

plt.xlabel('k')
plt.ylabel('f0')
plt.title(f'Original and Recomputed f0 for Various Values of n (c={c})')
plt.legend()
plt.grid(True)
plt.show()
